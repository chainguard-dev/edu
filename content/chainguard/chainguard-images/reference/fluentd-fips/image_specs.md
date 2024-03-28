---
title: "fluentd-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public fluentd-fips Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-03-28 00:50:32
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/fluentd-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/fluentd-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/fluentd-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/fluentd-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **fluentd-fips** Image.

|              | latest-dev         | latest             |
|--------------|--------------------|--------------------|
| Default User | `fluent`           | `fluent`           |
| Entrypoint   | `/usr/bin/fluentd` | `/usr/bin/fluentd` |
| CMD          | not specified      | not specified      |
| Workdir      | not specified      | not specified      |
| Has apk?     | yes                | no                 |
| Has a shell? | yes                | no                 |

Check the [tags history page](/chainguard/chainguard-images/reference/fluentd-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                               | latest-dev | latest |
|-------------------------------|------------|--------|
| `apk-tools`                   | X          |        |
| `bash`                        | X          |        |
| `busybox`                     | X          |        |
| `ca-certificates-bundle`      | X          | X      |
| `chainguard-baselayout`       | X          | X      |
| `git`                         | X          |        |
| `glibc`                       | X          | X      |
| `glibc-locale-posix`          | X          | X      |
| `ld-linux`                    | X          | X      |
| `libbrotlicommon1`            | X          |        |
| `libbrotlidec1`               | X          |        |
| `libcrypt1`                   | X          | X      |
| `libcrypto3`                  | X          | X      |
| `libcurl-openssl4`            | X          |        |
| `libexpat1`                   | X          |        |
| `libffi`                      | X          | X      |
| `libgcc`                      | X          | X      |
| `libidn2`                     | X          |        |
| `libnghttp2-14`               | X          |        |
| `libpcre2-8-0`                | X          |        |
| `libpq-16`                    | X          | X      |
| `libpsl`                      | X          |        |
| `libssl3`                     | X          | X      |
| `libunistring`                | X          |        |
| `libxcrypt`                   | X          | X      |
| `ncurses`                     | X          | X      |
| `ncurses-terminfo-base`       | X          | X      |
| `openssl-config-fipshardened` | X          | X      |
| `openssl-provider-fips`       | X          | X      |
| `readline`                    | X          | X      |
| `ruby-3.2`                    | X          | X      |
| `ruby3.2-bundler`             | X          | X      |
| `ruby3.2-concurrent-ruby`     | X          | X      |
| `ruby3.2-cool.io`             | X          | X      |
| `ruby3.2-fluentd-1.16`        | X          | X      |
| `ruby3.2-http_parser.rb`      | X          | X      |
| `ruby3.2-msgpack`             | X          | X      |
| `ruby3.2-serverengine`        | X          | X      |
| `ruby3.2-sigdump`             | X          | X      |
| `ruby3.2-strptime`            | X          | X      |
| `ruby3.2-tzinfo`              | X          | X      |
| `ruby3.2-tzinfo-data`         | X          | X      |
| `ruby3.2-webrick`             | X          | X      |
| `ruby3.2-yajl-ruby`           | X          | X      |
| `wget`                        | X          |        |
| `wolfi-baselayout`            | X          | X      |
| `yaml`                        | X          | X      |
| `zlib`                        | X          | X      |

