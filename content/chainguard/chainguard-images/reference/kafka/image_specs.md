---
title: "kafka Image Variants"
type: "article"
description: "Detailed specs for kafka Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "kafka"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **kafka** Image.

## Variants Compared
The **kafka** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                                     | latest-dev                                 |
|--------------|--------------------------------------------|--------------------------------------------|
| Default User | `kafka`                                    | `kafka`                                    |
| Entrypoint   | `/usr/lib/kafka/bin/kafka-server-start.sh` | `/usr/lib/kafka/bin/kafka-server-start.sh` |
| CMD          | `/usr/lib/kafka/config/server.properties`  | `/usr/lib/kafka/config/server.properties`  |
| Workdir      | not specified                              | not specified                              |
| Has apk?     | no                                         | yes                                        |
| Has a shell? | yes                                        | yes                                        |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `ca-certificates-bundle` | X      | X          |
| `wolfi-baselayout`       | X      | X          |
| `bash`                   | X      | X          |
| `busybox`                | X      | X          |
| `kafka`                  | X      | X          |
| `apk-tools`              |        | X          |
| `git`                    |        | X          |
