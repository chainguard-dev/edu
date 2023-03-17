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
The **zookeeper** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                                      | latest-dev                                  |
|--------------|---------------------------------------------|---------------------------------------------|
| Default User | `zookeeper`                                 | `zookeeper`                                 |
| Entrypoint   | `/usr/share/java/zookeeper/bin/zkServer.sh` | `/usr/share/java/zookeeper/bin/zkServer.sh` |
| CMD          | `start-foreground`                          | `start-foreground`                          |
| Workdir      | not specified                               | not specified                               |
| Has apk?     | no                                          | yes                                         |
| Has a shell? | yes                                         | yes                                         |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `ca-certificates-bundle` | X      | X          |
| `wolfi-baselayout`       | X      | X          |
| `busybox`                | X      | X          |
| `glibc-locale-en`        | X      | X          |
| `bash`                   | X      | X          |
| `zookeeper`              | X      | X          |
| `openjdk-17-jre`         | X      | X          |
| `apk-tools`              |        | X          |
