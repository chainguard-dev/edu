---
title: "haproxy Image Variants"
type: "article"
description: "Detailed specs for haproxy Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "haproxy"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **haproxy** Image.

## Variants Compared
The **haproxy** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                                |
|--------------|---------------------------------------|
| Default User | `haproxy`                             |
| Entrypoint   | `/usr/local/bin/docker-entrypoint.sh` |
| CMD          | not specified                         |
| Workdir      | not specified                         |
| Has apk?     | no                                    |
| Has a shell? | no                                    |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `wolfi-baselayout`       | X      |
| `haproxy`                | X      |
| `haproxy-oci-entrypoint` | X      |
| `dataplaneapi`           | X      |
