---
title: "zookeeper Image Variants"
type: "article"
description: "Detailed specs for zookeeper Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "zookeeper"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **zookeeper** Image.

## Variants Compared
The **zookeeper** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                                      |
|--------------|---------------------------------------------|
| Default User | `zookeeper`                                 |
| Entrypoint   | `/usr/share/java/zookeeper/bin/zkServer.sh` |
| CMD          | `start-foreground`                          |
| Workdir      | not specified                               |
| Has apk?     | no                                          |
| Has a shell? | yes                                         |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `wolfi-baselayout`       | X      |
| `busybox`                | X      |
| `glibc-locale-en`        | X      |
| `bash`                   | X      |
| `zookeeper`              | X      |
| `openjdk-17-jre`         | X      |
