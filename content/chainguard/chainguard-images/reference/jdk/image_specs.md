---
title: "jdk Image Variants"
type: "article"
description: "Detailed specs for jdk Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "jdk"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **jdk** Image.

## Variants Compared
The **jdk** Chainguard Image currently has 2 public variants: 

- `latest`
- `openjdk-11`

The table has detailed information about each of these variants.

|              | latest        | openjdk-11    |
|--------------|---------------|---------------|
| Default User | `java`        | `java`        |
| Entrypoint   | not specified | not specified |
| CMD          | not specified | not specified |
| Workdir      | `/home/build` | `/home/build` |
| Has apk?     | no            | no            |
| Has a shell? | yes           | yes           |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | openjdk-11 |
|--------------------------|--------|------------|
| `ca-certificates-bundle` | X      | X          |
| `wolfi-baselayout`       | X      | X          |
| `glibc-locale-en`        | X      | X          |
| `busybox`                | X      | X          |
| `openjdk-17`             | X      |            |
| `openjdk-11`             |        | X          |
