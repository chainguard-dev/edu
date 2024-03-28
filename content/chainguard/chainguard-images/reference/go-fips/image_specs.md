---
title: "go-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public go-fips Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-03-28 00:50:32
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/go-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/go-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/go-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/go-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **go-fips** Image.

|              | latest-dev    | latest        |
|--------------|---------------|---------------|
| Default User | `root`        | `root`        |
| Entrypoint   | `/usr/bin/go` | `/usr/bin/go` |
| CMD          | `help`        | `help`        |
| Workdir      | not specified | not specified |
| Has apk?     | yes           | no            |
| Has a shell? | yes           | yes           |

Check the [tags history page](/chainguard/chainguard-images/reference/go-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                               | latest-dev | latest |
|-------------------------------|------------|--------|
| `apk-tools`                   | X          |        |
| `bash`                        | X          | X      |
| `binutils`                    | X          | X      |
| `binutils-gold`               | X          | X      |
| `build-base`                  | X          | X      |
| `busybox`                     | X          | X      |
| `ca-certificates-bundle`      | X          | X      |
| `chainguard-baselayout`       | X          | X      |
| `gcc`                         | X          | X      |
| `git`                         | X          | X      |
| `glibc`                       | X          | X      |
| `glibc-dev`                   | X          | X      |
| `glibc-locale-posix`          | X          | X      |
| `gmp`                         | X          | X      |
| `go-fips-1.22`                | X          | X      |
| `isl`                         | X          | X      |
| `ld-linux`                    | X          | X      |
| `libatomic`                   | X          | X      |
| `libbrotlicommon1`            | X          | X      |
| `libbrotlidec1`               | X          | X      |
| `libcrypt1`                   | X          | X      |
| `libcrypto3`                  | X          | X      |
| `libcurl-openssl4`            | X          | X      |
| `libedit`                     | X          | X      |
| `libexpat1`                   | X          | X      |
| `libgcc`                      | X          | X      |
| `libgo`                       | X          | X      |
| `libgomp`                     | X          | X      |
| `libidn2`                     | X          | X      |
| `libnghttp2-14`               | X          | X      |
| `libpcre2-8-0`                | X          | X      |
| `libpsl`                      | X          | X      |
| `libssl3`                     | X          | X      |
| `libstdc++`                   | X          | X      |
| `libstdc++-dev`               | X          | X      |
| `libunistring`                | X          | X      |
| `libxcrypt`                   | X          | X      |
| `libxcrypt-dev`               | X          | X      |
| `linux-headers`               | X          | X      |
| `make`                        | X          | X      |
| `mpc`                         | X          | X      |
| `mpfr`                        | X          | X      |
| `ncurses`                     | X          | X      |
| `ncurses-terminfo-base`       | X          | X      |
| `nss-db`                      | X          | X      |
| `nss-hesiod`                  | X          | X      |
| `openssh`                     | X          | X      |
| `openssh-client`              | X          | X      |
| `openssh-keygen`              | X          | X      |
| `openssh-server`              | X          | X      |
| `openssh-server-config`       | X          | X      |
| `openssh-sftp-server`         | X          | X      |
| `openssl-config-fipshardened` | X          | X      |
| `openssl-provider-fips`       | X          | X      |
| `pkgconf`                     | X          | X      |
| `posix-cc-wrappers`           | X          | X      |
| `wget`                        | X          |        |
| `wolfi-baselayout`            | X          | X      |
| `zlib`                        | X          | X      |

