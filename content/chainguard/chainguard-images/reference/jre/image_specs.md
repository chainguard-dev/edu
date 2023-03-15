---
title: "jre Image Variants"
type: "article"
description: "Detailed specs for jre Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "jre"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **jre** Image.

## Variants Compared
The **jre** Chainguard Image currently has 2 public variants: 

- `latest`
- `openjdk-11`

The table has detailed information about each of these variants.

|              | latest          | openjdk-11      |
|--------------|-----------------|-----------------|
| Default User | `java`          | `java`          |
| Entrypoint   | `/usr/bin/java` | `/usr/bin/java` |
| CMD          | not specified   | not specified   |
| Workdir      | `/app`          | `/app`          |
| Has apk?     | no              | no              |
| Has a shell? | no              | no              |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | openjdk-11 |
|--------------------------|--------|------------|
| `ca-certificates-bundle` | X      | X          |
| `wolfi-baselayout`       | X      | X          |
| `glibc-locale-en`        | X      | X          |
| `openjdk-17-jre`         | X      |            |
| `openjdk-11-jre`         |        | X          |
