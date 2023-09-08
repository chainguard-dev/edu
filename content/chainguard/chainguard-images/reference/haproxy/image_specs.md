---
title: "haproxy Image Variants"
type: "article"
description: "Detailed information about the public haproxy Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "haproxy"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **haproxy** Image.

## Variants Compared
The **haproxy** Chainguard Image currently has 3 public variants: 

- `ingress-latest-dev`
- `ingress-latest`
- `latest`

The table has detailed information about each of these variants.

|              | ingress-latest-dev                        | ingress-latest                            | latest                                |
|--------------|-------------------------------------------|-------------------------------------------|---------------------------------------|
| Default User | `65532`                                   | `65532`                                   | `65532`                               |
| Entrypoint   | `/usr/bin/dumb-init -- /usr/bin/start.sh` | `/usr/bin/dumb-init -- /usr/bin/start.sh` | `/usr/local/bin/docker-entrypoint.sh` |
| CMD          | not specified                             | not specified                             | not specified                         |
| Workdir      | not specified                             | not specified                             | not specified                         |
| Has apk?     | yes                                       | no                                        | no                                    |
| Has a shell? | yes                                       | yes                                       | yes                                   |

Check the [tags history page](/chainguard/chainguard-images/reference/haproxy/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | ingress-latest-dev | ingress-latest | latest |
|--------------------------|--------------------|----------------|--------|
| `apk-tools`              | X                  |                |        |
| `bash`                   | X                  |                |        |
| `busybox`                | X                  | X              | X      |
| `ca-certificates-bundle` | X                  | X              | X      |
| `dumb-init`              | X                  | X              |        |
| `git`                    | X                  |                |        |
| `glibc`                  | X                  | X              | X      |
| `glibc-locale-posix`     | X                  | X              | X      |
| `haproxy`                | X                  | X              | X      |
| `haproxy-ingress`        | X                  | X              |        |
| `haproxy-ingress-compat` | X                  | X              |        |
| `ld-linux`               | X                  | X              | X      |
| `libbrotlicommon1`       | X                  |                |        |
| `libbrotlidec1`          | X                  |                |        |
| `libcrypt1`              | X                  | X              | X      |
| `libcrypto3`             | X                  | X              | X      |
| `libcurl-openssl4`       | X                  |                |        |
| `libexpat1`              | X                  |                |        |
| `libgcc`                 | X                  | X              | X      |
| `libnghttp2-14`          | X                  |                |        |
| `libpcre2-8-0`           | X                  | X              | X      |
| `libpcre2-posix-3`       | X                  | X              | X      |
| `libssl3`                | X                  | X              | X      |
| `lua-json4`              | X                  | X              |        |
| `ncurses`                | X                  |                |        |
| `ncurses-terminfo-base`  | X                  |                |        |
| `openssl-config`         | X                  | X              | X      |
| `wolfi-baselayout`       | X                  | X              | X      |
| `zlib`                   | X                  |                |        |
| `dataplaneapi`           |                    |                | X      |
| `haproxy-oci-entrypoint` |                    |                | X      |
