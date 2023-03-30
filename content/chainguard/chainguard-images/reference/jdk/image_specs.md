---
title: "jdk Image Variants"
type: "article"
description: "Detailed specs for jdk Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "jdk"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **jdk** Image.

## Variants Compared
The **jdk** Chainguard Image currently has 4 public variants: 

- `latest`
- `latest-dev`
- `openjdk-11`
- `openjdk-11-dev`

The table has detailed information about each of these variants.

|              | latest        | latest-dev    | openjdk-11    | openjdk-11-dev |
|--------------|---------------|---------------|---------------|----------------|
| Default User | `java`        | `java`        | `java`        | `java`         |
| Entrypoint   | not specified | not specified | not specified | not specified  |
| CMD          | not specified | not specified | not specified | not specified  |
| Workdir      | `/home/build` | `/home/build` | `/home/build` | `/home/build`  |
| Has apk?     | no            | yes           | no            | yes            |
| Has a shell? | yes           | yes           | yes           | yes            |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev | openjdk-11 | openjdk-11-dev |
|--------------------------|--------|------------|------------|----------------|
| `ca-certificates-bundle` | X      | X          | X          | X              |
| `wolfi-baselayout`       | X      | X          | X          | X              |
| `glibc-locale-en`        | X      | X          | X          | X              |
| `busybox`                | X      | X          | X          | X              |
| `openjdk-17`             | X      | X          |            |                |
| `apk-tools`              |        | X          |            | X              |
| `bash`                   |        | X          |            | X              |
| `git`                    |        | X          |            | X              |
| `openjdk-11`             |        |            | X          | X              |

