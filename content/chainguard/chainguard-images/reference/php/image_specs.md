---
title: "php Image Variants"
type: "article"
description: "Detailed information about the public php Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "php"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **php** Image.

## Variants Compared
The **php** Chainguard Image currently has 4 public variants: 

- `latest-dev`
- `latest-fpm-dev`
- `latest-fpm`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev    | latest-fpm-dev | latest-fpm     | latest        |
|--------------|---------------|----------------|----------------|---------------|
| Default User | `php`         | `php`          | `php`          | `php`         |
| Entrypoint   | `/bin/php`    | Service Bundle | Service Bundle | `/bin/php`    |
| CMD          | not specified | not specified  | not specified  | not specified |
| Workdir      | `/app`        | `/app`         | `/app`         | `/app`        |
| Has apk?     | yes           | yes            | no             | no            |
| Has a shell? | yes           | yes            | no             | no            |

Check the [tags history page](/chainguard/chainguard-images/reference/php/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest-fpm-dev | latest-fpm | latest |
|--------------------------|------------|----------------|------------|--------|
| `apk-tools`              | X          | X              |            |        |
| `bash`                   | X          | X              |            |        |
| `busybox`                | X          | X              |            |        |
| `ca-certificates`        | X          | X              | X          | X      |
| `ca-certificates-bundle` | X          | X              | X          | X      |
| `composer`               | X          | X              |            |        |
| `curl`                   | X          | X              | X          | X      |
| `git`                    | X          | X              |            |        |
| `glibc`                  | X          | X              | X          | X      |
| `glibc-locale-posix`     | X          | X              | X          | X      |
| `ld-linux`               | X          | X              | X          | X      |
| `libbrotlicommon1`       | X          | X              | X          | X      |
| `libbrotlidec1`          | X          | X              | X          | X      |
| `libcrypt1`              | X          | X              |            |        |
| `libcrypto3`             | X          | X              | X          | X      |
| `libcurl-openssl4`       | X          | X              | X          | X      |
| `libexpat1`              | X          | X              |            |        |
| `libnghttp2-14`          | X          | X              | X          | X      |
| `libpcre2-8-0`           | X          | X              |            |        |
| `libsodium`              | X          | X              | X          | X      |
| `libssl3`                | X          | X              | X          | X      |
| `libxml2`                | X          | X              | X          | X      |
| `ncurses`                | X          | X              | X          | X      |
| `ncurses-terminfo-base`  | X          | X              | X          | X      |
| `oniguruma`              | X          | X              | X          | X      |
| `openssl-config`         | X          | X              | X          | X      |
| `php`                    | X          | X              | X          | X      |
| `php-curl`               | X          | X              | X          | X      |
| `php-iconv`              | X          | X              | X          | X      |
| `php-mbstring`           | X          | X              | X          | X      |
| `php-mysqlnd`            | X          | X              | X          | X      |
| `php-openssl`            | X          | X              | X          | X      |
| `php-pdo`                | X          | X              | X          | X      |
| `php-pdo_mysql`          | X          | X              | X          | X      |
| `php-pdo_sqlite`         | X          | X              | X          | X      |
| `php-phar`               | X          | X              | X          | X      |
| `php-sodium`             | X          | X              | X          | X      |
| `readline`               | X          | X              | X          | X      |
| `sqlite-libs`            | X          | X              | X          | X      |
| `wolfi-baselayout`       | X          | X              | X          | X      |
| `xz`                     | X          | X              | X          | X      |
| `zlib`                   | X          | X              | X          | X      |
| `execline`               |            | X              | X          |        |
| `php-fpm`                |            | X              | X          |        |
| `s6`                     |            | X              | X          |        |
| `skalibs`                |            | X              | X          |        |

