---
title: "fluentd Image Variants"
type: "article"
description: "Detailed information about the public fluentd Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "fluentd"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **fluentd** Image.

## Variants Compared
The **fluentd** Chainguard Image currently has 3 public variants: 

- `latest-dev`
- `latest-splunk`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev     | latest-splunk  | latest         |
|--------------|----------------|----------------|----------------|
| Default User | `fluent`       | `fluent`       | `fluent`       |
| Entrypoint   | Service Bundle | Service Bundle | Service Bundle |
| CMD          | not specified  | not specified  | not specified  |
| Workdir      | not specified  | not specified  | not specified  |
| Has apk?     | yes            | no             | no             |
| Has a shell? | yes            | no             | no             |

Check the [tags history page](/chainguard/chainguard-images/reference/fluentd/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                            | latest-dev | latest-splunk | latest |
|----------------------------|------------|---------------|--------|
| `apk-tools`                | X          |               |        |
| `bash`                     | X          |               |        |
| `binutils`                 | X          |               |        |
| `build-base`               | X          |               |        |
| `busybox`                  | X          |               |        |
| `ca-certificates-bundle`   | X          | X             | X      |
| `execline`                 | X          | X             | X      |
| `gcc`                      | X          |               |        |
| `git`                      | X          |               |        |
| `glibc`                    | X          | X             | X      |
| `glibc-dev`                | X          |               |        |
| `glibc-locale-posix`       | X          | X             | X      |
| `gmp`                      | X          |               |        |
| `isl`                      | X          |               |        |
| `ld-linux`                 | X          | X             | X      |
| `libatomic`                | X          |               |        |
| `libbrotlicommon1`         | X          |               |        |
| `libbrotlidec1`            | X          |               |        |
| `libcrypt1`                | X          | X             | X      |
| `libcrypto3`               | X          | X             | X      |
| `libcurl-openssl4`         | X          |               |        |
| `libexpat1`                | X          |               |        |
| `libffi`                   | X          | X             | X      |
| `libgcc`                   | X          | X             | X      |
| `libgo`                    | X          |               |        |
| `libgomp`                  | X          |               |        |
| `libnghttp2-14`            | X          |               |        |
| `libpcre2-8-0`             | X          |               |        |
| `libssl3`                  | X          | X             | X      |
| `libstdc++`                | X          |               |        |
| `libstdc++-dev`            | X          |               |        |
| `linux-headers`            | X          |               |        |
| `make`                     | X          |               |        |
| `mpc`                      | X          |               |        |
| `mpfr`                     | X          |               |        |
| `ncurses`                  | X          | X             | X      |
| `ncurses-terminfo-base`    | X          | X             | X      |
| `nss-db`                   | X          |               |        |
| `nss-hesiod`               | X          |               |        |
| `openssl-config`           | X          | X             | X      |
| `pkgconf`                  | X          |               |        |
| `posix-cc-wrappers`        | X          |               |        |
| `readline`                 | X          | X             | X      |
| `ruby-3.2`                 | X          | X             | X      |
| `ruby-3.2-dev`             | X          |               |        |
| `ruby3.2-bundler`          | X          | X             | X      |
| `ruby3.2-concurrent-ruby`  | X          | X             | X      |
| `ruby3.2-cool.io`          | X          | X             | X      |
| `ruby3.2-fluentd`          | X          | X             | X      |
| `ruby3.2-http_parser.rb`   | X          | X             | X      |
| `ruby3.2-msgpack`          | X          | X             | X      |
| `ruby3.2-serverengine`     | X          | X             | X      |
| `ruby3.2-sigdump`          | X          | X             | X      |
| `ruby3.2-strptime`         | X          | X             | X      |
| `ruby3.2-tzinfo`           | X          | X             | X      |
| `ruby3.2-tzinfo-data`      | X          | X             | X      |
| `ruby3.2-webrick`          | X          | X             | X      |
| `ruby3.2-yajl-ruby`        | X          | X             | X      |
| `s6`                       | X          | X             | X      |
| `skalibs`                  | X          | X             | X      |
| `wolfi-baselayout`         | X          | X             | X      |
| `yaml`                     | X          | X             | X      |
| `zlib`                     | X          | X             | X      |
| `fluent-plugin-splunk-hec` |            | X             |        |

