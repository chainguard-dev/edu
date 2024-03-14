---
title: "How to Use Chainguard Images"
linktitle: "How to Use"
type: "article"
description: "A primer on how to migrate to Chainguard Images"
lead: "A primer on how to migrate to Chainguard Images"
date: 2022-09-01T08:49:31+00:00
lastmod: 2023-01-23T19:42:31+00:00
draft: false
tags: ["Chainguard Images", "Procedural", "Product"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 020
terminalImage: academy/chainguard-images:latest
toc: true
---

[Chainguard Images](https://www.chainguard.dev/chainguard-images?utm_source=docs) are distroless images based on [Wolfi](/open-source/wolfi/overview/), our Linux _undistro_. You can have a look at [Chainguard Image's GitHub org](https://github.com/chainguard-images) in order to find out which images are already available for general usage.

Each image has its own usage instructions, which is detailed in their READMEs. All images are hosted on the `cgr.dev` registry.

In this guide, you'll learn how to get started using Chainguard Images and how to migrate existing container-based workflows to use our images.

## Quickstart: Using Chainguard Images

To get up and running with Chainguard Images, you can use `docker` commands to pull and run images. For each specific image, you'll find this guidance on its overview page (for example, see [Node](/chainguard/chainguard-images/reference/node/overview/), [Python](/chainguard/chainguard-images/reference/python/overview/), or [NGINX](/chainguard/chainguard-images/reference/nginx/overview/)).

### Pulling a Chainguard Image

You can pull a Chainguard Image with the `docker pull` command. For example, to pull down the Git Chainguard Image, you can run the following.

```sh
docker pull cgr.dev/chainguard/git
```

Without passing a tag or a digest, the reference to the Git image will pull down the default tag, which is `:latest`.

Note that if you have your own registry, you'll need to change the `cgr.dev/chainguard` path to your own registry path.

### Pulling by Tag

You can also add a relevant tag that you have access to. In the case of the Git image, you can pull the `:latest-glibc` tag for the Git image. [Note that not all tags are available for public images](/chainguard/chainguard-images/faq/#do-i-need-to-authenticate-into-chainguard-to-use-chainguard-images).

```sh
docker pull cgr.dev/chainguard/git:latest-glibc
```

You may use tags to pull a specific version of a software like Git, or programming language version in a catalog you have access to. Chainguard Academy has tag history pages for each image, which you can find in our reference docs. For example, the [Git Image Tags History](/chainguard/chainguard-images/reference/git/tags_history/), [PHP Image Tags History](/chainguard/chainguard-images/reference/php/tags_history/), and [JDK Image Tags History](/chainguard/chainguard-images/reference/jdk/tags_history/).

You can learn about the Chainguard Images tags history in our guide about [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/).

### Pulling by Digest

Pulling a Chainguard Image by its digest guarantees reproducibility, as it will ensure that you are using the same image each time (versus the tag that may receive updates).

To pull an image by its digest, you can do so by appending the digest which begins with `sha256`. You can find these on our reference tags history pages.

In our Git example, we can review the [Git Image Tags History](/chainguard/chainguard-images/reference/git/tags_history/) page and choose a relevant digest. We will choose the `:latest-dev` image that was last updated on September 2, 2023 at the time this document was being prepared.

```sh
docker pull cgr.dev/chainguard/git@sha256:f6658e10edde332c6f1dc804f0f664676dc40db78ba4009071fea6b9d97d592f
```

When you pull this image, you'll receive output of the digest which should match the exact digest you have pulled.

To learn more about image digests, you can review our video [How to Use Container Image Digests to Improve Reproducibility](/chainguard/chainguard-images/videos/container-image-digests/).

### Specifying Architecture

As Chainguard Images are [built for both AMD64 and ARM64 architecture](/chainguard/chainguard-images/overview/#architecture), you can specify the architecture you would like to use by employing the `--platform` flag with the `docker pull` command. In this example, we'll specify using the `linux/arm64` architecture with the Go image.

```sh
docker pull --platform=linux/arm64 cgr.dev/chainguard/go
```

After pulling the image, you can verify the architecture by calling the version.

```sh
docker run --rm -t cgr.dev/chainguard/go:latest version
```

You'll receive output similar to the following:

```sh
go version go1.21.0 linux/arm64
```

Specifying the platform will ensure that you're using the desired image and relevant architecture.

### Running a Chainguard Image

You can run a Chainguard Image with the `docker run` command. Note that because Chainguard Images are minimalist containers, most of them ship without a shell or package manager. If you would like a shell, you can often use the development image, which is tagged as `:latest-dev` (for example, [Python](/chainguard/chainguard-images/reference/python/getting-started-python/) has its dev image at `cgr.dev/chainguard/python:latest-dev`). Otherwise, you can work with Chainguard Images in way similar to other images.

Let's run the [Cosign Chainguard Image](/chainguard/chainguard-images/reference/cosign/overview/) to check its version.

```sh
docker run --rm -t cgr.dev/chainguard/cosign:latest version
```

You'll receive the version information that confirms the image is working as expected.

```
  ______   ______        _______. __    _______ .__   __.
 /      | /  __  \      /       ||  |  /  _____||  \ |  |
|  ,----'|  |  |  |    |   (----`|  | |  |  __  |   \|  |
|  |     |  |  |  |     \   \    |  | |  | |_ | |  . `  |
|  `----.|  `--'  | .----)   |   |  | |  |__| | |  |\   |
 \______| \______/  |_______/    |__|  \______| |__| \__|
cosign: A tool for Container Signing, Verification and Storage in an OCI registry.

GitVersion:    2.0.0
GitCommit:     unknown
GitTreeState:  unknown
BuildDate:     unknown
GoVersion:     go1.20.1
Compiler:      gc
Platform:      linux/arm64
```

If you would like to review a filesystem, you can use the [wolfi-base image](/chainguard/chainguard-images/reference/wolfi-base/overview/):

```sh
docker run -it cgr.dev/chainguard/wolfi-base
```

This will start a Wolfi container where you can explore the file system and investigate which packages are available.

Continue reading the next section to learn more about building off of the Wolfi base image.

## Getting Started with Distroless Base Images

Chainguard Images are fully OCI compatible, which means they work seamlessly with any system that supports that standard, including Docker.

Most Chainguard Images do not include a package manager such as `apt` or `apk`. This is by design to keep images minimal, following the distroless approach.

There are a few different ways to include additional software on distroless images, depending on your use case. If you are using Chainguard Images with  Dockerfile pipelines, you can add artifacts from a multi-stage Docker build. Alternatively, you can use Chainguard’s [apko](/open-source/apko/getting-started-with-apko/) and [melange](/open-source/melange/tutorials/getting-started-with-melange/) tooling to add extra software (this will also give you some extra features like build-time SBOM support).

### Using the Distroless Base Images

Many of the images are intended as platforms for running compiled binaries in as minimal an environment as possible. In the case of languages that can compile completely static binaries (such as C and Rust), the static base image can be used.

Let's work on an example. Navigate to a test directory. For example:

```sh
mkdir ~/distroless-example && cd $_
```

In this directory, we'll create an example Dockerfile that builds a "Hello, World!" program in C.

You can create the Dockerfile with nano, for instance.

```sh
nano Dockerfile
```

We will create the program on top of the `cgr.dev/chainguard/static:latest` base image.

```dockerfile
# syntax=docker/dockerfile:1.4
FROM cgr.dev/chainguard/gcc-glibc:latest as build

COPY <<EOF /hello.c
#include <stdio.h>
int main() { printf("Hello Distroless!%c",0x0A); }
EOF
RUN cc -static /hello.c -o /hello

FROM cgr.dev/chainguard/static:latest

COPY --from=build /hello /hello
CMD ["/hello"]
```

Run the following command to build the demo image and tag it as `c-distroless`:

```shell
DOCKER_BUILDKIT=1 docker build -t c-distroless  .
```

If you receive an error, you may try removing the top line of the Dockerfile. Now you can run the image with:

```shell
docker run c-distroless
```

You should get output like this:

```
Hello Distroless!
```

You can note the size of the resulting image.

```shell
docker images c-distroless
```

```
REPOSITORY     TAG       IMAGE ID       CREATED              SIZE
c-distroless   latest    d3b1c78f4ed2   8 seconds ago   3.31MB
```

### Extending Chainguard Base Images

It often happens that you want a distroless image with one or two extra packages, for example you may have a binary with a dependency on `curl` or `git`. Ideally you’d like a base image with this dependency already installed. There are a few options here:

1. Compile the dependency from source and use a multi-stage Dockerfile to create a new base image. This works, but may require considerable effort to get the dependency compiling and to keep it up to date. This process quickly becomes untenable if you require several dependencies.
2. Use the `wolfi-base` image that includes apk tools to install the package in the traditional Dockerfile manner. This works but sacrifices a lot of the advantages of the “distroless” philosophy.
3. Use Chainguard’s [melange and apko tooling to create a custom base image](/open-source/melange/tutorials/getting-started-with-melange/). This keeps the image as minimal as possible without sacrificing maintainability.

### Using the wolfi-base Image
The `wolfi-base` image is a good starting point to try out Chainguard Images. Unlike most of the other images, which are strictly distroless, `wolfi-base` includes the `apk` package manager, which facilitates composing additional software into it. Just keep in mind that the resulting image will be a little larger due to the extra software and won't have a comprehensive SBOM that covers all your dependencies, since the new software will be added as a layer on top of `wolfi-base`.

The following command will pull the `wolfi-base` image to your local system and run an interactive shell that you can use to explore the image features:

```shell
docker run -it --rm cgr.dev/chainguard/wolfi-base /bin/sh -l
```

First you will need to update the list of packages available in Wolfi:

```shell
apk update
```

Now you can use `apk search` to search for packages that are already available on Wolfi repositories:

```shell
apk search curl
```

More packages will be added with time, as the ecosystem matures and drives community involvement.

_Looking for a specific package that is not yet available? Feel free to open an issue on the [wolfi-os](https://github.com/chainguard-dev/wolfi-os) GitHub repository._

### Using the wolfi-base Image within Dockerfiles

Following, you can see an example of a Dockerfile that uses `wolfi-base` as base image, installing the packages `curl` and `jq` in order to make a query to the [advice slip](https://api.adviceslip.com/) API:

```dockerfile
FROM cgr.dev/chainguard/wolfi-base

RUN apk update && apk add --no-cache --update-cache curl jq

CMD curl -s https://api.adviceslip.com/advice --http1.1 | jq .slip.advice
```

You can build this Dockerfile as usual:

```shell
docker build . -t advice-slip:test
```

Then, execute the image with:

```shell
docker run -it --rm advice-slip:test
```

You should get output like this, with a random piece of advice:

```
"Big things have small beginnings."
```

