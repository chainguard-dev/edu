---
title: "go Image Variants"
type: "article"
description: "Detailed specs for go Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "go"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **go** Image.

## Variants Compared
The **go** Chainguard Image currently has 2 public variants: 

- `1.19`
- `latest`

The table has detailed information about each of these variants.

|              | 1.19          | latest        |
|--------------|---------------|---------------|
| Default User | ``            | ``            |
| Entrypoint   | `/usr/bin/go` | `/usr/bin/go` |
| CMD          | `help`        | `help`        |
| Workdir      | not specified | not specified |
| Has apk?     | no            | no            |
| Has a shell? | yes           | yes           |

## Image Dependencies
The table shows package distribution across all variants.

|                          | 1.19 | latest |
|--------------------------|------|--------|
| `ca-certificates-bundle` | X    | X      |
| `busybox`                | X    | X      |
| `build-base`             | X    | X      |
| `git`                    | X    | X      |
| `go-1.19`                | X    |        |
| `openssh`                | X    | X      |
| `wolfi-baselayout`       | X    | X      |
| `go-1.20`                |      | X      |
