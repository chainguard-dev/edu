---
title: "rust Image Variants"
type: "article"
description: "Detailed information about the public rust Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "rust"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **rust** Image.

## Variants Compared
The **rust** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev       | latest           |
|--------------|------------------|------------------|
| Default User | `nonroot`        | `nonroot`        |
| Entrypoint   | `/usr/bin/rustc` | `/usr/bin/rustc` |
| CMD          | `--help`         | `--help`         |
| Workdir      | `/work`          | `/work`          |
| Has apk?     | yes              | no               |
| Has a shell? | yes              | yes              |

Check the [tags history page](/chainguard/chainguard-images/reference/rust/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `binutils`               | X          | X      |
| `build-base`             | X          | X      |
| `busybox`                | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `gcc`                    | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-dev`              | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `gmp`                    | X          | X      |
| `isl`                    | X          | X      |
| `ld-linux`               | X          | X      |
| `libLLVM-15`             | X          | X      |
| `libatomic`              | X          | X      |
| `libbrotlicommon1`       | X          | X      |
| `libbrotlidec1`          | X          | X      |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          | X      |
| `libcurl-openssl4`       | X          | X      |
| `libexpat1`              | X          |        |
| `libffi`                 | X          | X      |
| `libgcc`                 | X          | X      |
| `libgo`                  | X          | X      |
| `libgomp`                | X          | X      |
| `libnghttp2-14`          | X          | X      |
| `libpcre2-8-0`           | X          |        |
| `libssl3`                | X          | X      |
| `libstdc++`              | X          | X      |
| `libstdc++-dev`          | X          | X      |
| `libxml2`                | X          | X      |
| `linux-headers`          | X          | X      |
| `make`                   | X          | X      |
| `mpc`                    | X          | X      |
| `mpfr`                   | X          | X      |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `nss-db`                 | X          | X      |
| `nss-hesiod`             | X          | X      |
| `openssl-config`         | X          | X      |
| `pkgconf`                | X          | X      |
| `posix-cc-wrappers`      | X          | X      |
| `rust`                   | X          | X      |
| `rustup`                 | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `xz`                     | X          | X      |
| `zlib`                   | X          | X      |
