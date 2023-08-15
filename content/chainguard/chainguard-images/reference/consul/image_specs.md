---
title: "consul Image Variants"
type: "article"
description: "Detailed information about the public consul Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "consul"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **consul** Image.

## Variants Compared
The **consul** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                      | latest                          |
|--------------|---------------------------------|---------------------------------|
| Default User | `root`                          | `root`                          |
| Entrypoint   | `/usr/bin/docker-entrypoint.sh` | `/usr/bin/docker-entrypoint.sh` |
| CMD          | `agent -dev -client 0.0.0.0`    | `agent -dev -client 0.0.0.0`    |
| Workdir      | not specified                   | not specified                   |
| Has apk?     | yes                             | no                              |
| Has a shell? | yes                             | yes                             |

Check the [tags history page](/chainguard/chainguard-images/reference/consul/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                | latest-dev | latest |
|--------------------------------|------------|--------|
| `apk-tools`                    | X          |        |
| `bash`                         | X          |        |
| `busybox`                      | X          | X      |
| `ca-certificates-bundle`       | X          | X      |
| `consul-1.16`                  | X          | X      |
| `consul-oci-entrypoint`        | X          | X      |
| `consul-oci-entrypoint-compat` | X          | X      |
| `curl`                         | X          | X      |
| `dumb-init`                    | X          | X      |
| `git`                          | X          |        |
| `glibc`                        | X          | X      |
| `glibc-locale-posix`           | X          | X      |
| `ld-linux`                     | X          | X      |
| `libbrotlicommon1`             | X          | X      |
| `libbrotlidec1`                | X          | X      |
| `libcap`                       | X          | X      |
| `libcap-utils`                 | X          | X      |
| `libcrypt1`                    | X          | X      |
| `libcrypto3`                   | X          | X      |
| `libcurl-openssl4`             | X          | X      |
| `libexpat1`                    | X          |        |
| `libnghttp2-14`                | X          | X      |
| `libpcre2-8-0`                 | X          |        |
| `libssl3`                      | X          | X      |
| `ncurses`                      | X          |        |
| `ncurses-terminfo-base`        | X          |        |
| `openssl-config`               | X          | X      |
| `su-exec`                      | X          | X      |
| `wolfi-baselayout`             | X          | X      |
| `zlib`                         | X          | X      |
