---
title: "dynamic-localpv-provisioner Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public dynamic-localpv-provisioner Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/dynamic-localpv-provisioner/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/dynamic-localpv-provisioner/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/dynamic-localpv-provisioner/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/dynamic-localpv-provisioner/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **dynamic-localpv-provisioner** Image.

## Variants Compared
The **dynamic-localpv-provisioner** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                     | latest                         |
|--------------|--------------------------------|--------------------------------|
| Default User | `nonroot`                      | `nonroot`                      |
| Entrypoint   | `/usr/bin/provisioner-localpv` | `/usr/bin/provisioner-localpv` |
| CMD          | not specified                  | not specified                  |
| Workdir      | not specified                  | not specified                  |
| Has apk?     | yes                            | no                             |
| Has a shell? | yes                            | yes                            |

Check the [tags history page](/chainguard/chainguard-images/reference/dynamic-localpv-provisioner/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                               | latest-dev | latest |
|-------------------------------|------------|--------|
| `apk-tools`                   | X          |        |
| `bash`                        | X          | X      |
| `busybox`                     | X          | X      |
| `ca-certificates-bundle`      | X          | X      |
| `dynamic-localpv-provisioner` | X          | X      |
| `git`                         | X          |        |
| `glibc`                       | X          | X      |
| `glibc-locale-posix`          | X          | X      |
| `iproute2`                    | X          | X      |
| `iptables`                    | X          | X      |
| `ld-linux`                    | X          | X      |
| `libbrotlicommon1`            | X          |        |
| `libbrotlidec1`               | X          |        |
| `libbz2-1`                    | X          | X      |
| `libcrypt1`                   | X          | X      |
| `libcrypto3`                  | X          |        |
| `libcurl-openssl4`            | X          |        |
| `libelf`                      | X          | X      |
| `libexpat1`                   | X          |        |
| `libmnl`                      | X          | X      |
| `libnftnl`                    | X          | X      |
| `libnghttp2-14`               | X          |        |
| `libpcre2-8-0`                | X          |        |
| `libproc-2-0`                 | X          | X      |
| `libssl3`                     | X          |        |
| `mii-tool`                    | X          | X      |
| `ncurses`                     | X          | X      |
| `ncurses-terminfo-base`       | X          | X      |
| `net-tools`                   | X          | X      |
| `openssl-config`              | X          |        |
| `procps`                      | X          | X      |
| `wolfi-baselayout`            | X          | X      |
| `xz`                          | X          | X      |
| `zlib`                        | X          | X      |

