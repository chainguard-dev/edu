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
The **nats** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                                |
|--------------|---------------------------------------|
| Default User | `nats`                                |
| Entrypoint   | `/usr/bin/nats-server`                |
| CMD          | `--config=/etc/nats/nats-server.conf` |
| Workdir      | not specified                         |
| Has apk?     | no                                    |
| Has a shell? | no                                    |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `wolfi-baselayout`       | X      |
| `nats`                   | X      |
| `nsc`                    | X      |
| `nats-server`            | X      |
