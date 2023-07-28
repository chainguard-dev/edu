---
title: "Php Image Variants"
type: "article"
description: "Detailed information about the Php Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Php"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Php** Image.

## Variants Compared
The **php** Chainguard Image currently has 4 public variants: 

- `latest`
- `latest-dev`
- `latest-fpm`
- `latest-fpm-dev`

## Default Image Settings
`USER`:		`php`

`WORKDIR`:	`/app`

`ENTRYPOINT`:	Service Bundle

`CMD`:		not specified

The following table has additional information about each of these variants.

|              | latest | latest-dev | latest-fpm | latest-fpm-dev |
|--------------|--------|------------|------------|----------------|
| Has apk?     | no     | yes        | no         | yes            |
| Has a shell? | no     | yes        | no         | yes            |

Check the [tags history page](/chainguard/chainguard-images/reference/php/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                   | latest | latest-dev | latest-fpm | latest-fpm-dev |
|-------------------|--------|------------|------------|----------------|
| `ca-certificates` | X      | X          | X          | X              |
| `curl`            | X      | X          | X          | X              |
| `php`             | X      | X          | X          | X              |
| `php-curl`        | X      | X          | X          | X              |
| `php-openssl`     | X      | X          | X          | X              |
| `php-iconv`       | X      | X          | X          | X              |
| `php-mbstring`    | X      | X          | X          | X              |
| `php-mysqlnd`     | X      | X          | X          | X              |
| `php-pdo`         | X      | X          | X          | X              |
| `php-pdo_sqlite`  | X      | X          | X          | X              |
| `php-pdo_mysql`   | X      | X          | X          | X              |
| `php-sodium`      | X      | X          | X          | X              |
| `php-phar`        | X      | X          | X          | X              |
| `php-fpm`         |        |            | X          | X              |
