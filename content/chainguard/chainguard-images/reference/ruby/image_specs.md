---
title: "ruby Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public ruby Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-01-15 00:20:04
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/ruby/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/ruby/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/ruby/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/ruby/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **ruby** Image.

## Variants Compared
The **ruby** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev      | latest          |
|--------------|-----------------|-----------------|
| Default User | `nonroot`       | `nonroot`       |
| Entrypoint   | `/usr/bin/ruby` | `/usr/bin/ruby` |
| CMD          | `--version`     | `--version`     |
| Workdir      | `/work`         | `/work`         |
| Has apk?     | yes             | no              |
| Has a shell? | yes             | no              |

Check the [tags history page](/chainguard/chainguard-images/reference/ruby/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `binutils`               | X          |        |
| `build-base`             | X          |        |
| `busybox`                | X          |        |
| `ca-certificates-bundle` | X          | X      |
| `gcc`                    | X          |        |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-dev`              | X          |        |
| `glibc-locale-posix`     | X          | X      |
| `gmp`                    | X          |        |
| `isl`                    | X          |        |
| `ld-linux`               | X          | X      |
| `libatomic`              | X          |        |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          | X      |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          |        |
| `libffi`                 | X          | X      |
| `libgcc`                 | X          | X      |
| `libgo`                  | X          |        |
| `libgomp`                | X          |        |
| `libidn2`                | X          |        |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libpsl`                 | X          |        |
| `libssl3`                | X          | X      |
| `libstdc++`              | X          |        |
| `libstdc++-dev`          | X          |        |
| `libunistring`           | X          |        |
| `linux-headers`          | X          |        |
| `make`                   | X          |        |
| `mpc`                    | X          |        |
| `mpfr`                   | X          |        |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `nss-db`                 | X          |        |
| `nss-hesiod`             | X          |        |
| `openssl-config`         | X          | X      |
| `pkgconf`                | X          |        |
| `posix-cc-wrappers`      | X          |        |
| `ruby-3.3`               | X          | X      |
| `ruby-3.3-dev`           | X          |        |
| `ruby3.3-bundler`        | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `yaml`                   | X          | X      |
| `zlib`                   | X          | X      |

