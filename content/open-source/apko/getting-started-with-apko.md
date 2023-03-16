---
title: "Getting Started with apko"
type: "article"
lead: "Minimalist OCI image builder based on APK"
description: "Quickstart to get apko up and running"
date: 2022-07-06T08:49:31+00:00
lastmod: 2023-03-15T16:49:31+00:00
contributors: ["Erika Heidi"]
draft: false
tags: ["apko", "Procedural",]
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

In this guide, we'll learn how to use apko to build a base [Wolfi](https://edu.chainguard.dev/open-source/wolfi/overview/) image.

## Requirements

The fastest way to get apko up and running on your system is by using the [official apko image](/chainguard/chainguard-images/reference/apko/overview/) with Docker. This method is compatible with all operating systems that support Docker and shared volumes. Please follow the [appropriate Docker installation instructions](https://docs.docker.com/get-docker/) for your operating system.

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

GitVersion:    v0.6.0
...
```

In the next step, you'll build your first apko image.


## Step 2 — Build a Test Image

To test that you're able to build images, you can use one of the example `yaml` definition files that are included in the [official apko code repository](https://github.com/chainguard-dev/apko/tree/main/examples). Here we'll use the `wolfi-base.yaml` for demonstration.

Create a new folder to save your image files, them move to that directory:

```shell
mkdir ~/apko
cd ~/apko
```

Next, create a file named `wolfi-base.yaml` to save your image definition. You can use `nano` for that:

```shell
nano wolfi-base.yaml
```

The `wolfi-base.yaml` example image is defined as follows:

```yaml
contents:
  keyring:
    - https://packages.wolfi.dev/os/wolfi-signing.rsa.pub
  repositories:
    - https://packages.wolfi.dev/os
  packages:
    - ca-certificates-bundle
    - wolfi-base

entrypoint:
  command: /bin/sh -l

archs:
  - x86_64
```

The `contents` node is used to define allowed package sources and which packages should be included in the image. Here we'll be using only packages from the main Wolfi APK repository. In the `packages` section, we require the [wolfi-base](https://github.com/wolfi-dev/os/blob/main/wolfi-base.yaml) package, which is a meta-package to set up a bare minimum Wolfi system.

The `cmd` node defines the image entry point command `/bin/sh -l`, which will land you in a shell prompt whenever the image is executed. Finally, the `environment` node sets up the $PATH variable that defines binary directories within the guest system, allowing for simpler command execution paths.

Save and close the file after you're done including these contents. With `nano`, you can do that by pressing `CTRL+X`, then confirming with `Y` and `ENTER`.

The only thing left to do now is run apko to build this image. The following build command will:

- set up a volume share in the current directory, synchronizing its contents with apko's image workdir; this way, the generated artifacts will be available on your host system.
- execute the `cgr.dev/chainguard/apko` image with the `build` command, tagging the image as `wolfi-base:test-amd64` and saving the build as `wolfi-test.tar`.

```shell
docker run --rm -v ${PWD}:/work -w /work cgr.dev/chainguard/apko build wolfi-base.yaml wolfi-base:test wolfi-test.tar
```

You should get output similar to this:

```
. . .
Mar 15 20:17:02.023 [INFO] [arch:x86_64] Building images for 1 architectures: [amd64]
Mar 15 20:17:02.023 [INFO] [arch:x86_64] building tags [wolfi-base:test]
. . .
Mar 15 20:17:04.261 [INFO] loading config file: wolfi-base.yaml
Mar 15 20:17:04.416 [INFO] [arch:x86_64] adding amd64 to index
Mar 15 20:17:04.419 [INFO] [arch:x86_64] Generating index SBOM
Mar 15 20:17:04.420 [INFO] [arch:x86_64] Final index tgz at: wolfi-test.tar
```

From the output, you can notice that the image was successfully built as `wolfi-test.tar` in the container, which is shared with your local folder on the host thanks to the volume you created when running the `docker run` command.

## Step 3 — Test the Image with Docker

To test the generated image with Docker, you'll need to use the `docker load` command and import the `.tar` file you created in the previous step:

```shell
docker load <  wolfi-test.tar
```
You'll get output like this:
```
bf6e72d71c13: Loading layer [==================================================>]  5.491MB/5.491MB
Loaded image: wolfi-base:test-amd64
```

You can check that the image is available at the host system with:

```shell
docker image list
```

You should be able to find the `wolfi-base` image with the `test-amd64` tag among the results.

Now you can run the image with:

```shell
docker run -it wolfi-base:test-amd64
```

This will get you into a container running the apko-built image `wolfi-base:test-amd64`. It's a regular shell that you can explore to see what's included - just keep in mind that this is a minimalist image with only the base Wolfi system. To include additional software packages, check the [Wolfi repository](https://github.com/wolfi-dev/os) to find the packages you'll need for your specific use case, or check out [melange](/open-source/melange/), apko's companion project that allows users to build their own APK packages from source.

## Conclusion

In this guide, you learned what apko is and what makes it a powerful resource in your cloud-native tooling.

If you need help debugging your build, check our [Troubleshooting apko](/open-source/apko/troubleshooting/) page for more information.
Check the [official apko repository](https://github.com/chainguard-dev/apko/) if you want to report an issue or suggest new features.

