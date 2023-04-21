---
title: "node Image Variants"
type: "article"
description: "Detailed specs for node Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "node"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **node** Image.

## Variants Compared
The **node** Chainguard Image currently has 6 public variants: 

- `latest`
- `latest-dev`
- `19`
- `19-dev`
- `20`
- `20-dev`

The table has detailed information about each of these variants.

|              | latest          | latest-dev      | 19              | 19-dev          | 20              | 20-dev          |
|--------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
| Default User | `node`          | `node`          | `node`          | `node`          | `node`          | `node`          |
| Entrypoint   | `/usr/bin/node` | `/usr/bin/node` | `/usr/bin/node` | `/usr/bin/node` | `/usr/bin/node` | `/usr/bin/node` |
| CMD          | `--help`        | `--help`        | `--help`        | `--help`        | `--help`        | `--help`        |
| Workdir      | `/app`          | `/app`          | `/app`          | `/app`          | `/app`          | `/app`          |
| Has apk?     | no              | yes             | no              | yes             | no              | yes             |
| Has a shell? | yes             | yes             | yes             | yes             | yes             | yes             |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev | 19 | 19-dev | 20 | 20-dev |
|--------------------------|--------|------------|----|--------|----|--------|
| `busybox`                | X      | X          | X  | X      | X  | X      |
| `ca-certificates-bundle` | X      | X          | X  | X      | X  | X      |
| `nghttp2`                | X      | X          | X  | X      | X  | X      |
| `nodejs`                 | X      | X          |    |        |    |        |
| `wolfi-baselayout`       | X      | X          | X  | X      | X  | X      |
| `apk-tools`              |        | X          |    | X      |    | X      |
| `bash`                   |        | X          |    | X      |    | X      |
| `git`                    |        | X          |    | X      |    | X      |
| `yarn`                   |        | X          |    | X      |    | X      |
| `build-base`             |        | X          |    | X      |    | X      |
| `python-3.11`            |        | X          |    | X      |    | X      |
| `nodejs-19`              |        |            | X  | X      |    |        |
| `nodejs-20`              |        |            |    |        | X  | X      |

