---
title: "Bazel Image Variants"
type: "article"
description: "Detailed information about the Bazel Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Bazel"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Bazel** Image.

## Variants Compared
The **bazel** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest           | latest-dev       |
|--------------|------------------|------------------|
| Default User | `bazel`          | `bazel`          |
| Entrypoint   | `/usr/bin/bazel` | `/usr/bin/bazel` |
| CMD          | not specified    | not specified    |
| Workdir      | `/home/bazel`    | `/home/bazel`    |
| Has apk?     | no               | yes              |
| Has a shell? | yes              | yes              |

Check the [tags history page](/chainguard/chainguard-images/reference/bazel/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `openjdk-17`             | X      | X          |
| `openjdk-17-default-jvm` | X      | X          |
| `bash`                   | X      | X          |
| `busybox`                | X      | X          |
| `gcc`                    | X      | X          |
| `git`                    | X      | X          |
| `bazel-6`                | X      | X          |
| `zip`                    | X      | X          |
| `file`                   | X      | X          |
| `openssh-client`         | X      | X          |
| `build-base`             | X      | X          |
