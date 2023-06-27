---
title: "Go Image Variants"
type: "article"
description: "Detailed information about the GoChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Go"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Go** Image.

## Variants Compared
The **go** Chainguard Image currently has 4 public variants: 

- `1.19`
- `1.19-dev`
- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | 1.19          | 1.19-dev      | latest        | latest-dev    |
|--------------|---------------|---------------|---------------|---------------|
| Default User | `root`        | `root`        | `root`        | `root`        |
| Entrypoint   | `/usr/bin/go` | `/usr/bin/go` | `/usr/bin/go` | `/usr/bin/go` |
| CMD          | `help`        | `help`        | `help`        | `help`        |
| Workdir      | not specified | not specified | not specified | not specified |
| Has apk?     | no            | no            | no            | no            |
| Has a shell? | yes           | yes           | yes           | yes           |

Check the [tags history page](/chainguard/chainguard-images/reference/go/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | 1.19 | 1.19-dev | latest | latest-dev |
|--------------------------|------|----------|--------|------------|
| `ca-certificates-bundle` | X    | X        | X      | X          |
| `busybox`                | X    | X        | X      | X          |
| `build-base`             | X    | X        | X      | X          |
| `git`                    | X    | X        | X      | X          |
| `go-1.19`                | X    | X        |        |            |
| `openssh`                | X    | X        | X      | X          |
| `wolfi-baselayout`       | X    | X        | X      | X          |
| `go-1.20`                |      |          | X      | X          |
