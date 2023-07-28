---
title: "Gradle Image Variants"
type: "article"
description: "Detailed information about the Gradle Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Gradle"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Gradle** Image.

## Variants Compared
The **gradle** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

## Default Image Settings
`USER`:		`gradle`

`WORKDIR`:	`/home/build`

`ENTRYPOINT`:	`/usr/bin/gradle`

`CMD`:		not specified

The following table has additional information about each of these variants.

|              | latest | latest-dev |
|--------------|--------|------------|
| Has apk?     | no     | yes        |
| Has a shell? | yes    | yes        |

Check the [tags history page](/chainguard/chainguard-images/reference/gradle/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `glibc-locale-en`        | X      | X          |
| `busybox`                | X      | X          |
| `gradle-8`               | X      | X          |
| `openjdk-17`             | X      | X          |
| `openjdk-17-default-jvm` | X      | X          |
