---
title: "Ruby Public Image Variants"
type: "article"
description: "Detailed information about the public Ruby Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Ruby"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **Ruby** Image.

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
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libssl3`                | X          | X      |
| `libstdc++`              | X          |        |
| `libstdc++-dev`          | X          |        |
| `linux-headers`          | X          |        |
| `make`                   | X          |        |
| `mpc`                    | X          |        |
| `mpfr`                   | X          |        |
| `ncurses`                | X          | X      |
| `ncurses-terminfo-base`  | X          | X      |
| `nss-db`                 | X          |        |
| `nss-hesiod`             | X          |        |
| `openssl-config`         | X          | X      |
| `pkgconf`                | X          |        |
| `posix-cc-wrappers`      | X          |        |
| `readline`               | X          | X      |
| `ruby-3.2`               | X          | X      |
| `ruby-3.2-dev`           | X          |        |
| `ruby3.2-bundler`        | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `yaml`                   | X          | X      |
| `zlib`                   | X          | X      |
