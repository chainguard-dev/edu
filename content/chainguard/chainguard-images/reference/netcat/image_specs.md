---
title: "Netcat Image Variants"
type: "article"
description: "Detailed information about the NetcatChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Netcat"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Netcat** Image.

## Variants Compared
The **netcat** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest        | latest-dev    |
|--------------|---------------|---------------|
| Default User | `nonroot`     | `nonroot`     |
| Entrypoint   | `/usr/bin/nc` | `/usr/bin/nc` |
| CMD          | `-h`          | `-h`          |
| Workdir      | `/home/nc`    | `/home/nc`    |
| Has apk?     | no            | yes           |
| Has a shell? | yes           | yes           |

Check the [tags history page](/chainguard/chainguard-images/reference/netcat/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                  | latest | latest-dev |
|------------------|--------|------------|
| `busybox`        | X      | X          |
| `netcat-openbsd` | X      | X          |
