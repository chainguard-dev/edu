---
title: "nats Image Variants"
type: "article"
description: "Detailed specs for nats Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "nats"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **nats** Image.

## Variants Compared
The **nats** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                                | latest-dev                            |
|--------------|---------------------------------------|---------------------------------------|
| Default User | `nats`                                | `nats`                                |
| Entrypoint   | `/usr/bin/nats-server`                | `/usr/bin/nats-server`                |
| CMD          | `--config=/etc/nats/nats-server.conf` | `--config=/etc/nats/nats-server.conf` |
| Workdir      | not specified                         | not specified                         |
| Has apk?     | no                                    | yes                                   |
| Has a shell? | no                                    | yes                                   |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `ca-certificates-bundle` | X      | X          |
| `wolfi-baselayout`       | X      | X          |
| `nats`                   | X      | X          |
| `nsc`                    | X      | X          |
| `nats-server`            | X      | X          |
| `apk-tools`              |        | X          |
| `bash`                   |        | X          |
| `busybox`                |        | X          |
