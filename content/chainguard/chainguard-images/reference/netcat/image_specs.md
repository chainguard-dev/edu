---
title: "netcat Image Variants"
type: "article"
description: "Detailed specs for netcat Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "netcat"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **netcat** Image.

## Variants Compared
The **netcat** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest        |
|--------------|---------------|
| Default User | `nonroot`     |
| Entrypoint   | `/usr/bin/nc` |
| CMD          | `-h`          |
| Workdir      | `/home/nc`    |
| Has apk?     | no            |
| Has a shell? | no            |

## Image Dependencies
The table shows package distribution across all variants.

|                    | latest |
|--------------------|--------|
| `wolfi-baselayout` | X      |
| `netcat-openbsd`   | X      |
