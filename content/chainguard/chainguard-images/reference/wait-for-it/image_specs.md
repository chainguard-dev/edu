---
title: "wait-for-it Image Variants"
type: "article"
description: "Detailed specs for wait-for-it Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "wait-for-it"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **wait-for-it** Image.

## Variants Compared
The **wait-for-it** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                 |
|--------------|------------------------|
| Default User | `root`                 |
| Entrypoint   | `/usr/bin/wait-for-it` |
| CMD          | not specified          |
| Workdir      | not specified          |
| Has apk?     | no                     |
| Has a shell? | no                     |

## Image Dependencies
The table shows package distribution across all variants.

|                    | latest |
|--------------------|--------|
| `wait-for-it`      | X      |
| `wolfi-baselayout` | X      |
