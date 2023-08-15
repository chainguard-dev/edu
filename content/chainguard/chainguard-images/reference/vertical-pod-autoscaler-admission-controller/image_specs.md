---
title: "Vertical-pod-autoscaler-admission-controller Public Image Variants"
type: "article"
description: "Detailed information about the public Vertical-pod-autoscaler-admission-controller Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Vertical-pod-autoscaler-admission-controller"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **Vertical-pod-autoscaler-admission-controller** Image.

## Variants Compared
The **vertical-pod-autoscaler-admission-controller** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                      | latest                          |
|--------------|---------------------------------|---------------------------------|
| Default User | `nonroot`                       | `nonroot`                       |
| Entrypoint   | `/usr/bin/admission-controller` | `/usr/bin/admission-controller` |
| CMD          | `--v=4 --stderrthreshold=info`  | `--v=4 --stderrthreshold=info`  |
| Workdir      | not specified                   | not specified                   |
| Has apk?     | yes                             | no                              |
| Has a shell? | yes                             | no                              |

Check the [tags history page](/chainguard/chainguard-images/reference/vertical-pod-autoscaler-admission-controller/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                           | latest-dev | latest |
|---------------------------|------------|--------|
| `apk-tools`               | X          |        |
| `bash`                    | X          |        |
| `busybox`                 | X          |        |
| `ca-certificates-bundle`  | X          | X      |
| `git`                     | X          |        |
| `glibc`                   | X          | X      |
| `glibc-locale-posix`      | X          | X      |
| `ld-linux`                | X          | X      |
| `libbrotlicommon1`        | X          |        |
| `libbrotlidec1`           | X          |        |
| `libcrypt1`               | X          |        |
| `libcrypto3`              | X          |        |
| `libcurl-openssl4`        | X          |        |
| `libexpat1`               | X          |        |
| `libnghttp2-14`           | X          |        |
| `libpcre2-8-0`            | X          |        |
| `libssl3`                 | X          |        |
| `ncurses`                 | X          |        |
| `ncurses-terminfo-base`   | X          |        |
| `openssl-config`          | X          |        |
| `vertical-pod-autoscaler` | X          | X      |
| `wolfi-baselayout`        | X          | X      |
| `zlib`                    | X          |        |
