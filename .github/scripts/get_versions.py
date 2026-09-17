#!/usr/bin/env python3
"""解析本次 CI 需要构建的 GitLab 版本。

为什么不再用 atom feed：
    feed 只返回最近 ~14 个 tag（大约 2~3 个 minor）。某个 minor 的补丁周期一旦
    错过这个窗口，就再也不会被构建 —— 18.8 / 18.9 就是这么丢的，而 18.8 恰好是
    GitLab 升级路径上必须停留（required upgrade stop）的版本。
    tags API 一页 100 个 tag，覆盖约 12 个 minor（约一年），足够撑过每个 minor
    的整个补丁周期。

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


def main():
    names = fetch_tags()
    latest = latest_patch_per_minor(names)
    log(f"tags API 返回 {len(names)} 个 tag，解析出 {len(latest)} 个 minor")

    requested = (os.environ.get("INPUT_VERSIONS") or "").replace(",", " ").split()
    if requested:
        versions = []
        for item in requested:
            item = item.strip().lstrip("v")
            if not item:
                continue
            if re.fullmatch(r"\d+\.\d+", item):
                if item not in latest:  # 页外的老 minor，按 minor 搜索一次
                    latest.update(latest_patch_per_minor(fetch_tags(search=f"v{item}.")))
                if item not in latest:
                    raise SystemExit(f"找不到 {item} 的任何版本")
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

    latest_version = max(versions, key=version_key)
    log("待处理: " + ", ".join(versions))
    log(f"最新版本: {latest_version}")

    lines = [f"versions={json.dumps(versions)}", f"latest_version={latest_version}"]
    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a", encoding="utf-8") as handle:
            handle.write("\n".join(lines) + "\n")
    else:
        print("\n".join(lines))


if __name__ == "__main__":
    main()
