---
title: "cc-dynamic Image Variants"
type: "article"
description: "Detailed specs for cc-dynamic Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "cc-dynamic"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **cc-dynamic** Image.

## Variants Compared
The **cc-dynamic** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest        |
|--------------|---------------|
| Default User | `nonroot`     |
| Entrypoint   | not specified |
| CMD          | not specified |
| Workdir      | not specified |
| Has apk?     | no            |
| Has a shell? | no            |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `glibc`                  | X      |
| `libgcc`                 | X      |
| `wolfi-baselayout`       | X      |
