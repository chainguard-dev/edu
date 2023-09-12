---
title: "go Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public go Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/go/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/go/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/go/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/go/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **go** Image.

## Variants Compared
The **go** Chainguard Image currently has 3 public variants: 

- `latest-dev`
- `latest`
- `google-cloud-sdk-latest`

The table has detailed information about each of these variants.

|              | latest-dev    | latest        | google-cloud-sdk-latest |
|--------------|---------------|---------------|-------------------------|
| Default User | `0`           | `0`           | `65532`                 |
| Entrypoint   | `/usr/bin/go` | `/usr/bin/go` | not specified           |
| CMD          | `help`        | `help`        | `/usr/bin/gcloud`       |
| Workdir      | not specified | not specified | not specified           |
| Has apk?     | yes           | no            | yes                     |
| Has a shell? | yes           | yes           | yes                     |

Check the [tags history page](/chainguard/chainguard-images/reference/go/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest | google-cloud-sdk-latest |
|--------------------------|------------|--------|-------------------------|
| `apk-tools`              | X          |        | X                       |
| `bash`                   | X          | X      | X                       |
| `binutils`               | X          | X      |                         |
| `binutils-gold`          | X          | X      |                         |
| `build-base`             | X          | X      |                         |
| `busybox`                | X          | X      | X                       |
| `ca-certificates-bundle` | X          | X      | X                       |
| `gcc`                    | X          | X      |                         |
| `git`                    | X          | X      |                         |
| `glibc`                  | X          | X      | X                       |
| `glibc-dev`              | X          | X      |                         |
| `glibc-locale-posix`     | X          | X      | X                       |
| `gmp`                    | X          | X      |                         |
| `go-1.21`                | X          | X      |                         |
| `isl`                    | X          | X      |                         |
| `ld-linux`               | X          | X      | X                       |
| `libatomic`              | X          | X      |                         |
| `libbrotlicommon1`       | X          | X      |                         |
| `libbrotlidec1`          | X          | X      |                         |
| `libcrypt1`              | X          | X      | X                       |
| `libcrypto3`             | X          | X      | X                       |
| `libcurl-openssl4`       | X          | X      |                         |
| `libedit`                | X          | X      |                         |
| `libexpat1`              | X          | X      | X                       |
| `libgcc`                 | X          | X      | X                       |
| `libgo`                  | X          | X      |                         |
| `libgomp`                | X          | X      |                         |
| `libnghttp2-14`          | X          | X      |                         |
| `libpcre2-8-0`           | X          | X      |                         |
| `libssl3`                | X          | X      | X                       |
| `libstdc++`              | X          | X      | X                       |
| `libstdc++-dev`          | X          | X      |                         |
| `linux-headers`          | X          | X      |                         |
| `make`                   | X          | X      |                         |
| `mpc`                    | X          | X      |                         |
| `mpfr`                   | X          | X      |                         |
| `ncurses`                | X          | X      | X                       |
| `ncurses-terminfo-base`  | X          | X      | X                       |
| `nss-db`                 | X          | X      |                         |
| `nss-hesiod`             | X          | X      |                         |
| `openssh`                | X          | X      |                         |
| `openssh-client`         | X          | X      |                         |
| `openssh-keygen`         | X          | X      |                         |
| `openssh-server`         | X          | X      |                         |
| `openssh-sftp-server`    | X          | X      |                         |
| `openssl-config`         | X          | X      | X                       |
| `pkgconf`                | X          | X      |                         |
| `posix-cc-wrappers`      | X          | X      |                         |
| `wolfi-baselayout`       | X          | X      | X                       |
| `zlib`                   | X          | X      | X                       |
| `gdbm`                   |            |        | X                       |
| `google-cloud-sdk`       |            |        | X                       |
| `libbz2-1`               |            |        | X                       |
| `libffi`                 |            |        | X                       |
| `mpdecimal`              |            |        | X                       |
| `python-3.11`            |            |        | X                       |
| `readline`               |            |        | X                       |
| `sqlite-libs`            |            |        | X                       |
| `xz`                     |            |        | X                       |

