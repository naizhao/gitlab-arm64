#!/usr/bin/env python3
"""解析本次 CI 需要构建的 GitLab 版本。

为什么不再用 atom feed：
    feed 只返回最近 ~14 个 tag（大约 2~3 个 minor）。某个 minor 的补丁周期一旦
    错过这个窗口，就再也不会被构建 —— 18.8 / 18.9 就是这么丢的，而 18.8 恰好是
    GitLab 升级路径上必须停留（required upgrade stop）的版本。
    tags API 一页 100 个 tag，覆盖约 12 个 minor（约一年），足够撑过每个 minor
    的整个补丁周期。

为什么还要探测 deb 是否已发布：
    GitLab 会提前给下一个 minor 打 tag（例如 v19.4.0-ee），但对应的 deb 往往要
    几天后才发布。只看 tag 会把这种版本排进构建矩阵，导致该 job 必然失败，还可能
    把 latest / ee 这类移动标签指到不存在的版本上。

latest_version 为什么必须是全局最新：
    它取的是"所有已发布 minor 里最大的版本"，与 INPUT_VERSIONS 指定的子集无关。
    否则手动构建某个老版本（例如 versions=18.8）时，latest_version 会退化成
    18.8.11，把 latest / ee / <major>-ee 这些移动标签错误地移动过去。

用法（通过 INPUT_VERSIONS 环境变量）：
    INPUT_VERSIONS=""              取所有 minor 的最新 patch（定时任务用）
    INPUT_VERSIONS="18.8"          取 18.8 的最新 patch（页内没有时回退到 search 接口）
    INPUT_VERSIONS="18.8.11,19.0"  精确版本与 minor 混用

输出（写到 $GITHUB_OUTPUT；本地运行时直接打印）：
    versions=<JSON 数组>
    latest_version=X.Y.Z
"""

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

PROJECT_ID = 278964  # gitlab-org/gitlab
PER_PAGE = 100  # 一页≈12 个 minor，约一年
API = f"https://gitlab.com/api/v4/projects/{PROJECT_ID}/repository/tags"
RELEASE_PATTERN = re.compile(r"v(\d+\.\d+\.\d+)-ee$")  # 排除 rc / 其他后缀
PACKAGE_URL = (
    "https://packages.gitlab.com/gitlab/gitlab-ee/packages/ubuntu/jammy/"
    "gitlab-ee_{version}-ee.0_amd64.deb/download.deb"
)


def log(message):
    print(message, file=sys.stderr)


def fetch_tags(**params):
    query = urllib.parse.urlencode({"per_page": PER_PAGE, **params})
    url = f"{API}?{query}"
    try:
        with urllib.request.urlopen(url, timeout=60) as response:
            return [tag["name"] for tag in json.load(response)]
    except urllib.error.URLError as error:
        raise SystemExit(f"拉取 GitLab tags 失败: {error}") from error


def version_key(version):
    return tuple(int(part) for part in version.split("."))


def latest_patch_per_minor(names):
    """{minor: 该 minor 的最大 patch 版本}"""
    latest = {}
    for name in names:
        match = RELEASE_PATTERN.match(name)
        if not match:
            continue
        version = match.group(1)
        minor = ".".join(version.split(".")[:2])
        if minor not in latest or version_key(version) > version_key(latest[minor]):
            latest[minor] = version
    return latest


def package_published(version):
    """对应 deb 是否已发布。只有明确的 404 才算未发布，网络异常按已发布处理（不误杀）。"""
    request = urllib.request.Request(PACKAGE_URL.format(version=version), method="HEAD")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.status == 200
    except urllib.error.HTTPError as error:
        return error.code != 404
    except Exception:
        return True


def drop_unpublished(latest):
    for minor, version in list(latest.items()):
        if not package_published(version):
            log(f"跳过 {version}（{minor}）：对应的 deb 还没发布")
            del latest[minor]
    return latest


def main():
    names = fetch_tags()
    latest = drop_unpublished(latest_patch_per_minor(names))
    log(f"tags API 返回 {len(names)} 个 tag，其中 {len(latest)} 个 minor 有已发布的包")

    requested = (os.environ.get("INPUT_VERSIONS") or "").replace(",", " ").split()
    if requested:
        versions = []
        for item in requested:
            item = item.strip().lstrip("v")
            if not item:
                continue
            if re.fullmatch(r"\d+\.\d+", item):
                if item not in latest:  # 页外的老 minor，按 minor 搜索一次
                    latest.update(drop_unpublished(latest_patch_per_minor(fetch_tags(search=f"v{item}."))))
                if item not in latest:
                    raise SystemExit(f"找不到 {item} 的任何已发布版本")
                versions.append(latest[item])
            elif re.fullmatch(r"\d+\.\d+\.\d+", item):
                versions.append(item)
            else:
                raise SystemExit(f"无法解析的版本号: {item}")
        log(f"手工指定: {requested}")
    else:
        versions = sorted(latest.values(), key=version_key, reverse=True)

    seen = set()
    versions = [v for v in versions if not (v in seen or seen.add(v))]
    if not versions:
        raise SystemExit("没有解析到任何需要构建的版本")

    # 全局最新（与本次请求的子集无关），只有它才允许移动 latest / ee / <major>-ee
    latest_version = max(latest.values(), key=version_key)
    log("待处理: " + ", ".join(versions))
    log(f"全局最新版本: {latest_version}｜本次是否包含: {'是' if latest_version in versions else '否'}")

    lines = [f"versions={json.dumps(versions)}", f"latest_version={latest_version}"]
    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a", encoding="utf-8") as handle:
            handle.write("\n".join(lines) + "\n")
    else:
        print("\n".join(lines))


if __name__ == "__main__":
    main()
