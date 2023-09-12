---
title: "memcached Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public memcached Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/memcached/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/memcached/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/memcached/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/memcached/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **memcached** Image.

## Variants Compared
The **memcached** Chainguard Image currently has 2 public variants: 

- `exporter-latest`
- `latest`

The table has detailed information about each of these variants.

|              | exporter-latest               | latest        |
|--------------|-------------------------------|---------------|
| Default User | `65532`                       | `65532`       |
| Entrypoint   | `/usr/bin/memcached_exporter` | `memcached`   |
| CMD          | not specified                 | not specified |
| Workdir      | not specified                 | not specified |
| Has apk?     | no                            | no            |
| Has a shell? | no                            | no            |

Check the [tags history page](/chainguard/chainguard-images/reference/memcached/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | exporter-latest | latest |
|--------------------------|-----------------|--------|
| `ca-certificates-bundle` | X               | X      |
| `glibc`                  | X               | X      |
| `glibc-locale-posix`     | X               | X      |
| `ld-linux`               | X               | X      |
| `memcached-exporter`     | X               |        |
| `wolfi-baselayout`       | X               | X      |
| `cyrus-sasl`             |                 | X      |
| `gdbm`                   |                 | X      |
| `heimdal`                |                 | X      |
| `libcrypt1`              |                 | X      |
| `libcrypto3`             |                 | X      |
| `libevent`               |                 | X      |
| `libseccomp`             |                 | X      |
| `libssl3`                |                 | X      |
| `memcached`              |                 | X      |
| `ncurses`                |                 | X      |
| `ncurses-terminfo-base`  |                 | X      |
| `openssl-config`         |                 | X      |
| `readline`               |                 | X      |
| `sqlite-libs`            |                 | X      |

