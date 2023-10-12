---
title: "stakater-reloader Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public stakater-reloader Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/stakater-reloader/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/stakater-reloader/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/stakater-reloader/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/stakater-reloader/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **stakater-reloader** Image.

## Variants Compared
The **stakater-reloader** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev         | latest             |
|--------------|--------------------|--------------------|
| Default User | `nonroot`          | `nonroot`          |
| Entrypoint   | `/usr/bin/manager` | `/usr/bin/manager` |
| CMD          | not specified      | not specified      |
| Workdir      | not specified      | not specified      |
| Has apk?     | yes                | no                 |
| Has a shell? | yes                | yes                |

Check the [tags history page](/chainguard/chainguard-images/reference/stakater-reloader/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                            | latest-dev | latest |
|----------------------------|------------|--------|
| `apk-tools`                | X          |        |
| `bash`                     | X          |        |
| `busybox`                  | X          | X      |
| `ca-certificates-bundle`   | X          | X      |
| `git`                      | X          |        |
| `glibc`                    | X          | X      |
| `glibc-locale-posix`       | X          | X      |
| `ld-linux`                 | X          | X      |
| `libbrotlicommon1`         | X          |        |
| `libbrotlidec1`            | X          |        |
| `libcrypt1`                | X          | X      |
| `libcrypto3`               | X          |        |
| `libcurl-rustls4`          | X          |        |
| `libexpat1`                | X          |        |
| `libgcc`                   | X          |        |
| `libnghttp2-14`            | X          |        |
| `libpcre2-8-0`             | X          |        |
| `libssl3`                  | X          |        |
| `ncurses`                  | X          |        |
| `ncurses-terminfo-base`    | X          |        |
| `openssl-config`           | X          |        |
| `stakater-reloader`        | X          | X      |
| `stakater-reloader-compat` | X          | X      |
| `wolfi-baselayout`         | X          | X      |
| `zlib`                     | X          |        |

