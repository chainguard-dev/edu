---
title: "Redis Public Image Variants"
type: "article"
description: "Detailed information about the public Redis Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Redis"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **Redis** Image.

## Variants Compared
The **redis** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest         |
|--------------|----------------|
| Default User | `redis`        |
| Entrypoint   | `redis-server` |
| CMD          | not specified  |
| Workdir      | `/data`        |
| Has apk?     | no             |
| Has a shell? | yes            |

Check the [tags history page](/chainguard/chainguard-images/reference/redis/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `busybox`                | X      |
| `ca-certificates-bundle` | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `ld-linux`               | X      |
| `libcrypt1`              | X      |
| `libcrypto3`             | X      |
| `libssl3`                | X      |
| `openssl-config`         | X      |
| `redis`                  | X      |
| `wolfi-baselayout`       | X      |
