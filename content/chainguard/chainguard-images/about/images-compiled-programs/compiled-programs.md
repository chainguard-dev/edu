---
title: "Choosing a Container for your Compiled Programs"
linktitle: "Selecting a Container"
aliases: 
- /chainguard/chainguard-images/working-with-images/compiled-programs/
- /chainguard/chainguard-images/working-with-images/images-compiled-programs/compiled-programs
- /chainguard/chainguard-images/working-with-images/about/images-compiled-programs/compiled-programs
type: "article"
description: "An overview comparing various Chainguard Containers for compiled programs"
date: 2024-07-12T17:55:01+00:00
lastmod: 2025-04-07T18:42:57+00:00
draft: false
tags: ["Chainguard Containers", "Product", "Cheatsheet"]
images: []
menu:
  docs:
    parent: "about"
weight: 205
toc: true
---

When selecting the right base image for your application, there are a variety of factors to take into consideration. For starters, it is critical that your application has all of the dependencies it needs to run. The ideal base image will contain the essential packages you need, while leaving out the ones you don’t. However, in practice, you will need to build upon your container images so they meet your specific needs, making it all the more important that you have a strong foundation.

In this guide, we will explore a variety of Chainguard Containers which are suitable for different compiled applications. We will take a look at their availability and use-case differences so you can move closer to settling on the best base image for your specific needs.


## Available Container Containers

### wolfi-base

The [`wolfi-base`](https://images.chainguard.dev/directory/image/wolfi-base/versions?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-images-compiled-programs-compiled-programs) Chainguard Container is a minimal container image based on the [Wolfi *un-distro*](https://github.com/wolfi-dev/), a community-oriented Linux distribution created by Chainguard to facilitate image builds. The `wolfi-base` image contains `busybox` and `apk-tools` so that you can build your own packages for a custom image. It also supports `glibc`.

{{< details "What is Wolfi?" >}}
{{< blurb/wolfi >}}
{{< /details >}}

The following packages are included in the `wolfi-base:latest` Chainguard Containers:
- `apk-tools`
- `busybox`
- `ca-certificates-bundle`
- `chainguard-baselayout`
- `glibc`
- `glibc-locale-posix`
- `ld-linux`


### chainguard-base

*Paid Container* \
In addition to the functionality of the `wolfi-base` Chainguard Container, [`chainguard-base`](https://images.chainguard.dev/directory/image/chainguard-base/versions?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-images-compiled-programs-compiled-programs) reports as being a Chainguard Container, which scanners use to determine what security feeds to reference for vulnerabilities. Additionally, the `chainguard-base` container image provides access to vulnerability remediation SLAs to ensure your containers are always up-to-date with the latest releases and patches.

The following packages are included in the `chainguard-base:latest` Chainguard Container:
- `apk-tools`
- `busybox`
- `ca-certificates-bundle`
- `chainguard-baselayout`
- `glibc`
- `glibc-locale-posix`
- `ld-linux`

You can find the complete inventory of packages for the `chainguard-base` Chainguard Container at [its listing on the Chainguard Registry](https://images.chainguard.dev/directory/image/chainguard-base/versions?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-images-compiled-programs-compiled-programs).

### static

The Chainguard [`static`](https://images.chainguard.dev/directory/image/static/versions?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-images-compiled-programs-compiled-programs) base image is a Wolfi-based image available in one variant with the `:latest` tag. The `static` image is extremely minimal and is not intended to be run directly. It is used to host stand-alone, static binaries, like those produced by compilers such as `gcc`, `go`, and `rust`. It does not contain any programs you can run out-of-the-box. You must add your own static binaries to the image, for example using a Dockerfile multi-stage build.
 
The following packages are included in the `static:latest` Chainguard Container:
- `ca-certificates-bundle`
- `chainguard-baselayout`
- `glibc-locale-posix`
- `tzdata`
- `wolfi-baselayout`

You can find more information about the `static` Chainguard Container at [its listing on the Chainguard Registry](https://images.chainguard.dev/directory/image/static/versions?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-images-compiled-programs-compiled-programs).

### glibc-dynamic

The [`glibc-dynamic`](https://images.chainguard.dev/directory/image/glibc-dynamic/versions?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-images-compiled-programs-compiled-programs) Chainguard Container is best suited for when you need to host dynamically linked binaries that depend on the C standard library. Like the `static` image, `glibc-dynamic` is intended to be used as a base image only, and you must add your own binaries to the image.

The `glibc-dynamic` image is freely available in two variants: `:latest` and `:latest-dev`. The `:latest-dev` image adds additional packages which are not present in `:latest` to help facilitate application development. It is suggested to use the `:latest` image for production-facing purposes because of its smaller footprint. 

The following packages are included in the `glibc-dynamic:latest` Chainguard Container:
- `ca-certificates-bundle`
- `chainguard-baselayout`
- `glibc`
- `glibc-locale-posix`
- `ld-linux`
- `libgcc`
- `libstdc++`
- `wolfi-baselayout`

You can find more information about the `glibc-dynamic` Chainguard Container at [its listing on the Chainguard Registry](https://images.chainguard.dev/directory/image/glibc-dynamic/versions?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-images-compiled-programs-compiled-programs).

### cc-dynamic

The [`cc-dynamic`](https://images.chainguard.dev/directory/image/cc-dynamic/versions?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-images-compiled-programs-compiled-programs) Chainguard Container is deprecated. It is suggested that you use the `glibc-dynamic` image instead, as it is designed to replace `cc-dynamic`. You can find more information about the `cc-dynamic` image, such as its packages and licensing information, on the [Chainguard Registry](https://images.chainguard.dev/directory/image/cc-dynamic/advisories?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-images-compiled-programs-compiled-programs).

### gcc-glibc

The [`gcc-glibc`](https://images.chainguard.dev/directory/image/gcc-glibc/versions?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-images-compiled-programs-compiled-programs) Chainguard Container is best suited for building C applications which depend on `glibc`. There are two freely available variants of this image, `:latest` and `:latest-dev`. `:latest-dev` is a developer variant of the image which adds additional packages such as `bash` to facilitate the development process. 

In comparison to the `static` and `glibc-dynamic` Chainguard Containers, `gcc-glibc` is intended to be used to develop programs based on the C standard library, instead of simply hosting binaries. Because of this, it contains additional packages such as `make`, `busybox`, as well as `gcc` to compile programs.

The following packages are included in the `gcc-glibc:latest` Chainguard Container:
- `binutils`
- `build-base`
- `busybox`
- `ca-certificates-bundle`
- `gcc`
- `glibc`

You can find the complete inventory of packages for the `gcc-glibc` Chainguard Container at [its listing on the Chainguard Registry](https://images.chainguard.dev/directory/image/gcc-glibc/versions?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-images-compiled-programs-compiled-programs).

### glibc-openssl

*Paid Container* \
The [`glibc-openssl`](https://images.chainguard.dev/directory/image/glibc-openssl/versions?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-images-compiled-programs-compiled-programs) Chainguard Container is designed for C applications which depend on OpenSSL. It contains the `openssl` and `openssl-provider-legacy` packages to support this use-case. It comes in two variants,`latest` and `latest-dev`. As in the aforementioned images, `latest` is designed for deployment, while `latest-dev` contains additional packages to assist in program development such as a shell and package manager.

The following packages are included in the `glibc-openssl:latest` Chainguard Container:
- `ca-certificates-bundle`
- `chainguard-baselayout`
- `glibc`
- `glibc-locale-posix`
- `ld-linux`
- `openssl`
- `openssl-provider-legacy`

You can find the complete inventory of packages for the `glibc-openssl` Chainguard Container at [its listing on the Chainguard Registry](https://images.chainguard.dev/directory/image/glibc-openssl/versions?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-images-compiled-programs-compiled-programs).


## What About `musl`?

At the time of this writing, no Chainguard Containers come packaged with `musl`. Chainguard builds `glibc`-based container images because `glibc` is commonly used, which makes it easier for most developers to start consuming Chainguard Containers in their environments. Additionally, `glibc` is widely tested, making it a dependable choice for a C standard library implementation. As `glibc` is a well-established option, choosing to use `glibc` ensures more applications will be compatible with new images.

Though `musl` is sometimes chosen because of its minimal footprint, Chainguard’s distroless approach based on [Wolfi](https://www.chainguard.dev/unchained/introducing-wolfi-the-first-linux-un-distro) often results in a container image of comparable (or smaller) size than official `musl` based images. For more information, please refer to our [glibc vs. musl](/chainguard/chainguard-images/about/images-compiled-programs/glibc-vs-musl/) article. 

## Next Steps

Understanding the differences between various Chainguard Containers allows you to make informed decisions about what images to choose for your compiled applications. You can check out our complete suite of Chainguard Containers at the [Chainguard Registry](https://images.chainguard.dev/?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-images-compiled-programs-compiled-programs). To learn more about using Chainguard Containers, head to the [Chainguard Academy](/chainguard/chainguard-images/), where you can find documentation to help you start incorporating them into your workflow.

Interested in learning more about adopting Chainguard Containers for your organization? [Let’s get in touch!](https://www.chainguard.dev/contact)
