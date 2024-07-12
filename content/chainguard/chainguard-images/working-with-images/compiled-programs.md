---
title: "Choosing an Image for your Compiled Programs"
linktitle: "Images for Compiled Programs"
aliases: 
type: "article"
description: "An overview comparing various Chainguard Images for compiled programs"
date: 2024-07-12T17:55:01+00:00
lastmod: 2024-07-12T18:23:31+00:00
draft: false
tags: ["Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 200
toc: true
---

When selecting the right base image for your application, there are a variety of factors to take into consideration. For starters, it is critical that your application has all of the dependencies it needs to run. The ideal base image will contain the essential packages you need, while leaving out the ones you don’t. However, in practice, you will need to build upon your images so they meet your specific needs, making it all the more important that you have a strong foundation.

In this guide, we will explore a variety of Chainguard Images which are suitable for different compiled applications. We will take a look at their availability, packages, and use-case differences so you can move closer to settling on the best base image for your specific needs.

## Available Images

### static
The Chainguard `static` base image is a Wolfi-based image available in one variant with the `:latest` tag. The `static` image is extremely minimal and is not intended to be run directly. It is used to host stand-alone, static binaries, like those produced by compilers such as `gcc`, `go`, and `rust`. It does not contain any programs you can run out-of-the-box. You must add your own static binaries to the image, for example using a Dockerfile multi-stage build.

The following packages are included in the `static:latest` Chainguard Image:
`ca-certificates-bundle`, `chainguard-baselayout`, `glibc-locale-posix`, `tzdata`, and `wolfi-baselayout`.

### glibc-dynamic
The `glibc-dynamic` Chainguard Image is best suited where you need to host dynamically linked binaries which depend on the C standard library. Like the `static` image, `glibc-dynamic` is intended to be used as a base image only, and you must add your own binaries to the image.

The `glibc-dynamic` image is freely available in two variants: `:latest` and `:latest-dev`. The `:latest-dev` image adds additional packages which are not present in `:latest` to help facilitate application development. It is suggested to use the `:latest` image for production-facing purposes because of its smaller footprint. 

The following packages are included in the `glibc-dynamic:latest` Chainguard Image:
`ca-certificates-bundle`, `chainguard-baselayout`, `glibc`, `glibc-locale-posix`, `ld-linux`, `libgcc`, `libstdc++`, and `wolfi-baselayout`.

### cc-dynamic
The `cc-dynamic` Chainguard Image is deprecated. It is suggested that you use the `glibc-dynamic` image instead, as it is designed to replace `cc-dynamic`.

### gcc-glibc
The `gcc-glibc` Chainguard Image is best suited for building C applications which depend on `glibc`. There are two freely available variants of this image, `:latest` and `:latest-dev`. `:latest-dev` is a developer variant of the image which adds additional packages such as `bash` to facilitate the development process. 

In comparison to the `static` and `glibc-dynamic` Chainguard Images, `gcc-glibc` is intended to be used to develop programs based on the C standard library, instead of simply hosting binaries. Because of this, it contains additional packages such as `make`, `busybox`, as well as `gcc` to compile programs.

The following packages are included in the `gcc-glibc:latest` Chainguard Image:
`binutils`, `build-base`, `busybox`, `ca-certificates-bundle`, `gcc`, `glibc`, `glibc-dev`, `glibc-locale-posix`, `gmp`, `isl`, `ld-linux`, `libatomic`, `libcrypt1`, `libgcc`, `libgo`, `libgomp`, `libstdc++`, `libstdc++-dev`, `libxcrypt`, `libxcrypt-dev`, `linux-headers`, `make`, `mpc`, `mpfr`, `nss-db`, `nss-hesiod`, `pkgconf`, `posix-cc-wrappers`, `wolfi-baselayout`, and `zlib`.

### glibc-openssl
*Paid Image* \
The `glibc-openssl` Chainguard Image is designed for C applications which depend on OpenSSL. It contains a few packages in addition to those found in the `glibc-dynamic` image to achieve this. It comes in two variants,`latest` and `latest-dev`. As in the aforementioned images, `latest` is designed for deployment, while `latest-dev` contains additional packages to assist in program development such as a shell and package manager.

The following packages are included in the `glibc-openssl:latest` Chainguard Image:
`ca-certificates-bundle`, `chainguard-baselayout`, `glibc`, `glibc-locale-posix`, `ld-linux`, `libcrypto3`, `libgcc`, `libssl3`, `libstdc++`, `openssl`, `openssl-provider-legacy`, and `wolfi-baselayout`.

### wolfi-base
The `wolfi-base` image is a minimal container image based on the [Wolfi *un-distro*](https://github.com/wolfi-dev/), a community-oriented Linux distribution created by Chainguard to facilitate image builds. The `wolfi-base` image contains `busybox` and `apk-tools` so that you can build your own packages for a custom image. It supports `glibc`.

The following packages are included in the `wolfi-base:latest` Chainguard Image:
`apk-tools`, `busybox`, `ca-certificates-bundle`, `chainguard-baselayout`, `glibc`, `glibc-locale-posix`, `ld-linux`, `libcrypt1`, `libcrypto3`, `libssl3`, `libxcrypt`, `wolfi-base`, `wolfi-baselayout`, `wolfi-keys`, and `zlib`.

### chainguard-base
*Paid Image* \
In addition to the functionality of the `wolfi-base` image, `chainguard-base` reports as being a Chainguard Image, which scanners use to determine what security feeds to reference for vulnerabilities. Additionally, the `chainguard-base` image provides access to vulnerability remediation SLAs to ensure your containers are always up-to-date with the latest releases and patches.

The following packages are included in the `chainguard-base:latest` Chainguard Image:
`apk-tools`, `busybox`, `ca-certificates-bundle`, `chainguard-baselayout`, `glibc`, `glibc-locale-posix`, `ld-linux`, `libcrypt1`, `libcrypto3`, `libssl3`, `libxcrypt`, `wolfi-base`, `wolfi-baselayout`, `wolfi-keys`, and `zlib`.


## What about musl?
At the time of this writing, no Chainguard Images come packaged with `musl`. Chainguard builds `glibc`-based images because `glibc` is commonly used, which makes it easier for most developers to start consuming Chainguard Images in their environments. Additionally, `glibc` is widely tested, making it a dependable choice for a C standard library implementation. As `glibc` is a well-established option, choosing to use `glibc` ensures more applications will be compatible with new images.

Though `musl` is sometimes chosen because of its minimal footprint, Chainguard’s distroless approach based on [Wolfi](https://www.chainguard.dev/unchained/introducing-wolfi-the-first-linux-un-distro) often results in a container image of comparable (or smaller) size than official `musl` based images. 

## Learn More
In this article, you learned about the differences between select Chainguard Images, allowing you to make informed decisions about what images to choose for your compiled applications. You can check out our complete suite of Chainguard Images at the [Chainguard Registry](https://images.chainguard.dev/). To learn more about using Chainguard Images, head to the [Chainguard Academy](/chainguard/chainguard-images/), where you can find documentation to help you start incorporating them into your workflow.

Interested in learning more about adopting Chainguard Images for your organization? [Let’s get in touch!](https://www.chainguard.dev/contact)
