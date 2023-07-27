---
title: "Jre Image Variants"
type: "article"
description: "Detailed information about the JreChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Jre"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Jre** Image.

## Variants Compared
The **jre** Chainguard Image currently has 6 public variants: 

- `latest`
- `latest-dev`
- `openjdk-17`
- `openjdk-17-dev`
- `openjdk-11`
- `openjdk-11-dev`

The table has detailed information about each of these variants.

|              | latest          | latest-dev      | openjdk-17      | openjdk-17-dev  | openjdk-11      | openjdk-11-dev  |
|--------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
| Default User | `java`          | `java`          | `java`          | `java`          | `java`          | `java`          |
| Entrypoint   | `/usr/bin/java` | `/usr/bin/java` | `/usr/bin/java` | `/usr/bin/java` | `/usr/bin/java` | `/usr/bin/java` |
| CMD          | not specified   | not specified   | not specified   | not specified   | not specified   | not specified   |
| Workdir      | `/app`          | `/app`          | `/app`          | `/app`          | `/app`          | `/app`          |
| Has apk?     | no              | yes             | no              | yes             | no              | yes             |
| Has a shell? | no              | yes             | no              | yes             | no              | yes             |

Check the [tags history page](/chainguard/chainguard-images/reference/jre/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev | openjdk-17 | openjdk-17-dev | openjdk-11 | openjdk-11-dev |
|--------------------------|--------|------------|------------|----------------|------------|----------------|
| `glibc-locale-en`        | X      | X          | X          | X              | X          | X              |
| `openjdk-17-jre`         | X      | X          | X          | X              |            |                |
| `openjdk-17-default-jvm` | X      | X          | X          | X              |            |                |
| `libstdc++`              | X      | X          | X          | X              | X          | X              |
| `openjdk-11-jre`         |        |            |            |                | X          | X              |
| `openjdk-11-default-jvm` |        |            |            |                | X          | X              |
