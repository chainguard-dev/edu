---
title: "gcc-glibc Image Variants"
type: "article"
description: "Detailed information about the public gcc-glibc Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "gcc-glibc"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **gcc-glibc** Image.

## Variants Compared
The **gcc-glibc** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest         |
|--------------|----------------|
| Default User | `root`         |
| Entrypoint   | `/usr/bin/gcc` |
| CMD          | `--help`       |
| Workdir      | `/work`        |
| Has apk?     | no             |
| Has a shell? | yes            |

Check the [tags history page](/chainguard/chainguard-images/reference/gcc-glibc/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `binutils`               | X      |
| `build-base`             | X      |
| `busybox`                | X      |
| `ca-certificates-bundle` | X      |
| `gcc`                    | X      |
| `glibc`                  | X      |
| `glibc-dev`              | X      |
| `glibc-locale-posix`     | X      |
| `gmp`                    | X      |
| `isl`                    | X      |
| `ld-linux`               | X      |
| `libatomic`              | X      |
| `libcrypt1`              | X      |
| `libgcc`                 | X      |
| `libgo`                  | X      |
| `libgomp`                | X      |
| `libstdc++`              | X      |
| `libstdc++-dev`          | X      |
| `linux-headers`          | X      |
| `make`                   | X      |
| `mpc`                    | X      |
| `mpfr`                   | X      |
| `nss-db`                 | X      |
| `nss-hesiod`             | X      |
| `pkgconf`                | X      |
| `posix-cc-wrappers`      | X      |
| `wolfi-baselayout`       | X      |
| `zlib`                   | X      |

