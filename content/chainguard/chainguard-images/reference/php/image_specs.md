---
title: "php Image Variants"
type: "article"
description: "Detailed specs for php Chainguard Image Variants"
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

This page shows detailed information about all available variants of the Chainguard **php** Image.

## Variants Compared
The **php** Chainguard Image currently has 4 public variants: 

- `latest`
- `latest-dev`
- `latest-fpm`
- `latest-fpm-dev`

The table has detailed information about each of these variants.

|              | latest        | latest-dev    | latest-fpm     | latest-fpm-dev |
|--------------|---------------|---------------|----------------|----------------|
| Default User | `php`         | `php`         | `php`          | `php`          |
| Entrypoint   | `/bin/php`    | `/bin/php`    | Service Bundle | Service Bundle |
| CMD          | not specified | not specified | not specified  | not specified  |
| Workdir      | `/app`        | `/app`        | `/app`         | `/app`         |
| Has apk?     | no            | yes           | no             | yes            |
| Has a shell? | no            | yes           | no             | yes            |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev | latest-fpm | latest-fpm-dev |
|--------------------------|--------|------------|------------|----------------|
| `wolfi-baselayout`       | X      | X          | X          | X              |
| `ca-certificates-bundle` | X      | X          | X          | X              |
| `php`                    | X      | X          | X          | X              |
| `apk-tools`              |        | X          |            | X              |
| `bash`                   |        | X          |            | X              |
| `busybox`                |        | X          |            | X              |
| `git`                    |        | X          |            | X              |
| `composer`               |        | X          |            | X              |
| `php-fpm`                |        |            | X          | X              |

