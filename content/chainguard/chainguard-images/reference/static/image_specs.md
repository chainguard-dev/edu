---
title: "static Image Variants"
type: "article"
description: "Detailed information about the public static Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "static"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **static** Image.

## Variants Compared
The **static** Chainguard Image currently has 2 public variants: 

- `latest-glibc`
- `latest`

The table has detailed information about each of these variants.

|              | latest-glibc  | latest        |
|--------------|---------------|---------------|
| Default User | `nonroot`     | `nonroot`     |
| Entrypoint   | not specified | not specified |
| CMD          | not specified | not specified |
| Workdir      | not specified | not specified |
| Has apk?     | no            | no            |
| Has a shell? | no            | no            |

Check the [tags history page](/chainguard/chainguard-images/reference/static/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-glibc | latest |
|--------------------------|--------------|--------|
| `ca-certificates-bundle` | X            | X      |
| `tzdata`                 | X            | X      |
| `wolfi-baselayout`       | X            |        |
| `alpine-baselayout-data` |              | X      |
| `alpine-keys`            |              | X      |
| `alpine-release`         |              | X      |
