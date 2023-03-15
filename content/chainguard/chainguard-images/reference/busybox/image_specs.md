---
title: "busybox Image Variants"
type: "article"
description: "Detailed specs for busybox Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "busybox"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **busybox** Image.

## Variants Compared
The **busybox** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-glibc`

The table has detailed information about each of these variants.

|              | latest        | latest-glibc  |
|--------------|---------------|---------------|
| Default User | `nonroot`     | `nonroot`     |
| Entrypoint   | not specified | not specified |
| CMD          | not specified | not specified |
| Workdir      | not specified | not specified |
| Has apk?     | no            | no            |
| Has a shell? | yes           | yes           |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-glibc |
|--------------------------|--------|--------------|
| `alpine-baselayout-data` | X      |              |
| `ca-certificates-bundle` | X      | X            |
| `alpine-release`         | X      |              |
| `busybox`                | X      | X            |
| `ssl_client`             | X      |              |
| `wolfi-baselayout`       |        | X            |
