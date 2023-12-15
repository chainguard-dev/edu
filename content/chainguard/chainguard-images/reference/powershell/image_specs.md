---
title: "powershell Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public powershell Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-12-15 00:37:05
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
The **powershell** Chainguard Image currently has 2 public variants: 

- `latest-root`
- `latest`

The table has detailed information about each of these variants.

|              | latest-root     | latest          |
|--------------|-----------------|-----------------|
| Default User | `root`          | `nonroot`       |
| Entrypoint   | `/usr/bin/pwsh` | `/usr/bin/pwsh` |
| CMD          | not specified   | not specified   |
| Workdir      | not specified   | not specified   |
| Has apk?     | no              | no              |
| Has a shell? | yes             | yes             |

Check the [tags history page](/chainguard/chainguard-images/reference/powershell/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-root | latest |
|--------------------------|-------------|--------|
| `aspnet-8-runtime`       | X           | X      |
| `busybox`                | X           | X      |
| `ca-certificates-bundle` | X           | X      |
| `dotnet-8`               | X           | X      |
| `dotnet-8-runtime`       | X           | X      |
| `glibc`                  | X           | X      |
| `glibc-locale-posix`     | X           | X      |
| `icu`                    | X           | X      |
| `ld-linux`               | X           | X      |
| `libcrypt1`              | X           | X      |
| `libcrypto3`             | X           | X      |
| `libgcc`                 | X           | X      |
| `libpsl-native`          | X           | X      |
| `libssl3`                | X           | X      |
| `libstdc++`              | X           | X      |
| `lttng-ust`              | X           | X      |
| `ncurses-terminfo-base`  | X           | X      |
| `openssl-config`         | X           | X      |
| `powershell`             | X           | X      |
| `wolfi-baselayout`       | X           | X      |
| `zlib`                   | X           | X      |

