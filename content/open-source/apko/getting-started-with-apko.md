---
title: "Getting Started with apko"
type: "article"
lead: "Minimalist OCI image builder based on APK"
description: "Quickstart to get apko up and running"
date: 2022-07-06T08:49:31+00:00
lastmod: 2022-07-06T08:49:31+00:00
contributors: ["Erika Heidi"]
draft: false
images: []
menu:
  docs:
    parent: "apko"
weight: 100
terminalImage: academy/apko:latest
toc: true
---

[apko](http://github.com/chainguard-dev/apko) is a command-line tool that allows users to build container images using a declarative language based on YAML. apko is so named as it uses the [apk](https://wiki.alpinelinux.org/wiki/Package_management) package format and is inspired by the [ko](https://github.com/google/ko) build tool.

## Why apko
Container images are typically assembled in multiple steps. A tool like Docker, for example, combines building steps (as in, running commands to copy files, build and deploy applications) and composition (as in, composing a base image with pre-built packages) in a single piece of software. apko, on the other hand, is solely a **composition** tool that focuses on producing lightweight, "flat" base images that are fully reproducible and contain auto generated [SBOM](https://www.cisa.gov/sbom) files for every successful build.

Instead of building your application together with your components and system dependencies, you can build your application once and compose it into different architectures and distributions, using a tool such as [melange](https://github.com/chainguard-dev/melange) in combination with apko. For more information on how melange and apko work together, you can check this blog post: [Secure your Software Factory with melange and apko](https://blog.chainguard.dev/secure-your-software-factory-with-melange-and-apko/).

In this guide, we'll learn how to use apko to build a base Alpine image.

## Requirements

The fastest way to get apko up and running on your system is by using the [official apko image](https://github.com/distroless/apko) with Docker. This method is compatible with all operating systems that support Docker and shared volumes. Please follow the [appropriate Docker installation instructions](https://docs.docker.com/get-docker/) for your operating system.

If you want to run apko on CI/CD pipelines built on top of GitHub Actions, check the [apko build action](https://github.com/chainguard-images/actions/tree/main/apko-build) on GitHub.

The instructions in this document were validated on an Ubuntu 22.04 workstation running Docker 20.10.

## Step 1 — Download the apko Image

Start by pulling the official apko image into your local system:

```shell
docker pull cgr.dev/chainguard/apko
```

This will download the latest version of the distroless apko image, which is rebuilt every night for extra freshness.

Check that you're able to run apko with:

```shell
docker run --rm cgr.dev/chainguard/apko version
```

You should get output similar to this:

```
     _      ____    _  __   ___
    / \    |  _ \  | |/ /  / _ \
   / _ \   | |_) | | ' /  | | | |
  / ___ \  |  __/  | . \  | |_| |
 /_/   \_\ |_|     |_|\_\  \___/
apko

GitVersion:    v0.5.0
GitCommit:     71cdb2460aece396d00dd4ea47d7d7b5eab3a37d
GitTreeState:  clean
BuildDate:     2022-07-18T16:59:54
GoVersion:     go1.18.3
Compiler:      gc
Platform:      linux/amd64
```

In the next step, you'll build your first apko image.


## Step 2 — Build a Test Image

To test that you're able to build images, you can use one of the example `yaml` definition files that are included in the [official apko code repository](https://github.com/chainguard-dev/apko/tree/main/examples). Here we'll use the `alpine-base.yaml` for demonstration.

Create a new folder to save your image files, them move to that directory:

```shell
mkdir ~/apko
cd ~/apko
```

Next, create a file named `alpine-base.yaml` to save your image definition. You can use `nano` for that:

```shell
nano alpine-base.yaml
```

The `alpine-base.yaml` example image is defined as follows:

```yaml
contents:
  repositories:
    - https://dl-cdn.alpinelinux.org/alpine/edge/main
  packages:
    - alpine-base

cmd: /bin/sh -l

# optional environment configuration
environment:
  PATH: /usr/sbin:/sbin:/usr/bin:/bin

```

The `contents` node is used to define allowed package sources and which packages should be included in the image. Here we'll be using only packages from the main Alpine APK repository. In the `packages` section, we have a single requirement: the [alpine-base](https://pkgs.alpinelinux.org/package/edge/main/x86/alpine-base) package, which is a meta-package to set up a bare minimum alpine system.

The `cmd` node defines the image entry point command `/bin/sh -l`, which will land you in a shell prompt whenever the image is executed. Finally, the `environment` node sets up the $PATH variable that defines binary directories within the guest system, allowing for simpler command execution paths.

Save and close the file after you're done including these contents. With `nano`, you can do that by pressing `CTRL+X`, then confirming with `Y` and `ENTER`.

The only thing left to do now is run apko to build this image. The following build command will:

- set up a volume share in the current directory, synchronizing its contents with apko's image workdir; this way, the generated artifacts will be available on your host system.
- execute the `cgr.dev/chainguard/apko` image with the `build` command, tagging the image as `alpine-base:test` and saving the build as `alpine-test.rar`.

```shell
docker run --rm -v ${PWD}:/work -w /work cgr.dev/chainguard/apko build alpine-base.yaml alpine-base:test alpine-test.tar
```

You should get output similar to this:

```
Jul 25 17:14:52.623 [INFO] loading config file: alpine-base.yaml
Jul 25 17:14:52.625 [INFO] [arch:x86_64] building image 'alpine-base:test'
Jul 25 17:14:52.625 [INFO] [arch:x86_64] build context:
Jul 25 17:14:52.625 [INFO] [arch:x86_64]   working directory: /tmp/apko-912607687
Jul 25 17:14:52.625 [INFO] [arch:x86_64]   tarball path:
Jul 25 17:14:52.625 [INFO] [arch:x86_64]   use proot: false
Jul 25 17:14:52.625 [INFO] [arch:x86_64]   source date: 1970-01-01 00:00:00 +0000 UTC
Jul 25 17:14:52.625 [INFO] [arch:x86_64]   Docker mediatypes: false
Jul 25 17:14:52.625 [INFO] [arch:x86_64]   SBOM output path: /work
Jul 25 17:14:52.625 [INFO] [arch:x86_64]   arch: x86_64
Jul 25 17:14:52.625 [INFO] [arch:x86_64] image configuration:
Jul 25 17:14:52.625 [INFO] [arch:x86_64]   contents:
Jul 25 17:14:52.625 [INFO] [arch:x86_64]     repositories: [https://dl-cdn.alpinelinux.org/alpine/edge/main]
Jul 25 17:14:52.625 [INFO] [arch:x86_64]     keyring:      []
Jul 25 17:14:52.625 [INFO] [arch:x86_64]     packages:     [alpine-base]
Jul 25 17:14:52.625 [INFO] [arch:x86_64]   cmd: /bin/sh -l
Jul 25 17:14:52.625 [INFO] [arch:x86_64] doing pre-flight checks
Jul 25 17:14:52.625 [INFO] [arch:x86_64] building image fileystem in /tmp/apko-912607687
Jul 25 17:14:52.625 [INFO] [arch:x86_64] initializing apk database
Jul 25 17:14:52.626 [INFO] [arch:x86_64] [cmd:apk] [use-proot:false] [use-qemu:] running: /sbin/apk add --initdb --arch x86_64 --root /tmp/apko-912607687
Jul 25 17:14:52.732 [INFO] [arch:x86_64] initializing apk repositories
Jul 25 17:14:52.732 [INFO] [arch:x86_64] initializing apk world
Jul 25 17:14:52.732 [INFO] [arch:x86_64] initializing apk keyring
Jul 25 17:14:52.739 [INFO] [arch:x86_64] synchronizing with desired apk world
Jul 25 17:14:52.739 [INFO] [arch:x86_64] [cmd:apk] [use-proot:false] [use-qemu:] running: /sbin/apk fix --root /tmp/apko-912607687 --no-scripts --no-cache --update-cache --arch x86_64
Jul 25 17:14:53.707 [INFO] [arch:x86_64] [cmd:/bin/busybox] [use-proot:false] [use-qemu:] running: /usr/sbin/chroot /tmp/apko-912607687 /bin/busybox --install -s
Jul 25 17:14:53.737 [INFO] [arch:x86_64] generating supervision tree
Jul 25 17:14:53.737 [INFO] [arch:x86_64] finished building filesystem in /tmp/apko-912607687
Jul 25 17:14:53.837 [INFO] [arch:x86_64] built image layer tarball as /tmp/apko-temp-1954328382/apko-x86_64.tar.gz
Jul 25 17:14:53.913 [INFO] [arch:x86_64] building OCI image from layer '/tmp/apko-temp-1954328382/apko-x86_64.tar.gz'
Jul 25 17:14:53.981 [INFO] [arch:x86_64] OCI layer digest: sha256:d1354df643e7c9ad2e88ec505bf9566f8034038affafd7f119a4e269d1803d68
Jul 25 17:14:53.981 [INFO] [arch:x86_64] OCI layer diffID: sha256:d34e58ab1ef2c3d4aff216116728afb18183fb4d6d4abe9a31ff83049a739524
Jul 25 17:14:53.982 [WARNING] [arch:x86_64] multiple SBOM formats requested, uploading SBOM with media type: spdx+json
Jul 25 17:14:53.984 [INFO] [arch:x86_64] output OCI image file to alpine-test.tar
```

From the output, you can notice that the image was successfully built at the location `/work/alpine-test.tar` in the container, which is shared with your local folder on the host thanks to the volume you created when running the `docker run` command.

## Step 3 — Test the Image with Docker

To test the generated image with Docker, you'll need to use the `docker load` command and import the `.tar` file you created in the previous step:

```shell
docker load <  alpine-test.tar
```
You'll get output like this:
```
4d1fb8cd56aa: Loading layer  3.242MB/3.242MB
Loaded image: alpine-base:test
```

You can check that the image is available at the host system with:

```shell
docker image list
```

You should be able to find the `alpine-base` image with the `test` tag among the results.

Now you can run the image with:

```shell
docker run -it alpine-base:test
```

This will get you into a container running the apko-built image `alpine-base:test`. It's a regular shell that you can explore to see what's included - just keep in mind that this is a minimalist image with only the base Alpine system. To include additional software packages, check the [Alpine APK repositories](https://pkgs.alpinelinux.org/packages) to find the packages you'll need for your specific use case, or check out [melange](), apko's companion project that allows users to build their own APK packages from source.

## Conclusion

In this guide, you learned what apko is and what makes it a powerful resource in your cloud-native tooling. For more information, troubleshooting, and feedback about apko's features, please refer to the [official apko repository](https://github.com/chainguard-dev/apko/).

