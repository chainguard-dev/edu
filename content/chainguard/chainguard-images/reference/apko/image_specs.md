---
title: "apko Image Variants"
type: "article"
description: "Detailed information about the public apko Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "apko"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **apko** Image.

## Variants Compared
The **apko** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest          |
|--------------|-----------------|
| Default User | `root`          |
| Entrypoint   | `/usr/bin/apko` |
| CMD          | `--help`        |
| Workdir      | `/work`         |
| Has apk?     | no              |
| Has a shell? | no              |

Check the [tags history page](/chainguard/chainguard-images/reference/apko/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `alpine-keys`            | X      |
| `apko`                   | X      |
| `ca-certificates-bundle` | X      |
| `wolfi-baselayout`       | X      |
| `wolfi-keys`             | X      |
