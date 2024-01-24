---
title: "dotnet-sdk Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public dotnet-sdk Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-01-24 00:37:09
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/dotnet-sdk/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/dotnet-sdk/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/dotnet-sdk/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/dotnet-sdk/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **dotnet-sdk** Image.

## Variants Compared
The **dotnet-sdk** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev    | latest        |
|--------------|---------------|---------------|
| Default User | `nonroot`     | `nonroot`     |
| Entrypoint   | not specified | not specified |
| CMD          | `/bin/sh -l`  | `/bin/sh -l`  |
| Workdir      | not specified | not specified |
| Has apk?     | yes           | no            |
| Has a shell? | yes           | yes           |

Check the [tags history page](/chainguard/chainguard-images/reference/dotnet-sdk/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                            | latest-dev | latest |
|----------------------------|------------|--------|
| `apk-tools`                | X          |        |
| `aspnet-8-runtime`         | X          | X      |
| `aspnet-8-runtime-default` | X          | X      |
| `aspnet-8-targeting-pack`  | X          | X      |
| `bash`                     | X          |        |
| `busybox`                  | X          | X      |
| `ca-certificates-bundle`   | X          | X      |
| `dotnet-8`                 | X          | X      |
| `dotnet-8-runtime`         | X          | X      |
| `dotnet-8-runtime-default` | X          | X      |
| `dotnet-8-sdk`             | X          | X      |
| `dotnet-8-sdk-default`     | X          | X      |
| `dotnet-8-targeting-pack`  | X          | X      |
| `git`                      | X          |        |
| `glibc`                    | X          | X      |
| `glibc-locale-posix`       | X          | X      |
| `icu`                      | X          | X      |
| `ld-linux`                 | X          | X      |
| `libbrotlicommon1`         | X          |        |
| `libbrotlidec1`            | X          |        |
| `libcrypt1`                | X          | X      |
| `libcrypto3`               | X          | X      |
| `libcurl-openssl4`         | X          |        |
| `libexpat1`                | X          |        |
| `libgcc`                   | X          | X      |
| `libidn2`                  | X          |        |
| `libnghttp2-14`            | X          |        |
| `libpcre2-8-0`             | X          |        |
| `libpsl`                   | X          |        |
| `libssl3`                  | X          | X      |
| `libstdc++`                | X          | X      |
| `libunistring`             | X          |        |
| `lttng-ust`                | X          | X      |
| `ncurses`                  | X          |        |
| `ncurses-terminfo-base`    | X          |        |
| `openssl-config`           | X          | X      |
| `wolfi-baselayout`         | X          | X      |
| `zlib`                     | X          | X      |

