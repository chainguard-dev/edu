---
title: "How to Use Chainguard Images"
type: "article"
description: "A primer on how to migrate to Chainguard Images"
lead: "A primer on how to migrate to Chainguard Images"
date: 2022-09-01T08:49:31+00:00
lastmod: 2023-01-23T19:42:31+00:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 300
terminalImage: academy/chainguard-images:latest
toc: true
---

[Chainguard Images](https://www.chainguard.dev/chainguard-images?utm_source=docs) are distroless images based on [Wolfi](/open-source/wolfi/overview/), our Linux _undistro_. You can have a look at [Chainguard Image's GitHub org](https://github.com/chainguard-images) in order to find out which images are already available for general usage.

Each image has its own usage instructions, which is detailed in their READMEs. All images are hosted on the `cgr.dev` registry.

In this guide, you'll learn how to get started using Chainguard Images and how to migrate existing container-based workflows to use our images.

## Getting Started
Chainguard Images are fully OCI compatible, which means they work seamlessly with any system that supports that standard, including Docker.

Most Chainguard Images do not include a package manager such as `apt` or `apk`. This is by design to keep images minimal, following the distroless approach.

There are a few different ways to include additional software on distroless images, depending on your use case. If you are using Chainguard Images with  Dockerfile pipelines, you can add artifacts from a multi-stage Docker build. Alternatively, you can use Chainguard’s [apko](/open-source/apko/getting-started-with-apko/) and [melange](/open-source/melange/tutorials/getting-started-with-melange/) tooling to add extra software (this will also give you some extra features like build-time SBOM support).

### Using the Distroless Base Images

Many of the images are intended as platforms for running compiled binaries in as minimal an environment as possible. In the case of languages that can compile completely static binaries (such as C and Rust), the static base image can be used.

The following example Dockerfile builds a hello-world program in C and copies it on top of the `cgr.dev/chainguard/static:latest` base image:

```dockerfile
# syntax=docker/dockerfile:1.4
FROM cgr.dev/chainguard/gcc-musl:latest as build

COPY <<EOF /hello.c
#include <stdio.h>
int main() { printf("Hello Distroless!"); }
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

Now you can run the image with:

```shell
docker run c-distroless
```

You should get output like this:

```
Hello Distroless!
```

It’s worth noting how small the resulting image is:

```shell
docker images c-distroless
```

```
REPOSITORY     TAG       IMAGE ID       CREATED              SIZE
c-distroless   latest    de04a116ff9d   18 seconds ago   1.57MB
```

If your binary is dependent on `glibc` or `musl`, take a look at the [glibc-dynamic](https://github.com/chainguard-images/glibc-dynamic) and [musl-dynamic](https://github.com/chainguard-images/musl-dynamic) images.

We are working on similar images for runtimes such as the JVM.

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

