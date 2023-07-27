---
title: "Redis Image Variants"
type: "article"
description: "Detailed information about the RedisChainguard Image variants"
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

This page shows detailed information about all available variants of the Chainguard **Redis** Image.

## Variants Compared
The **redis** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest         | latest-dev     |
|--------------|----------------|----------------|
| Default User | `redis`        | `redis`        |
| Entrypoint   | `redis-server` | `redis-server` |
| CMD          | not specified  | not specified  |
| Workdir      | `/data`        | `/data`        |
| Has apk?     | no             | yes            |
| Has a shell? | yes            | yes            |

Check the [tags history page](/chainguard/chainguard-images/reference/redis/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|           | latest | latest-dev |
|-----------|--------|------------|
| `redis`   | X      | X          |
| `busybox` | X      | X          |
