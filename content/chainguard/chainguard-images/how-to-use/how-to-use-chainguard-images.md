---
title: "How to Use Chainguard Images"
linktitle: "Using Chainguard Images"
aliases:
- /chainguard/chainguard-images/how-to-use-chainguard-images/
- /chainguard/chainguard-images/how-to-use/how-to-use-chainguard-images/
type: "article"
description: "A primer on how to migrate to Chainguard Images"
lead: "A primer on how to migrate to Chainguard Images"
date: 2022-09-01T08:49:31+00:00
lastmod: 2025-02-26T15:56:52-07:00
draft: false
tags: ["CHAINGUARD IMAGES", "PROCEDURAL", "PRODUCT"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 005
toc: true
---

[Chainguard Images](https://images.chainguard.dev) are based on [Wolfi](/open-source/wolfi/overview/), our Linux _undistro_ designed specifically for containers. Wolfi uses the [Alpine apk](https://wiki.alpinelinux.org/wiki/Package_management) package format, which contributes in making packages smaller and more accountable, resulting in smaller images with traceable provenance information based on cryptographic signatures.

In this guide, you'll find general instructions on how to get started using Chainguard Images and how to migrate existing container-based workflows to use our images. For specific image usage instructions, please refer to our [Chainguard Images Directory](https://images.chainguard.dev), which contains the full list of all images available to the public and their respective documentation.

## Quickstart: Using Chainguard Images

To get up and running with Chainguard Images, you can use `docker` commands to pull and run images. For each specific image, you'll find this guidance on its overview page (for example, see [Node](https://images.chainguard.dev/directory/image/node/overview?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-how-to-use-chainguard-images), [Python](https://images.chainguard.dev/directory/image/python/overview?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-how-to-use-chainguard-images), or [NGINX](https://images.chainguard.dev/directory/image/nginx/overview?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-how-to-use-chainguard-images)).

### Pulling a Chainguard Image

You can pull a Chainguard Image with the `docker pull` command. For example, to pull down the Git Chainguard Image, you can run the following.

```sh
docker pull cgr.dev/chainguard/git
```

Without passing a tag or a digest, the reference to the Git image will pull down the default tag, which is `:latest`.

If you have your own registry, you'll need to change the `cgr.dev/chainguard` path to your own registry path.

Chainguard [Starter Images](/chainguard/chainguard-images/about/images-categories/#starter-containers) are also available on Docker Hub. Check out [Chainguard's organization page on Docker Hub](https://hub.docker.com/u/chainguard?utm_source=academy&utm_medium=referral&utm_campaign=FY25-DockerHub-Orgprofile) for a list of all images and instructions. Note that Production Images can only be accessed from cgr.dev.

### Pulling by Tag

You can also add a relevant tag that you have access to. In the case of the public Git image, you can always pull the `:latest` tag. [Note that not all tags are available for public images](/chainguard/chainguard-images/faq/#do-i-need-to-authenticate-into-chainguard-to-use-chainguard-images).

```sh
docker pull cgr.dev/chainguard/git:latest
```

You may use tags to pull a specific version of a software like Git, or programming language version in a catalog you have access to. The Chainguard Images Directory has tag history pages for each image, for example, the [Git Image Tags History](https://images.chainguard.dev/directory/image/git/versions?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-how-to-use-chainguard-images), [PHP Image Tags History](https://images.chainguard.dev/directory/image/php/versions?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-how-to-use-chainguard-images), and [JDK Image Tags History](https://images.chainguard.dev/directory/image/jdk/versions?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-how-to-use-chainguard-images).

You can learn about the Chainguard Images tags history in our guide about [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/).

### Pulling by Digest

Pulling a Chainguard Image by its digest guarantees reproducibility, as it will ensure that you are using the same image each time (versus the tag that may receive updates).

To pull an image by its digest, you can do so by appending the digest which begins with `sha256`.<!-- You can find these on our reference tags history pages. -->

<!-- In our Git example, we can review the [Git Image Tags History](https://images.chainguard.dev/directory/image/git/versions?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-how-to-use-chainguard-images) page and choose a relevant digest. We will choose the `:latest-dev` image that was last updated on September 2, 2023 at the time this document was being prepared. -->

<!-- TODO(juverm) - do we want to broadcast the above? We don't show digests in public directory because we want free tier pinned on latest. -->

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

You can run a Chainguard Image with the `docker run` command. Note that because Chainguard Images are minimalist containers, most of them ship without a shell or package manager. If you would like a shell, you can often use the development image, which is tagged as `:latest-dev` (for example, [Python](https://images.chainguard.dev/directory/image/python/overview?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-how-to-use-chainguard-images) has its dev image at `cgr.dev/chainguard/python:latest-dev`). Otherwise, you can work with Chainguard Images in way similar to other images.

Let's run the [Cosign Chainguard Image](https://images.chainguard.dev/directory/image/cosign/overview?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-how-to-use-chainguard-images) to check its version.

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

If you would like to review a filesystem, you can use the [wolfi-base image](https://images.chainguard.dev/directory/image/wolfi-base/overview?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-how-to-use-chainguard-images):

```sh
docker run -it cgr.dev/chainguard/wolfi-base
```

This will start a Wolfi container where you can explore the file system and investigate which packages are available.

Continue reading the next section to learn more about building off of the Wolfi base image.

## Extending Chainguard Base Images

It often happens that you want a [distroless](/chainguard/chainguard-images/getting-started-distroless/) image with one or two extra packages, for example you may have a binary with a dependency on `curl` or `git`. Ideally you’d like a base image with this dependency already installed. There are a few options here:

1. Compile the dependency from source and use a multi-stage Dockerfile to create a new base image. This works, but may require considerable effort to get the dependency compiling and to keep it up to date. This process quickly becomes untenable if you require several dependencies.
2. Use the `wolfi-base` image that includes apk tools to install the package in the traditional Dockerfile manner. This works but sacrifices a lot of the advantages of the “distroless” philosophy.
3. Use Chainguard’s [melange and apko tooling to create a custom base image](/open-source/build-tools/melange/getting-started-with-melange/). This keeps the image as minimal as possible without sacrificing maintainability.

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

SHELL ["/bin/sh", "-c"]

CMD curl -s https://api.adviceslip.com/advice --http1.1 | jq .slip.advice
```

The `SHELL` command suppresses a warning about the `CMD` line using shell syntax, which isn't a
problem in this example. In other cases, you may want to use the [exec
form](https://docs.docker.com/reference/dockerfile/#shell-and-exec-form).

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

Check also the [Wolfi Images with Dockerfiles](/open-source/wolfi/wolfi-with-dockerfiles/) guide for more examples using Wolfi-based images with Dockerfiles, and the [Getting Started with Distroless](/chainguard/chainguard-images/getting-started-distroless/) guide for more details about distroless images and how to use them in Docker multi-stage builds.


## A Note regarding package availability in Chainguard Images

Chainguard Images only contain packages that come from the [Wolfi Project](https://github.com/wolfi-dev) or those that are built and maintained internally by Chainguard.

Starting in March of 2024, Chainguard will maintain one version of each Wolfi package at a time. These will track the latest version of the upstream software in the package. Chainguard will end patch support for previous versions of packages in Wolfi. Existing packages will not be removed from Wolfi and you may continue to use them, but be aware that older packages will no longer be updated and will accrue vulnerabilities over time. The tools we use to build packages and images remain freely available and open source in [Wolfi](https://github.com/wolfi-dev).

This change ensures that Chainguard can provide the most up-to-date patches to all packages for our Images customers. Note that specific package versions can be made available in Production Images. If you have a request for a specific package version, please [contact us](https://www.chainguard.dev/contact?utm=docs).
