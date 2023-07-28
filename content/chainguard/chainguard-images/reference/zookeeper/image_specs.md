---
title: "Zookeeper Image Variants"
type: "article"
description: "Detailed information about the Zookeeper Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Zookeeper"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Zookeeper** Image.

## Variants Compared
The **zookeeper** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

## Default Image Settings
`USER`:		`zookeeper`

`WORKDIR`:	not specified

`ENTRYPOINT`:	`/usr/share/java/zookeeper/bin/zkServer.sh`

`CMD`:		`start-foreground`

The following table has additional information about each of these variants.

|              | latest | latest-dev |
|--------------|--------|------------|
| Has apk?     | no     | yes        |
| Has a shell? | yes    | yes        |

Check the [tags history page](/chainguard/chainguard-images/reference/zookeeper/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `busybox`                | X      | X          |
| `glibc-locale-en`        | X      | X          |
| `bash`                   | X      | X          |
| `zookeeper`              | X      | X          |
| `openjdk-17-jre`         | X      | X          |
| `openjdk-17-default-jvm` | X      | X          |
