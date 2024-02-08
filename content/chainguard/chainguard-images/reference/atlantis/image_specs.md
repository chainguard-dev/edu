---
title: "atlantis Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public atlantis Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-02-08 00:18:32
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/atlantis/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/atlantis/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/atlantis/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/atlantis/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **atlantis** Image.

## Variants Compared
The **atlantis** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev          | latest              |
|--------------|---------------------|---------------------|
| Default User | `nonroot`           | `nonroot`           |
| Entrypoint   | `/usr/bin/atlantis` | `/usr/bin/atlantis` |
| CMD          | not specified       | not specified       |
| Workdir      | not specified       | not specified       |
| Has apk?     | yes                 | no                  |
| Has a shell? | yes                 | yes                 |

Check the [tags history page](/chainguard/chainguard-images/reference/atlantis/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                           | latest-dev | latest |
|---------------------------|------------|--------|
| `apk-tools`               | X          |        |
| `atlantis`                | X          | X      |
| `bash`                    | X          |        |
| `busybox`                 | X          | X      |
| `ca-certificates-bundle`  | X          | X      |
| `conftest`                | X          | X      |
| `cue`                     | X          | X      |
| `curl`                    | X          | X      |
| `dumb-init`               | X          | X      |
| `git`                     | X          | X      |
| `git-lfs`                 | X          | X      |
| `glibc`                   | X          | X      |
| `glibc-locale-posix`      | X          | X      |
| `gnupg`                   | X          | X      |
| `ld-linux`                | X          | X      |
| `libbrotlicommon1`        | X          | X      |
| `libbrotlidec1`           | X          | X      |
| `libcap`                  | X          | X      |
| `libcrypt1`               | X          | X      |
| `libcrypto3`              | X          | X      |
| `libcurl-openssl4`        | X          | X      |
| `libexpat1`               | X          | X      |
| `libidn2`                 | X          | X      |
| `libnghttp2-14`           | X          | X      |
| `libpcre2-8-0`            | X          | X      |
| `libpsl`                  | X          | X      |
| `libssl3`                 | X          | X      |
| `libunistring`            | X          | X      |
| `ncurses`                 | X          |        |
| `ncurses-terminfo-base`   | X          |        |
| `openssh-keygen`          | X          | X      |
| `openssh-server`          | X          | X      |
| `openssh-server-config`   | X          | X      |
| `openssl`                 | X          | X      |
| `openssl-config`          | X          | X      |
| `openssl-provider-legacy` | X          | X      |
| `terraform`               | X          | X      |
| `wget`                    | X          |        |
| `wolfi-baselayout`        | X          | X      |
| `zlib`                    | X          | X      |

