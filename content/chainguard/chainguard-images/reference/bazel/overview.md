---
title: "Image Overview: bazel"
type: "article"
description: "Overview: bazel Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "images-reference"
weight: 500
toc: true
---

[cgr.dev/chainguard/bazel](https://github.com/chainguard-images/images/tree/main/images/bazel)

| Tag (s)   | Last Changed | Digest                                                                    |
|-----------|--------------|---------------------------------------------------------------------------|
|  `latest` | August 23rd  | `sha256:a7bf6131ca22ffb5f889c054e44da8e4e3e4dac88aece1c4549fe7dff2ecab2d` |



[Bazel](https://github.com/bazelbuild/bazel) - A fast, scalable, multi-language and extensible build system.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/bazel
```

## Using Bazel

We can use the Bazel examples to try this image.

first clone https://github.com/bazelbuild/examples

```sh
git clone git@github.com:bazelbuild/examples.git
```

change into the Java tutorial directory

```
cd examples/java-tutorial
```

now run the chainguard image, mounting the example and overwrite the entrypoint to bash

```sh
docker run --rm -ti --entrypoint bash -v ${PWD}:/home/bazel cgr.dev/chainguard/bazel
```

once in the container you can perform a build

```sh
bazel build //:ProjectRunner
```

and now run the example

```sh
bazel-bin/ProjectRunner
```

and see the message from the example application

```sh
Hi
```

