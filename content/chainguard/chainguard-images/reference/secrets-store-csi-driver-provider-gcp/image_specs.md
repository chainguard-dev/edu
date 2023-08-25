---
title: "secrets-store-csi-driver-provider-gcp Image Variants"
type: "article"
description: "Detailed information about the public secrets-store-csi-driver-provider-gcp Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "secrets-store-csi-driver-provider-gcp"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **secrets-store-csi-driver-provider-gcp** Image.

## Variants Compared
The **secrets-store-csi-driver-provider-gcp** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                       | latest                                           |
|--------------|--------------------------------------------------|--------------------------------------------------|
| Default User | `root`                                           | `root`                                           |
| Entrypoint   | `/usr/bin/secrets-store-csi-driver-provider-gcp` | `/usr/bin/secrets-store-csi-driver-provider-gcp` |
| CMD          | not specified                                    | not specified                                    |
| Workdir      | not specified                                    | not specified                                    |
| Has apk?     | yes                                              | no                                               |
| Has a shell? | yes                                              | no                                               |

Check the [tags history page](/chainguard/chainguard-images/reference/secrets-store-csi-driver-provider-gcp/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                         | latest-dev | latest |
|-----------------------------------------|------------|--------|
| `apk-tools`                             | X          |        |
| `bash`                                  | X          |        |
| `busybox`                               | X          |        |
| `ca-certificates-bundle`                | X          | X      |
| `git`                                   | X          |        |
| `glibc`                                 | X          | X      |
| `glibc-locale-posix`                    | X          | X      |
| `ld-linux`                              | X          | X      |
| `libbrotlicommon1`                      | X          |        |
| `libbrotlidec1`                         | X          |        |
| `libcrypt1`                             | X          |        |
| `libcrypto3`                            | X          |        |
| `libcurl-openssl4`                      | X          |        |
| `libexpat1`                             | X          |        |
| `libnghttp2-14`                         | X          |        |
| `libpcre2-8-0`                          | X          |        |
| `libssl3`                               | X          |        |
| `ncurses`                               | X          |        |
| `ncurses-terminfo-base`                 | X          |        |
| `openssl-config`                        | X          |        |
| `secrets-store-csi-driver-provider-gcp` | X          | X      |
| `wolfi-baselayout`                      | X          | X      |
| `zlib`                                  | X          |        |

