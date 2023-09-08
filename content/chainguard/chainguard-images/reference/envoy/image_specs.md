---
title: "envoy Image Variants"
type: "article"
description: "Detailed information about the public envoy Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "envoy"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **envoy** Image.

## Variants Compared
The **envoy** Chainguard Image currently has 3 public variants: 

- `latest`
- `ratelimit-latest-dev`
- `ratelimit-latest`

The table has detailed information about each of these variants.

|              | latest                                    | ratelimit-latest-dev | ratelimit-latest     |
|--------------|-------------------------------------------|----------------------|----------------------|
| Default User | `65532`                                   | `65532`              | `65532`              |
| Entrypoint   | `/var/lib/envoy/init/envoy-entrypoint.sh` | `/usr/bin/ratelimit` | `/usr/bin/ratelimit` |
| CMD          | not specified                             | not specified        | not specified        |
| Workdir      | not specified                             | not specified        | not specified        |
| Has apk?     | no                                        | yes                  | no                   |
| Has a shell? | yes                                       | yes                  | no                   |

Check the [tags history page](/chainguard/chainguard-images/reference/envoy/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest | ratelimit-latest-dev | ratelimit-latest |
|--------------------------|--------|----------------------|------------------|
| `busybox`                | X      | X                    |                  |
| `ca-certificates-bundle` | X      | X                    | X                |
| `envoy`                  | X      |                      |                  |
| `envoy-config`           | X      |                      |                  |
| `envoy-oci-entrypoint`   | X      |                      |                  |
| `glibc`                  | X      | X                    | X                |
| `glibc-locale-posix`     | X      | X                    | X                |
| `ld-linux`               | X      | X                    | X                |
| `libcrypt1`              | X      | X                    |                  |
| `su-exec`                | X      |                      |                  |
| `wolfi-baselayout`       | X      | X                    | X                |
| `apk-tools`              |        | X                    |                  |
| `bash`                   |        | X                    |                  |
| `envoy-ratelimit`        |        | X                    | X                |
| `envoy-ratelimit-compat` |        | X                    | X                |
| `git`                    |        | X                    |                  |
| `libbrotlicommon1`       |        | X                    |                  |
| `libbrotlidec1`          |        | X                    |                  |
| `libcrypto3`             |        | X                    |                  |
| `libcurl-openssl4`       |        | X                    |                  |
| `libexpat1`              |        | X                    |                  |
| `libnghttp2-14`          |        | X                    |                  |
| `libpcre2-8-0`           |        | X                    |                  |
| `libssl3`                |        | X                    |                  |
| `ncurses`                |        | X                    |                  |
| `ncurses-terminfo-base`  |        | X                    |                  |
| `openssl-config`         |        | X                    |                  |
| `zlib`                   |        | X                    |                  |
