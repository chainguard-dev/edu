---
title: "Node Image Variants"
type: "article"
description: "Detailed information about the NodeChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Node"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Node** Image.

## Variants Compared
The **node** Chainguard Image currently has 8 public variants: 

- `latest`
- `latest-dev`
- `20`
- `20-dev`
- `19`
- `19-dev`
- `18`
- `18-dev`

The table has detailed information about each of these variants.

|              | latest          | latest-dev      | 20              | 20-dev          | 19              | 19-dev          | 18              | 18-dev          |
|--------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
| Default User | `node`          | `node`          | `node`          | `node`          | `node`          | `node`          | `node`          | `node`          |
| Entrypoint   | `/usr/bin/node` | `/usr/bin/node` | `/usr/bin/node` | `/usr/bin/node` | `/usr/bin/node` | `/usr/bin/node` | `/usr/bin/node` | `/usr/bin/node` |
| CMD          | `--help`        | `--help`        | `--help`        | `--help`        | `--help`        | `--help`        | `--help`        | `--help`        |
| Workdir      | `/app`          | `/app`          | `/app`          | `/app`          | `/app`          | `/app`          | `/app`          | `/app`          |
| Has apk?     | no              | yes             | no              | yes             | no              | yes             | no              | yes             |
| Has a shell? | yes             | yes             | yes             | yes             | yes             | yes             | yes             | yes             |

Check the [tags history page](/chainguard/chainguard-images/reference/node/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|             | latest | latest-dev | 20 | 20-dev | 19 | 19-dev | 18 | 18-dev |
|-------------|--------|------------|----|--------|----|--------|----|--------|
| `busybox`   | X      | X          | X  | X      | X  | X      | X  | X      |
| `nghttp2`   | X      | X          | X  | X      | X  | X      | X  | X      |
| `nodejs-20` | X      | X          | X  | X      |    |        |    |        |
| `nodejs-19` |        |            |    |        | X  | X      |    |        |
| `nodejs`    |        |            |    |        |    |        | X  | X      |
