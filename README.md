# GitLab Docker Image for ARM64

[![build-badge][github-actions-badge]][github-actions]
[![Docker Pulls][dockerhub-badge-pulls]][dockerhub]

[![Docker Image Size (tag)][dockerhub-badge-image-size-ce]][dockerhub]
[![Docker Image Size (tag)][dockerhub-badge-image-size-ee]][dockerhub]
[![Docker Image Size (tag)][dockerhub-badge-image-size-15-ce]][dockerhub]
[![Docker Image Size (tag)][dockerhub-badge-image-size-15-ee]][dockerhub]
[![Docker Image Size (tag)][dockerhub-badge-image-size-16.0-ce]][dockerhub]
[![Docker Image Size (tag)][dockerhub-badge-image-size-16.0-ee]][dockerhub]
[![Docker Image Size (tag)][dockerhub-badge-image-size-16.1-ce]][dockerhub]
[![Docker Image Size (tag)][dockerhub-badge-image-size-16.1-ee]][dockerhub]
[![Docker Image Size (tag)][dockerhub-badge-image-size-16.2-ce]][dockerhub]
[![Docker Image Size (tag)][dockerhub-badge-image-size-16.2-ee]][dockerhub]
[![Docker Image Size (tag)][dockerhub-badge-image-size-16.3-ce]][dockerhub]
[![Docker Image Size (tag)][dockerhub-badge-image-size-16.3-ee]][dockerhub]

[![Docker Image Version (latest by date)][dockerhub-badge-latest-version-ce]][dockerhub]
[![Docker Image Version (latest by date)][dockerhub-badge-latest-version-ee]][dockerhub]
[![Docker Image Version (latest by date)][dockerhub-badge-latest-version-15-ce]][dockerhub]
[![Docker Image Version (latest by date)][dockerhub-badge-latest-version-15-ee]][dockerhub]
[![Docker Image Version (latest by date)][dockerhub-badge-latest-version-16.0-ce]][dockerhub]
[![Docker Image Version (latest by date)][dockerhub-badge-latest-version-16.0-ee]][dockerhub]
[![Docker Image Version (latest by date)][dockerhub-badge-latest-version-16.1-ce]][dockerhub]
[![Docker Image Version (latest by date)][dockerhub-badge-latest-version-16.1-ee]][dockerhub]
[![Docker Image Version (latest by date)][dockerhub-badge-latest-version-16.2-ce]][dockerhub]
[![Docker Image Version (latest by date)][dockerhub-badge-latest-version-16.2-ee]][dockerhub]
[![Docker Image Version (latest by date)][dockerhub-badge-latest-version-16.3-ce]][dockerhub]
[![Docker Image Version (latest by date)][dockerhub-badge-latest-version-16.3-ee]][dockerhub]

[github-actions]: https://github.com/naizhao/gitlab-arm64/actions/workflows/build.yml
[github-actions-badge]: https://github.com/naizhao/gitlab-arm64/actions/workflows/build.yml/badge.svg?branch=main
[dockerhub]: https://hub.docker.com/r/naizhao/gitlab-arm64/tags
[dockerhub-badge-pulls]: https://img.shields.io/docker/pulls/naizhao/gitlab-arm64?logo=docker
[dockerhub-badge-image-size-ce]: https://img.shields.io/docker/image-size/naizhao/gitlab-arm64/ce?label=gitlab-ce&logo=docker
[dockerhub-badge-image-size-ee]: https://img.shields.io/docker/image-size/naizhao/gitlab-arm64/ee?label=gitlab-ee&logo=docker
[dockerhub-badge-image-size-15-ce]: https://img.shields.io/docker/image-size/naizhao/gitlab-arm64/15-ce?label=gitlab-15-ce&logo=docker
[dockerhub-badge-image-size-15-ee]: https://img.shields.io/docker/image-size/naizhao/gitlab-arm64/15-ee?label=gitlab-15-ee&logo=docker
[dockerhub-badge-image-size-16.0-ce]: https://img.shields.io/docker/image-size/naizhao/gitlab-arm64/16.0-ce?label=gitlab-16.0-ce&logo=docker
[dockerhub-badge-image-size-16.0-ee]: https://img.shields.io/docker/image-size/naizhao/gitlab-arm64/16.0-ee?label=gitlab-16.0-ee&logo=docker
[dockerhub-badge-image-size-16.1-ce]: https://img.shields.io/docker/image-size/naizhao/gitlab-arm64/16.1-ce?label=gitlab-16.1-ce&logo=docker
[dockerhub-badge-image-size-16.1-ee]: https://img.shields.io/docker/image-size/naizhao/gitlab-arm64/16.1-ee?label=gitlab-16.1-ee&logo=docker
[dockerhub-badge-image-size-16.2-ce]: https://img.shields.io/docker/image-size/naizhao/gitlab-arm64/16.2-ce?label=gitlab-16.2-ce&logo=docker
[dockerhub-badge-image-size-16.2-ee]: https://img.shields.io/docker/image-size/naizhao/gitlab-arm64/16.2-ee?label=gitlab-16.2-ee&logo=docker
[dockerhub-badge-image-size-16.3-ce]: https://img.shields.io/docker/image-size/naizhao/gitlab-arm64/16.3-ce?label=gitlab-16.3-ce&logo=docker
[dockerhub-badge-image-size-16.3-ee]: https://img.shields.io/docker/image-size/naizhao/gitlab-arm64/16.3-ee?label=gitlab-16.3-ee&logo=docker
[dockerhub-badge-latest-version-ce]: https://img.shields.io/docker/v/naizhao/gitlab-arm64/ce?arch=arm64&logo=docker
[dockerhub-badge-latest-version-ee]: https://img.shields.io/docker/v/naizhao/gitlab-arm64/ee?arch=arm64&logo=docker
[dockerhub-badge-latest-version-15-ce]: https://img.shields.io/docker/v/naizhao/gitlab-arm64/15-ce?arch=arm64&logo=docker
[dockerhub-badge-latest-version-15-ee]: https://img.shields.io/docker/v/naizhao/gitlab-arm64/15-ee?arch=arm64&logo=docker
[dockerhub-badge-latest-version-16.0-ce]: https://img.shields.io/docker/v/naizhao/gitlab-arm64/16.0-ce?arch=arm64&logo=docker
[dockerhub-badge-latest-version-16.0-ee]: https://img.shields.io/docker/v/naizhao/gitlab-arm64/16.0-ee?arch=arm64&logo=docker
[dockerhub-badge-latest-version-16.1-ce]: https://img.shields.io/docker/v/naizhao/gitlab-arm64/16.1-ce?arch=arm64&logo=docker
[dockerhub-badge-latest-version-16.1-ee]: https://img.shields.io/docker/v/naizhao/gitlab-arm64/16.1-ee?arch=arm64&logo=docker
[dockerhub-badge-latest-version-16.2-ce]: https://img.shields.io/docker/v/naizhao/gitlab-arm64/16.2-ce?arch=arm64&logo=docker
[dockerhub-badge-latest-version-16.2-ee]: https://img.shields.io/docker/v/naizhao/gitlab-arm64/16.2-ee?arch=arm64&logo=docker
[dockerhub-badge-latest-version-16.3-ce]: https://img.shields.io/docker/v/naizhao/gitlab-arm64/16.3-ce?arch=arm64&logo=docker
[dockerhub-badge-latest-version-16.3-ee]: https://img.shields.io/docker/v/naizhao/gitlab-arm64/16.3-ee?arch=arm64&logo=docker
[ghcr]: https://github.com/naizhao/gitlab-arm64/pkgs/container/gitlab-arm64

English | [简体中文](./README.zh-Hans.md)

## What is this?

In recent years, ARM servers have become more and more widely used. Due to their flexibility,
small size, efficiency, and low price, ARM processors are a great choice for infrastructure.

Several top cloud vendors in the world have invested in ARM servers and launched ARM products,
including Amazon AWS, Azure, Google Cloud, Oracle Cloud, Huawei Cloud, etc.

However, the official GitLab docker image does not provide ARM64 version, which makes it
difficult for ARM users to use GitLab. Actually, GitLab has provided ARM64 version for a long
time, it's just that the official docker image is not built for ARM64.

This project is to build GitLab docker image for ARM64 use GitLab's official dockerfile.

> Upstream dockerfile: <https://gitlab.com/gitlab-org/omnibus-gitlab/-/tree/master/docker>
>
> This project is based on the official dockerfile, and only adds a few lines of code to make
> it work on ARM64.

## How to use it?

This project aims to provide an ARM64 image that is eactly the same as the official x86_64
image. So you can use it in the same way as the official image.

Refer to the official docker installation documentation:

- <https://docs.gitlab.com/omnibus/docker/>

## How to get image?

### Pull prebuilt image from DockerHub/GitHub Container Registry

This project provides at least one pre-built image for each minor release of GitLab CE/EE
since 13.12.

Checkout all available tags on [DockerHub][dockerhub] or [GitHub Container Registry][ghcr].

Pull image from DockerHub:

```sh
# Pull latest GitLab CE image
docker pull naizhao/gitlab-arm64:ce
# Pull latest GitLab CE 16 image
docker pull naizhao/gitlab-arm64:16-ce
# Pull latest GitLab EE image
docker pull naizhao/gitlab-arm64:ee
# Pull latest GitLab EE 16 image
docker pull naizhao/gitlab-arm64:16-ee
# Pull specific version of GitLab image
docker pull naizhao/gitlab-arm64:15.7.0-ce.0
docker pull naizhao/gitlab-arm64:16.0.1-ce.0
```

> Note:
>
> **ce** is community edition, **ee** is enterprise edition.
>
> Community edition is free and open source, enterprise edition is commercial but more features.
>
> If you don't know which edition to choose, see <https://about.gitlab.com/install/ce-or-ee/>.
> Or just choose community edition.

### Build image manually

Preqrequisites: ARM64 linux machine, docker installed.

1. Clone this project

   ```sh
   git clone https://github.com/zengxs/gitlab-docker.git
   ```

2. Check the version of GitLab you want to build

   Version used in this example: `15.7.0-ce.0`

   See <https://packages.gitlab.com/gitlab/gitlab-ce> or <https://packages.gitlab.com/gitlab/gitlab-ee> for available versions.

3. Build image

   ```sh
   cd gitlab-docker
   # Build GitLab CE image
   docker build . \
      -t gitlab-ce:15.9.0-ce.0 \
      --build-arg RELEASE_PACKAGE=gitlab-ce \
      --build-arg RELEASE_VERSION=15.9.0-ce.0
   # Build GitLab EE image
   docker build . \
      -t gitlab-ee:15.9.0-ee.0 \
      --build-arg RELEASE_PACKAGE=gitlab-ee \
      --build-arg RELEASE_VERSION=15.9.0-ee.0
   ```
