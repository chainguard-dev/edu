---
title: "python Image Variants"
type: "article"
description: "Detailed specs for python Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "python"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **python** Image.

## Variants Compared
The **python** Chainguard Image currently has 4 public variants: 

- `3.10`
- `3.10-dev`
- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | 3.10              | 3.10-dev          | latest            | latest-dev        |
|--------------|-------------------|-------------------|-------------------|-------------------|
| Default User | `nonroot`         | `nonroot`         | `nonroot`         | `nonroot`         |
| Entrypoint   | `/usr/bin/python` | `/usr/bin/python` | `/usr/bin/python` | `/usr/bin/python` |
| CMD          | not specified     | not specified     | not specified     | not specified     |
| Workdir      | not specified     | not specified     | not specified     | not specified     |
| Has apk?     | no                | yes               | no                | yes               |
| Has a shell? | no                | yes               | no                | yes               |

## Image Dependencies
The table shows package distribution across all variants.

|                          | 3.10 | 3.10-dev | latest | latest-dev |
|--------------------------|------|----------|--------|------------|
| `ca-certificates-bundle` | X    | X        | X      | X          |
| `python-3.10`            | X    | X        |        |            |
| `wolfi-baselayout`       | X    | X        | X      | X          |
| `apk-tools`              |      | X        |        | X          |
| `bash`                   |      | X        |        | X          |
| `busybox`                |      | X        |        | X          |
| `build-base`             |      | X        |        | X          |
| `py3.10-pip`             |      | X        |        |            |
| `python-3.10-dev`        |      | X        |        |            |
| `python-3.11`            |      |          | X      | X          |
| `py3.11-pip`             |      |          |        | X          |
| `python-3.11-dev`        |      |          |        | X          |
