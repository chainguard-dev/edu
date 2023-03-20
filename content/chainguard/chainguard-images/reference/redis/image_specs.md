---
title: "redis Image Variants"
type: "article"
description: "Detailed specs for redis Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "redis"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **redis** Image.

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

## Image Dependencies
The table shows package distribution across all variants.

|                    | latest |
|--------------------|--------|
| `redis`            | X      |
| `busybox`          | X      |
| `wolfi-baselayout` | X      |
