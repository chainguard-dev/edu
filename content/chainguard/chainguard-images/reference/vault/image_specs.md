---
title: "vault Image Variants"
type: "article"
description: "Detailed information about the public vault Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "vault"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **vault** Image.

## Variants Compared
The **vault** Chainguard Image currently has 4 public variants: 

- `k8s-latest-dev`
- `k8s-latest`
- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | k8s-latest-dev       | k8s-latest           | latest-dev                      | latest                          |
|--------------|----------------------|----------------------|---------------------------------|---------------------------------|
| Default User | `vault`              | `vault`              | `root`                          | `root`                          |
| Entrypoint   | `/usr/bin/vault-k8s` | `/usr/bin/vault-k8s` | `/usr/bin/docker-entrypoint.sh` | `/usr/bin/docker-entrypoint.sh` |
| CMD          | not specified        | not specified        | `server -dev`                   | `server -dev`                   |
| Workdir      | not specified        | not specified        | not specified                   | not specified                   |
| Has apk?     | yes                  | no                   | yes                             | no                              |
| Has a shell? | yes                  | no                   | yes                             | yes                             |

Check the [tags history page](/chainguard/chainguard-images/reference/vault/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | k8s-latest-dev | k8s-latest | latest-dev | latest |
|--------------------------|----------------|------------|------------|--------|
| `apk-tools`              | X              |            | X          |        |
| `bash`                   | X              |            | X          |        |
| `busybox`                | X              |            | X          | X      |
| `ca-certificates-bundle` | X              | X          | X          | X      |
| `git`                    | X              |            | X          |        |
| `glibc`                  | X              | X          | X          | X      |
| `glibc-locale-posix`     | X              | X          | X          | X      |
| `ld-linux`               | X              | X          | X          | X      |
| `libbrotlicommon1`       | X              |            | X          |        |
| `libbrotlidec1`          | X              |            | X          |        |
| `libcap`                 | X              | X          | X          | X      |
| `libcrypt1`              | X              |            | X          | X      |
| `libcrypto3`             | X              |            | X          |        |
| `libcurl-openssl4`       | X              |            | X          |        |
| `libexpat1`              | X              |            | X          |        |
| `libnghttp2-14`          | X              |            | X          |        |
| `libpcre2-8-0`           | X              |            | X          |        |
| `libssl3`                | X              |            | X          |        |
| `ncurses`                | X              |            | X          |        |
| `ncurses-terminfo-base`  | X              |            | X          |        |
| `openssl-config`         | X              |            | X          |        |
| `vault-k8s`              | X              | X          |            |        |
| `wolfi-baselayout`       | X              | X          | X          | X      |
| `zlib`                   | X              |            | X          |        |
| `dumb-init`              |                |            | X          | X      |
| `libcap-utils`           |                |            | X          | X      |
| `su-exec`                |                |            | X          | X      |
| `vault`                  |                |            | X          | X      |
| `vault-entrypoint`       |                |            | X          | X      |
