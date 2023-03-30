---
title: "prometheus Image Variants"
type: "article"
description: "Detailed specs for prometheus Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "prometheus"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **prometheus** Image.

## Variants Compared
The **prometheus** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest        |
|--------------|---------------|
| Default User | `root`        |
| Entrypoint   | `prometheus`  |
| CMD          | not specified |
| Workdir      | not specified |
| Has apk?     | no            |
| Has a shell? | no            |

## Image Dependencies
The table shows package distribution across all variants.

|                    | latest |
|--------------------|--------|
| `prometheus`       | X      |
| `wolfi-baselayout` | X      |

