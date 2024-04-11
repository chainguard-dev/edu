---
title: "rstudio Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public rstudio Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/rstudio/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/rstudio/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/rstudio/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/rstudio/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **rstudio** Image.

|              | latest-dev         | latest             |
|--------------|--------------------|--------------------|
| Default User | `rstudio-server`   | `rstudio-server`   |
| Entrypoint   | `/usr/bin/rserver` | `/usr/bin/rserver` |
| CMD          | not specified      | not specified      |
| Workdir      | not specified      | not specified      |
| Has apk?     | yes                | no                 |
| Has a shell? | yes                | yes                |

Check the [tags history page](/chainguard/chainguard-images/reference/rstudio/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `R`                      | X          | X      |
| `R-dev`                  | X          | X      |
| `R-doc`                  | X          | X      |
| `apk-tools`              | X          |        |
| `bash`                   | X          | X      |
| `binutils`               | X          | X      |
| `busybox`                | X          | X      |
| `bzip2-dev`              | X          | X      |
| `c-ares`                 | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `cairo`                  | X          | X      |
| `chainguard-baselayout`  | X          | X      |
| `curl`                   | X          | X      |
| `curl-dev`               | X          | X      |
| `esbuild`                | X          | X      |
| `fontconfig`             | X          | X      |
| `fontconfig-config`      | X          | X      |
| `freetype`               | X          | X      |
| `fribidi`                | X          | X      |
| `gcc`                    | X          | X      |
| `gfortran`               | X          | X      |
| `git`                    | X          |        |
| `glib`                   | X          | X      |
| `glibc`                  | X          | X      |
| `glibc-dev`              | X          | X      |
| `glibc-iconv`            | X          | X      |
| `glibc-locale-en`        | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `glibc-locales`          | X          | X      |
| `gmp`                    | X          | X      |
| `gnu-libiconv`           | X          | X      |
| `graphite2`              | X          | X      |
| `harfbuzz`               | X          | X      |
| `icu`                    | X          | X      |
| `icu-dev`                | X          | X      |
| `isl`                    | X          | X      |
| `ld-linux`               | X          | X      |
| `libatomic`              | X          | X      |
| `libblkid`               | X          | X      |
| `libbrotlicommon1`       | X          | X      |
| `libbrotlidec1`          | X          | X      |
| `libbrotlienc1`          | X          | X      |
| `libbz2-1`               | X          | X      |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          | X      |
| `libcurl-openssl4`       | X          | X      |
| `libexpat1`              | X          | X      |
| `libffi`                 | X          | X      |
| `libfontconfig1`         | X          | X      |
| `libgcc`                 | X          | X      |
| `libgfortran`            | X          | X      |
| `libgo`                  | X          | X      |
| `libgomp`                | X          | X      |
| `libice`                 | X          | X      |
| `libidn2`                | X          | X      |
| `libjpeg-turbo`          | X          | X      |
| `liblapack`              | X          | X      |
| `liblapacke`             | X          | X      |
| `libmount`               | X          | X      |
| `libnghttp2-14`          | X          | X      |
| `libpcre2-8-0`           | X          | X      |
| `libpng`                 | X          | X      |
| `libpsl`                 | X          | X      |
| `libsm`                  | X          | X      |
| `libssl3`                | X          | X      |
| `libstdc++`              | X          | X      |
| `libstdc++-dev`          | X          | X      |
| `libunistring`           | X          | X      |
| `libuuid`                | X          | X      |
| `libuv`                  | X          | X      |
| `libwebp`                | X          | X      |
| `libx11`                 | X          | X      |
| `libxau`                 | X          | X      |
| `libxcb`                 | X          | X      |
| `libxcrypt`              | X          | X      |
| `libxcrypt-dev`          | X          | X      |
| `libxdmcp`               | X          | X      |
| `libxext`                | X          | X      |
| `libxft`                 | X          | X      |
| `libxml2`                | X          | X      |
| `libxml2-dev`            | X          | X      |
| `libxml2-utils`          | X          | X      |
| `libxmu`                 | X          | X      |
| `libxrender`             | X          | X      |
| `libxt`                  | X          | X      |
| `libzstd1`               | X          | X      |
| `linux-headers`          | X          | X      |
| `linux-pam`              | X          | X      |
| `make`                   | X          | X      |
| `mpc`                    | X          | X      |
| `mpfr`                   | X          | X      |
| `ncurses`                | X          | X      |
| `ncurses-terminfo-base`  | X          | X      |
| `nodejs-20`              | X          | X      |
| `nss-db`                 | X          | X      |
| `nss-hesiod`             | X          | X      |
| `openblas`               | X          | X      |
| `openblas-dev`           | X          | X      |
| `openssl-config`         | X          | X      |
| `openssl-dev`            | X          | X      |
| `pango`                  | X          | X      |
| `pcre`                   | X          | X      |
| `pcre-dev`               | X          | X      |
| `pixman`                 | X          | X      |
| `posix-cc-wrappers`      | X          | X      |
| `readline`               | X          | X      |
| `rstudio`                | X          | X      |
| `sqlite-libs`            | X          | X      |
| `tcl`                    | X          | X      |
| `tiff`                   | X          | X      |
| `tk`                     | X          | X      |
| `tzdata`                 | X          | X      |
| `wget`                   | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `xz`                     | X          | X      |
| `xz-dev`                 | X          | X      |
| `yaml-cpp`               | X          | X      |
| `zlib`                   | X          | X      |
| `zlib-dev`               | X          | X      |

