---
title: "rabbitmq Image Variants"
type: "article"
description: "Detailed specs for rabbitmq Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "rabbitmq"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **rabbitmq** Image.

## Variants Compared
The **rabbitmq** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                      |
|--------------|-----------------------------|
| Default User | `rabbitmq`                  |
| Entrypoint   | `/usr/sbin/rabbitmq-server` |
| CMD          | not specified               |
| Workdir      | `/var/lib/rabbitmq`         |
| Has apk?     | no                          |
| Has a shell? | yes                         |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `rabbitmq-server`        | X      |
| `wolfi-baselayout`       | X      |
| `bash`                   | X      |
| `glibc-locale-en`        | X      |
| `tzdata`                 | X      |
| `ca-certificates-bundle` | X      |

