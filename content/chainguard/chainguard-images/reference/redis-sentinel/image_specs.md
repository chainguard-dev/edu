---
title: "redis-sentinel Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public redis-sentinel Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-01-03 00:37:41
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/redis-sentinel/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/redis-sentinel/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/redis-sentinel/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/redis-sentinel/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **redis-sentinel** Image.

## Variants Compared
The **redis-sentinel** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                                              |
|--------------|-----------------------------------------------------|
| Default User | `redis`                                             |
| Entrypoint   | `/opt/bitnami/scripts/redis-sentinel/entrypoint.sh` |
| CMD          | `/opt/bitnami/scripts/redis-sentinel/run.sh`        |
| Workdir      | not specified                                       |
| Has apk?     | no                                                  |
| Has a shell? | yes                                                 |

Check the [tags history page](/chainguard/chainguard-images/reference/redis-sentinel/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                             | latest |
|-----------------------------|--------|
| `bash`                      | X      |
| `busybox`                   | X      |
| `ca-certificates-bundle`    | X      |
| `coreutils`                 | X      |
| `glibc`                     | X      |
| `glibc-locale-posix`        | X      |
| `ld-linux`                  | X      |
| `libacl1`                   | X      |
| `libattr1`                  | X      |
| `libcrypt1`                 | X      |
| `libcrypto3`                | X      |
| `libssl3`                   | X      |
| `ncurses`                   | X      |
| `ncurses-terminfo-base`     | X      |
| `openssl-config`            | X      |
| `posix-libc-utils`          | X      |
| `redis-6.2`                 | X      |
| `redis-cli-6.2`             | X      |
| `redis-sentinel-6.2-compat` | X      |
| `wolfi-baselayout`          | X      |

