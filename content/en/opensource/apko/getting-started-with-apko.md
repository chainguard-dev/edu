---
title: "Getting Started with apko"
type: "article"
description: "One-pager quickstart to get apko up and running"
lead: "Minimalist OCI image builder based on APK"
date: 2021-07-06T08:49:31+00:00
lastmod: 2021-07-06T08:49:31+00:00
draft: false
images: []
menu:
docs:
parent: "apko"
weight: 630
toc: true
---

[apko](http://github.com/chainguard-dev/apko) is a command-line tool that allows users to build images that are compatible with the [OCI](https://opencontainers.org/) (Open Container Initiative) standard, using a declarative language based on YAML files. The name _apko_ references APK, the [Alpine Package Manager](https://wiki.alpinelinux.org/wiki/Package_management), since this is the package management system used by apko to build container images.

## Why apko
Using a declarative language to build container images has many advantages when compared to traditional Dockerfiles. Generally speaking, YAML definitions are easier to parse through and understand. This methodology facilitates automation and removes noise from image definitions, allowing users to "do more" with fewer lines of configuration.

In addition to that, apko builds are fully reproducible and automatically generate [SBOM](https://www.cisa.gov/sbom) files for every image built, which adds a new layer of security to your container images. apko images are also smaller and faster to build than traditional Dockerfile-based images.

It's worth noting that apko images are fully compatible with Docker.

## Requirements

The fastest way to get apko up and running on your system is by using the [official apko image](https://github.com/distroless/apko) with Docker. This method is compatible with all operating systems that support Docker and shared volumes. Please follow the [appropriate Docker installation instructions](https://docs.docker.com/get-docker/) for your operating system.

If you want to run apko on CI/CD pipelines built on top of GitHub Actions, check the [apko action]() repository.

The instructions in this document were validated on an Ubuntu 22.04 workstation running Docker 20.10.

## Step 1 — Download the apko Image

Start by pulling the official apko image into your local system:

```shell
docker pull distroless.dev/apko
```

This will download the latest version of the distroless apko image, which is rebuilt every night for extra freshness.

Check that you're able to run apko with:

```shell
docker run --rm distroless.dev/apko version
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

- set up an environment variable to define the $APKO_HOME directory;
- set up a volume share in the current directory;
- execute the `distroless.dev/apko` image with the `build` command.

```shell
export APKO_HOME=/home/nonroot
docker run --rm -v ${PWD}:${APKO_HOME} distroless.dev/apko build ${APKO_HOME}/alpine-base.yaml alpine-base:test ${APKO_HOME}/alpine-test.tar
```

You should get output similar to this:

```
Jul 20 17:20:34.187 [INFO] loading config file: /home/nonroot/alpine-base.yaml
Jul 20 17:20:34.188 [INFO] [arch:x86_64] building image 'alpine-base:test'
Jul 20 17:20:34.188 [INFO] [arch:x86_64] build context:
Jul 20 17:20:34.188 [INFO] [arch:x86_64]   working directory: /tmp/apko-3822091344
Jul 20 17:20:34.188 [INFO] [arch:x86_64]   tarball path:
Jul 20 17:20:34.188 [INFO] [arch:x86_64]   use proot: false
Jul 20 17:20:34.188 [INFO] [arch:x86_64]   source date: 1970-01-01 00:00:00 +0000 UTC
Jul 20 17:20:34.188 [INFO] [arch:x86_64]   Docker mediatypes: false
Jul 20 17:20:34.188 [INFO] [arch:x86_64]   SBOM output path: /home/nonroot
Jul 20 17:20:34.188 [INFO] [arch:x86_64]   arch: x86_64
Jul 20 17:20:34.188 [INFO] [arch:x86_64] image configuration:
Jul 20 17:20:34.188 [INFO] [arch:x86_64]   contents:
Jul 20 17:20:34.188 [INFO] [arch:x86_64]     repositories: [https://dl-cdn.alpinelinux.org/alpine/edge/main]
Jul 20 17:20:34.188 [INFO] [arch:x86_64]     keyring:      []
Jul 20 17:20:34.188 [INFO] [arch:x86_64]     packages:     [alpine-base]
Jul 20 17:20:34.188 [INFO] [arch:x86_64]   cmd: /bin/sh -l
Jul 20 17:20:34.188 [INFO] [arch:x86_64] doing pre-flight checks
Jul 20 17:20:34.188 [INFO] [arch:x86_64] building image fileystem in /tmp/apko-3822091344
Jul 20 17:20:34.188 [INFO] [arch:x86_64] initializing apk database
Jul 20 17:20:34.189 [INFO] [arch:x86_64] [cmd:apk] [use-proot:false] [use-qemu:] running: /sbin/apk add --initdb --arch x86_64 --root /tmp/apko-3822091344
Jul 20 17:20:34.266 [INFO] [arch:x86_64] initializing apk world
Jul 20 17:20:34.266 [INFO] [arch:x86_64] initializing apk repositories
Jul 20 17:20:34.267 [INFO] [arch:x86_64] initializing apk keyring
Jul 20 17:20:34.272 [INFO] [arch:x86_64] synchronizing with desired apk world
Jul 20 17:20:34.272 [INFO] [arch:x86_64] [cmd:apk] [use-proot:false] [use-qemu:] running: /sbin/apk fix --root /tmp/apko-3822091344 --no-scripts --no-cache --update-cache --arch x86_64
Jul 20 17:20:35.368 [INFO] [arch:x86_64] [cmd:/bin/busybox] [use-proot:false] [use-qemu:] running: /usr/sbin/chroot /tmp/apko-3822091344 /bin/busybox --install -s
Jul 20 17:20:35.389 [INFO] [arch:x86_64] generating supervision tree
Jul 20 17:20:35.389 [INFO] [arch:x86_64] finished building filesystem in /tmp/apko-3822091344
Jul 20 17:20:35.460 [INFO] [arch:x86_64] built image layer tarball as /tmp/apko-temp-2106040545/apko-x86_64.tar.gz
Jul 20 17:20:35.529 [INFO] [arch:x86_64] building OCI image from layer '/tmp/apko-temp-2106040545/apko-x86_64.tar.gz'
Jul 20 17:20:35.594 [INFO] [arch:x86_64] OCI layer digest: sha256:0502d32aa47200dd383c0c58c11431e66217642390fbee0aaef535e137c9c5f3
Jul 20 17:20:35.594 [INFO] [arch:x86_64] OCI layer diffID: sha256:4d1fb8cd56aa943f93c34a8506a7a090b5a8e3b1c4d1feb22ba189ab2c3d7bd1
Jul 20 17:20:35.595 [WARNING] [arch:x86_64] multiple SBOM formats requested, uploading SBOM with media type: spdx+json
Jul 20 17:20:35.597 [INFO] [arch:x86_64] output OCI image file to /home/nonroot/alpine-test.tar
```

From the output, you can notice that the image was successfully built at the location `/home/nonroot/alpine-test.tar` in the container, which is shared with your local folder on the host thanks to the volume you created when running the `docker exec` command. Because tagging happens inside the container, before using this image you'll need to load the generated `tar` image artifact into Docker with the `docker load` command, on the host machine (your main system).

To load the tar file into a Docker image, run:

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

This will get you into a container running the apko-built image `alpine-base:test`. It's a regular shell that you can explore to learn what's included - just keep in mind that this is a minimalist image with only the base Alpine system. To include additional software packages, check the [Alpine APK repositories](https://pkgs.alpinelinux.org/packages) to find the packages you'll need for your specific use case, or check out [melange](), apko's companion project that allows users to build their own APK packages from source.

## Conclusion

In this guide, you learned what apko is and what makes it a powerful resource in your cloud-native tooling. For more information, troubleshooting, and feedback about apko's features, please refer to the [official apko repository](https://github.com/chainguard-dev/apko/).

