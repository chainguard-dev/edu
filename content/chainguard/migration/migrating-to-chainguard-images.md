---
title: "Migrating Dockerfiles to Chainguard Containers"
linktitle: "Migrating Dockerfiles"
aliases:
- /chainguard/migration-guides/migrating-to-chainguard-images/
- /chainguard/migration/migrating-to-chainguard-images/
type: "article"
description: "Guidance on how to migrate existing Dockerfile workloads to use Chainguard Containers"
date: 2024-03-25T15:56:52-07:00
lastmod: 2024-03-25T15:56:52-07:00
draft: false
tags: ["Chainguard Containers", "Product",]
images: []
weight: 015
toc: true
---

Based on the [Wolfi](/open-source/wolfi/overview/) Linux _undistro_, Chainguard Containers have special features designed for increased security and provenance attestation. Depending on your current base image and custom commands, you may need to make some adjustments when migrating your current Dockerfile workloads to use Chainguard Containers.

A general migration process would involve the following steps:

1. **Identify the base image you need**. Check out the [Chainguard Containers Directory](https://images.chainguard.dev/directory?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-migration-migrating-to-chainguard-images) to identify the image that is the closest match to what you currently use. You may also use [wolfi-base](https://images.chainguard.dev/directory/image/wolfi-base/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-migration-migrating-to-chainguard-images) as a flexible starting point for your experimentation.
2. **Try the `-dev` variant of the image first.** Chainguard Containers typically have a **distroless** variant, which is very minimal and doesn't include `apk`, and a **dev** variant that contains tooling necessary to build applications and install new packages. Start with the **dev** variant or the **wolfi-base** image to have more room for customization.
3. **Identify packages you need to install**. Depending on your current base image, you may need to include additional packages to meet dependencies. Refer to the [Searching for Packages](#searching-for-packages) section for more details on how to find packages.
4. **Migrate to a distroless image**. Evaluate the option of using a Docker multi-stage build to create a final distroless image containing only what you need. Check the [Getting Started with Distroless images](/chainguard/chainguard-images/getting-started-distroless/) for more details of how to work with distroless images. Although not required, this process should give you a smaller image with additional safeguards.

There are some differences in Wolfi's `busybox` and `coreutils` packages when compared to their counterparts in distros such as Debian or even Alpine. Some binaries and scripts are not included by default, which contributes to a smaller package size. This was done in order to keep images to a minimum, but be aware that some commands might still be available through separate packages.

The next sections of this page contain distro-specific information that should help you streamline the migration process from your current base images to Chainguard images.


## Migrating from Debian and Ubuntu Dockerfiles
Chainguard Containers are based on the [Alpine apk](https://wiki.alpinelinux.org/wiki/Package_management) ecosystem, which differs from Debian-based `apt` in several aspects. Some of these features contribute in making packages smaller and more accountable, resulting in smaller images with traceable provenance information based on cryptographic signatures. The page [Why apk](/open-source/wolfi/apk-package-manager/) from the official Wolfi documentation explains in more detail why we use apk.

If you are coming from a Debian-based Dockerfile, you'll need to adapt some of your commands to be compatible with the apk ecosystem:

| Command Description          | Debian-based Dockerfile | Wolfi-based Equivalent |
|------------------------------|-------------------------|------------------------|
| Install a package            | `apt install`           | `apk add`              |
| Remove a package             | `apt remove`            | `apk del`              |
| Update package manager cache | `apt update`            | `apk update`           |

Our [Debian Compatibility](/chainguard/migration/debian-compatibility/) page has a table listing common tools and their corresponding package(s) in both Wolfi and Debian distributions. For Ubuntu-based Dockerfiles, check our [Ubuntu Compatibility](/chainguard/migration/ubuntu-compatibility/) page.

## Migrating from Red Hat UBI Dockerfiles
If you are coming from a Red Hat UBI (Universal Base Image) Dockerfile, you'll also need to adapt some of your commands to be compatible with the apk ecosystem. Wolfi uses BusyBox utilities, which offer a smaller footprint compared to GNU coreutils in Red Hat images. Our [Red Hat Compatibility](/chainguard/migration/red-hat-compatibility/) page has a table listing common tools and their corresponding package(s) in both Wolfi and Red Hat distributions.

If you are coming from a Red Hat UBI based Dockerfile, you'll need to adapt some of your commands to be compatible with the apk ecosystem:

| Command Description          | Red Hat UBI Dockerfile | Wolfi-based Equivalent |
|------------------------------|------------------------|------------------------|
| Install a package            | `yum install`          | `apk add`              |
| Remove a package             | `yum remove`           | `apk del`              |
| Update package manager cache | `yum makecache`        | `apk update`           |

## Migrating from Alpine Dockerfiles
If your Dockerfile is based on Alpine, the process for migrating to Chainguard Containers should be more straightforward, since you're already using `apk` commands. Wolfi packages typically match what is available in Alpine, with some exceptions. For instance, the Wolfi busybox package is slimmer and doesn't include all tools available in Alpine's busybox. Check the [Alpine Compatibility](/chainguard/migration/alpine-compatibility/) page for a list of common tools and their corresponding packages in Wolfi and Alpine.

Be aware that binaries are not compatible between Alpine and Wolfi. You **should not** attempt to copy Alipne binaries into a Wolfi-based container image.

## Searching for Packages
Packages from Debian and other base distributions might have a different name in Wolfi. To search for packages, log into an ephemeral container based on `cgr.dev/chainguard/wolfi-base`:

```shell
docker run -it --rm --entrypoint /bin/sh cgr.dev/chainguard/wolfi-base
```

Then, run `apk update` to update the local apk cache with latest Wolfi packages:

```shell
apk update
```

You'll get output similar to this:

```
fetch https://packages.wolfi.dev/os/x86_64/APKINDEX.tar.gz
[https://packages.wolfi.dev/os]
OK: 46985 distinct packages available
```

Now you can use `apk search` to look for packages. The following example searches for PHP 8.2 XML extensions:

```shell
apk search php*8.2*xml*
```
You should get output similar to this:

```
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

### Searching which package has a command
To search in which package you can find a command, you can use the syntax `apk search cmd:command-name`. For instance, if you want to discover which package has the command `useradd`, you can use:

```shell
apk search cmd:useradd
```
You'll get output indicating that the `shadow` package has the command you are looking for.

```
shadow-4.15.1-r0
```

### Searching for package dependencies
To check for package dependencies, you can use the syntax `apk search -R info package-name`. For example, to search which packages are listed as dependencies for the `shadow` package that we've seen in the previous section, you can run:

```shell
apk -R info shadow
```
And this will give you a list of dependencies for each version of the `shadow` package currently available:

```
...
shadow-4.15.1-r0 depends on:
so:ld-linux-x86-64.so.2
so:libbsd.so.0
so:libc.so.6
so:libcrypt.so.1
so:libpam.so.0
so:libpam_misc.so.0
```

### Searching for packages that include a shared object
To search which packages include a shared object, you can use the syntax `apk search so:shared-library`. As an example, if you want to check which packages include the `libxml2` shared library, you can run something like:

```shell
apk search so:libxml2.so*
```
And this should give you output indicating that this shared object is included within the `libxml2-2.12.6-r0` package.

For detailed information about apk options and flags when searching for packages, check the [official documentation](https://docs.alpinelinux.org/user-handbook/0.1a/Working/apk.html#_searching_for_packages).

## Resources to Learn More

Our [Getting Started Guides](/chainguard/chainguard-images/getting-started/) have detailed examples for different language ecosystems and stacks. Make sure to also check image-specific information in our [Chainguard Containers Directory](https://images.chainguard.dev/directory?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-migration-migrating-to-chainguard-images).

If you can't find an image that is a good match for your use case, or if your build has dependencies that cannot be met with the regular catalog, [get in touch with us](https://www.chainguard.dev/contact?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement) for alternative options.
