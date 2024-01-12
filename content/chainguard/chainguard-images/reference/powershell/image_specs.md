---
title: "powershell Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public powershell Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-01-12 00:39:30
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/powershell/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/powershell/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/powershell/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/powershell/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **powershell** Image.

## Variants Compared
The **powershell** Chainguard Image currently has 3 public variants: 

- `latest-dev`
- `latest-root`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev      | latest-root     | latest          |
|--------------|-----------------|-----------------|-----------------|
| Default User | `nonroot`       | `root`          | `nonroot`       |
| Entrypoint   | `/usr/bin/pwsh` | `/usr/bin/pwsh` | `/usr/bin/pwsh` |
| CMD          | not specified   | not specified   | not specified   |
| Workdir      | not specified   | not specified   | not specified   |
| Has apk?     | yes             | no              | no              |
| Has a shell? | yes             | yes             | yes             |

Check the [tags history page](/chainguard/chainguard-images/reference/powershell/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest-root | latest |
|--------------------------|------------|-------------|--------|
| `apk-tools`              | X          |             |        |
| `aspnet-8-runtime`       | X          | X           | X      |
| `bash`                   | X          |             |        |
| `busybox`                | X          | X           | X      |
| `ca-certificates-bundle` | X          | X           | X      |
| `dotnet-8`               | X          | X           | X      |
| `dotnet-8-runtime`       | X          | X           | X      |
| `git`                    | X          |             |        |
| `glibc`                  | X          | X           | X      |
| `glibc-locale-posix`     | X          | X           | X      |
| `icu`                    | X          | X           | X      |
| `ld-linux`               | X          | X           | X      |
| `libbrotlicommon1`       | X          |             |        |
| `libbrotlidec1`          | X          |             |        |
| `libcrypt1`              | X          | X           | X      |
| `libcrypto3`             | X          | X           | X      |
| `libcurl-openssl4`       | X          |             |        |
| `libexpat1`              | X          |             |        |
| `libgcc`                 | X          | X           | X      |
| `libidn2`                | X          |             |        |
| `libnghttp2-14`          | X          |             |        |
| `libpcre2-8-0`           | X          |             |        |
| `libpsl`                 | X          |             |        |
| `libpsl-native`          | X          | X           | X      |
| `libssl3`                | X          | X           | X      |
| `libstdc++`              | X          | X           | X      |
| `libunistring`           | X          |             |        |
| `lttng-ust`              | X          | X           | X      |
| `ncurses`                | X          |             |        |
| `ncurses-terminfo-base`  | X          | X           | X      |
| `openssl-config`         | X          | X           | X      |
| `powershell`             | X          | X           | X      |
| `wolfi-baselayout`       | X          | X           | X      |
| `zlib`                   | X          | X           | X      |

