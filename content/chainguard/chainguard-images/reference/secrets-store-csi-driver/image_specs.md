---
title: "secrets-store-csi-driver Image Variants"
type: "article"
description: "Detailed information about the public secrets-store-csi-driver Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "secrets-store-csi-driver"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **secrets-store-csi-driver** Image.

## Variants Compared
The **secrets-store-csi-driver** Chainguard Image currently has 4 public variants: 

- `latest-dev`
- `latest`
- `provider-gcp-latest-dev`
- `provider-gcp-latest`

The table has detailed information about each of these variants.

|              | latest-dev                   | latest                       | provider-gcp-latest-dev                          | provider-gcp-latest                              |
|--------------|------------------------------|------------------------------|--------------------------------------------------|--------------------------------------------------|
| Default User | `0`                          | `0`                          | `0`                                              | `0`                                              |
| Entrypoint   | `/usr/bin/secrets-store-csi` | `/usr/bin/secrets-store-csi` | `/usr/bin/secrets-store-csi-driver-provider-gcp` | `/usr/bin/secrets-store-csi-driver-provider-gcp` |
| CMD          | not specified                | not specified                | not specified                                    | not specified                                    |
| Workdir      | not specified                | not specified                | not specified                                    | not specified                                    |
| Has apk?     | yes                          | no                           | yes                                              | no                                               |
| Has a shell? | yes                          | yes                          | yes                                              | no                                               |

Check the [tags history page](/chainguard/chainguard-images/reference/secrets-store-csi-driver/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                         | latest-dev | latest | provider-gcp-latest-dev | provider-gcp-latest |
|-----------------------------------------|------------|--------|-------------------------|---------------------|
| `apk-tools`                             | X          |        | X                       |                     |
| `bash`                                  | X          |        | X                       |                     |
| `busybox`                               | X          | X      | X                       |                     |
| `ca-certificates-bundle`                | X          | X      | X                       | X                   |
| `git`                                   | X          |        | X                       |                     |
| `glibc`                                 | X          | X      | X                       | X                   |
| `glibc-locale-posix`                    | X          | X      | X                       | X                   |
| `ld-linux`                              | X          | X      | X                       | X                   |
| `libblkid`                              | X          | X      |                         |                     |
| `libbrotlicommon1`                      | X          |        | X                       |                     |
| `libbrotlidec1`                         | X          |        | X                       |                     |
| `libcrypt1`                             | X          | X      | X                       |                     |
| `libcrypto3`                            | X          |        | X                       |                     |
| `libcurl-openssl4`                      | X          |        | X                       |                     |
| `libexpat1`                             | X          |        | X                       |                     |
| `libmount`                              | X          | X      |                         |                     |
| `libnghttp2-14`                         | X          |        | X                       |                     |
| `libpcre2-8-0`                          | X          |        | X                       |                     |
| `libssl3`                               | X          |        | X                       |                     |
| `mount`                                 | X          | X      |                         |                     |
| `ncurses`                               | X          |        | X                       |                     |
| `ncurses-terminfo-base`                 | X          |        | X                       |                     |
| `openssl-config`                        | X          |        | X                       |                     |
| `secrets-store-csi-driver`              | X          | X      |                         |                     |
| `wolfi-baselayout`                      | X          | X      | X                       | X                   |
| `zlib`                                  | X          |        | X                       |                     |
| `secrets-store-csi-driver-provider-gcp` |            |        | X                       | X                   |
