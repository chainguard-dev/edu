---
title: "rabbitmq Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public rabbitmq Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/rabbitmq/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/rabbitmq/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/rabbitmq/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/rabbitmq/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **rabbitmq** Image.

## Variants Compared
The **rabbitmq** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                      |
|--------------|-----------------------------|
| Default User | `999`                       |
| Entrypoint   | `/usr/sbin/rabbitmq-server` |
| CMD          | not specified               |
| Workdir      | `/var/lib/rabbitmq`         |
| Has apk?     | no                          |
| Has a shell? | yes                         |

Check the [tags history page](/chainguard/chainguard-images/reference/rabbitmq/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `bash`                   | X      |
| `busybox`                | X      |
| `ca-certificates-bundle` | X      |
| `erlang-26`              | X      |
| `glibc`                  | X      |
| `glibc-locale-en`        | X      |
| `glibc-locale-posix`     | X      |
| `ld-linux`               | X      |
| `libcrypt1`              | X      |
| `libcrypto3`             | X      |
| `libgcc`                 | X      |
| `libstdc++`              | X      |
| `ncurses`                | X      |
| `ncurses-terminfo-base`  | X      |
| `openssl-config`         | X      |
| `rabbitmq-server`        | X      |
| `tzdata`                 | X      |
| `wolfi-baselayout`       | X      |
| `zlib`                   | X      |

