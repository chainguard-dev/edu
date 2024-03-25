---
title: "Migrating Dockerfiles to Chainguard Images"
linktitle: "Migrating to Chainguard Images"
type: "article"
description: "Guidance on how to migrate existing Dockerfile workloads to use Chainguard Images"
date: 2024-03-25T15:56:52-07:00
lastmod: 2024-03-25T15:56:52-07:00
draft: false
tags: ["Images", "Product", "Conceptual"]
images: []
menu:
  docs:
    parent: "concepts"
weight: 100
toc: true
---

## Overview
Based on the [Wolfi](/open-source/wolfi/overview/) Linux _undistro_, Chainguard Images have special features designed for increased security and provenance attestation. Depending on your current base image and custom commands, you may need some adjustments when migrating your current Dockerfile workloads to use Chainguard Images.

A general migration process would involve the following steps:

1. **Identify the base image you need**. Look at the [reference documentation](/chainguard/chainguard-images/reference) to identify the image that is the closest match to what you currently use. You may also use [wolfi-base](https://edu.chainguard.dev/chainguard/chainguard-images/reference/wolfi-base) as a flexible starting point for your experimentation.
2. **Try the `-dev` variant of the image first.** Chainguard Images typically have a **distroless** variant, which is very minimal and doesn't include `apk`, and a **dev** variant that contains tooling necessary to build applications and install new packages. Start with the **dev** variant or the **wolfi-base** image to have more room for customization.
3. **Identify packages you need to install**. Depending on your current base image, you may need to include additional packages to meet dependencies. Refer to the [Searching for Packages](#searching-for-packages) section for more details on how to find packages.
4. **Migrate to a distroless image**. Evaluate the option of using a Docker multi-stage build to create a final distroless image containing only what you need. Check the [Getting Started with Distroless images](/chainguard/chainguard-images/getting-started-distroless/) for more details of how to work with distroless images. Although not required, this process should give you a smaller image with additional safeguards.

There are some differences in Wolfi's `busybox` and `coreutils` packages when compared to their counterparts in distros such as Debian or even Alpine. Some binaries and scripts are not included by default, which contributes to a smaller package size. Commands might still be available through separate packages, in order to keep images to a minimum.

The next sections of this page contain distro-specific information that should help you streamline the migration process from your current base images to Chainguard images.


## Migrating from Debian and Ubuntu Dockerfiles
Chainguard Images are based on the [Alpine apk](https://wiki.alpinelinux.org/wiki/Package_management) ecosystem, which differs from Debian-based `apt` in several aspects. Some of these features contribute in making packages smaller and more accountable, resulting in smaller images with traceable provenance information based on cryptographic signatures. The page [Why apk](https://edu.chainguard.dev/open-source/wolfi/apk-package-manager/) from the official Wolfi documentation explains in more detail why we use apk.

If you are coming from a Debian-based Dockerfile, you'll need to adapt some of your commands to be compatible with the apk ecosystem:

| Command Description          | Debian-based Dockerfile | Wolfi-based Equivalent |
|------------------------------|-------------------------|------------------------|
| Install a package            | `apt install`           | `apk add`              |
| Remove a package             | `apt remove`            | `apk del`              |
| Update package manager cache | `apt update`            | `apk update`           |

Our [Debian Compatibility](https://edu.chainguard.dev/chainguard/migration-guides/debian-compatibility/) page has a table listing common tools and their corresponding package(s) in both Wolfi and Debian distributions. For Ubuntu-based Dockerfiles, check our [Ubuntu Compatibility](https://edu.chainguard.dev/chainguard/migration-guides/ubuntu-compatibility/) page.

## Migrating from Red Hat UBI Dockerfiles
If you are coming from a Red Hat UBI (Universal Base Image) Dockerfile, you'll also need to adapt some of your commands to be compatible with the apk ecosystem. Wolfi uses BusyBox utilities, which offer a smaller footprint compared to GNU coreutils in Red Hat images. Our [Red Hat Compatibility](https://edu.chainguard.dev/chainguard/migration-guides/debian-compatibility/) page has a table listing common tools and their corresponding package(s) in both Wolfi and Red Hat distributions.

If you are coming from a Red Hat UBI based Dockerfile, you'll need to adapt some of your commands to be compatible with the apk ecosystem:

| Command Description          | Red Hat UBI Dockerfile | Wolfi-based Equivalent |
|------------------------------|------------------------|------------------------|
| Install a package            | yum install            | apk add                |
| Remove a package             | yum remove             | apk del                |
| Update package manager cache | yum makecache          | apk update             |

## Migrating from Alpine Dockerfiles
If your Dockerfile is based on Alpine, the process for migrating to Chainguard Images should be more straightforward, since you're already using `apk` commands. Wolfi packages typically match what is available in Alpine, with some exceptions. For instance, the Wolfi busybox package is slimmer and doesn't include all tools available in Alpine's busybox. Check the [Alpine Compatibility](https://edu.chainguard.dev/chainguard/migration-guides/alpine-compatibility/) page for a list of common tools and their corresponding packages in Wolfi and Alpine.

## Searching for Packages
Packages from Debian and other base distributions might have a different name in Wolfi. To search for packages, log into an ephemeral container based on `cgr.dev/chainguard/wolfi-base`:

```shell
docker run -it --rm --entrypoint /bin/sh cgr.dev/chainguard/wolfi-base
```

Then, run `apk update` to update the local apk cache with latest Wolfi packages:

```shell
# apk update
fetch https://packages.wolfi.dev/os/x86_64/APKINDEX.tar.gz
[https://packages.wolfi.dev/os]
OK: 46985 distinct packages available
```
Now you can use `apk search` to look for packages. The following example searches for PHP 8.2 XML extensions:

```shell
# apk search php*8.2*xml*
```
You should get output similar to this:

```shell
php-8.2-simplexml-8.2.17-r0
php-8.2-simplexml-config-8.2.17-r0
php-8.2-xml-8.2.17-r0
php-8.2-xml-config-8.2.17-r0
php-8.2-xmlreader-8.2.17-r0
php-8.2-xmlreader-config-8.2.17-r0
php-8.2-xmlwriter-8.2.17-r0
php-8.2-xmlwriter-config-8.2.17-r0
php-simplexml-8.2.11-r1
php-xml-8.2.11-r1
php-xmlreader-8.2.11-r1
php-xmlwriter-8.2.11-r1
```

To search in which package you can find a command, you can use the syntax `apk search cmd:command-name`. For instance, if you want to discover which package has the command `useradd`, you can use:

```shell
# apk search cmd:useradd
```
You'll get output indicating that the `shadow` package has the command you are looking for.
```shell
shadow-4.15.1-r0
```
Use `apk --help` for more options when searching for packages.

### If you Can't find a Package

If your build requires dependencies that are not yet available in Wolfi, you can compile them from source using the `wolfi-base` image, or build your own apks using [melange](/open-source/melange/overview/). Check the [Getting started with melange](/open-source/melange/tutorials/getting-started-with-melange/) guide for more details on how to go about that.
