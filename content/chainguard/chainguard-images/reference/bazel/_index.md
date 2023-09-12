---
title: "Image Overview: bazel"
linktitle: "bazel"
type: "article"
layout: "single"
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

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/bazel/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/bazel/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/bazel/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/bazel/provenance_info/" >}}
{{</ tabs >}}



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

