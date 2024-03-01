---
title: "php Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public php Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-03-01 12:14:22
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/php/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/php/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/php/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/php/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **php** Image.

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

|                             | latest-dev | latest-fpm-dev | latest-fpm | latest |
|-----------------------------|------------|----------------|------------|--------|
| `apk-tools`                 | X          | X              |            |        |
| `bash`                      | X          | X              |            |        |
| `busybox`                   | X          | X              |            |        |
| `ca-certificates`           | X          | X              | X          | X      |
| `ca-certificates-bundle`    | X          | X              | X          | X      |
| `chainguard-baselayout`     | X          | X              | X          | X      |
| `composer`                  | X          | X              |            |        |
| `curl`                      | X          | X              | X          | X      |
| `git`                       | X          | X              |            |        |
| `glibc`                     | X          | X              | X          | X      |
| `glibc-locale-posix`        | X          | X              | X          | X      |
| `ld-linux`                  | X          | X              | X          | X      |
| `libbrotlicommon1`          | X          | X              | X          | X      |
| `libbrotlidec1`             | X          | X              | X          | X      |
| `libcrypt1`                 | X          | X              |            |        |
| `libcrypto3`                | X          | X              | X          | X      |
| `libcurl-openssl4`          | X          | X              | X          | X      |
| `libexpat1`                 | X          | X              |            |        |
| `libidn2`                   | X          | X              | X          | X      |
| `libnghttp2-14`             | X          | X              | X          | X      |
| `libpcre2-8-0`              | X          | X              |            |        |
| `libpsl`                    | X          | X              | X          | X      |
| `libsodium`                 | X          | X              | X          | X      |
| `libssl3`                   | X          | X              | X          | X      |
| `libunistring`              | X          | X              | X          | X      |
| `libxml2`                   | X          | X              | X          | X      |
| `ncurses`                   | X          | X              | X          | X      |
| `ncurses-terminfo-base`     | X          | X              | X          | X      |
| `oniguruma`                 | X          | X              | X          | X      |
| `openssl-config`            | X          | X              | X          | X      |
| `php-8.2`                   | X          | X              | X          | X      |
| `php-8.2-config`            | X          | X              | X          | X      |
| `php-8.2-curl`              | X          | X              | X          | X      |
| `php-8.2-curl-config`       | X          | X              | X          | X      |
| `php-8.2-iconv`             | X          | X              | X          | X      |
| `php-8.2-iconv-config`      | X          | X              | X          | X      |
| `php-8.2-mbstring`          | X          | X              | X          | X      |
| `php-8.2-mbstring-config`   | X          | X              | X          | X      |
| `php-8.2-mysqlnd`           | X          | X              | X          | X      |
| `php-8.2-mysqlnd-config`    | X          | X              | X          | X      |
| `php-8.2-openssl`           | X          | X              | X          | X      |
| `php-8.2-openssl-config`    | X          | X              | X          | X      |
| `php-8.2-pdo`               | X          | X              | X          | X      |
| `php-8.2-pdo-config`        | X          | X              | X          | X      |
| `php-8.2-pdo_mysql`         | X          | X              | X          | X      |
| `php-8.2-pdo_mysql-config`  | X          | X              | X          | X      |
| `php-8.2-pdo_sqlite`        | X          | X              | X          | X      |
| `php-8.2-pdo_sqlite-config` | X          | X              | X          | X      |
| `php-8.2-phar`              | X          | X              | X          | X      |
| `php-8.2-phar-config`       | X          | X              | X          | X      |
| `php-8.2-sodium`            | X          | X              | X          | X      |
| `php-8.2-sodium-config`     | X          | X              | X          | X      |
| `readline`                  | X          | X              | X          | X      |
| `sqlite-libs`               | X          | X              | X          | X      |
| `wget`                      | X          | X              |            |        |
| `wolfi-baselayout`          | X          | X              | X          | X      |
| `xz`                        | X          | X              | X          | X      |
| `zlib`                      | X          | X              | X          | X      |
| `execline`                  |            | X              | X          |        |
| `php-8.2-fpm`               |            | X              | X          |        |
| `php-8.2-fpm-config`        |            | X              | X          |        |
| `s6`                        |            | X              | X          |        |
| `skalibs`                   |            | X              | X          |        |

