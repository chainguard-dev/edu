---
title: "rabbitmq-bitnami-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public rabbitmq-bitnami-fips Chainguard Image."
date: 2024-05-24 00:45:45
lastmod: 2024-05-24 00:45:45
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/rabbitmq-bitnami-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/rabbitmq-bitnami-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/rabbitmq-bitnami-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/rabbitmq-bitnami-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **rabbitmq-bitnami-fips** Image.

|              | latest-dev                                                                         | latest                                                                             |
|--------------|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| Default User | `rabbitmq`                                                                         | `rabbitmq`                                                                         |
| Entrypoint   | `/opt/bitnami/scripts/rabbitmq/entrypoint.sh /opt/bitnami/scripts/rabbitmq/run.sh` | `/opt/bitnami/scripts/rabbitmq/entrypoint.sh /opt/bitnami/scripts/rabbitmq/run.sh` |
| CMD          | not specified                                                                      | not specified                                                                      |
| Workdir      | `/opt/bitnami/rabbitmq`                                                            | `/opt/bitnami/rabbitmq`                                                            |
| Has apk?     | yes                                                                                | no                                                                                 |
| Has a shell? | yes                                                                                | yes                                                                                |

Check the [tags history page](/chainguard/chainguard-images/reference/rabbitmq-bitnami-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                               | latest-dev | latest |
|-------------------------------|------------|--------|
| `apk-tools`                   | X          |        |
| `bash`                        | X          | X      |
| `busybox`                     | X          | X      |
| `ca-certificates-bundle`      | X          | X      |
| `chainguard-baselayout`       | X          | X      |
| `coreutils`                   | X          | X      |
| `curl`                        | X          | X      |
| `erlang-fips-26`              | X          | X      |
| `git`                         | X          |        |
| `glibc`                       | X          | X      |
| `glibc-locale-en`             | X          | X      |
| `glibc-locale-posix`          | X          | X      |
| `ld-linux`                    | X          | X      |
| `libacl1`                     | X          | X      |
| `libattr1`                    | X          | X      |
| `libbrotlicommon1`            | X          | X      |
| `libbrotlidec1`               | X          | X      |
| `libcrypt1`                   | X          | X      |
| `libcrypto3`                  | X          | X      |
| `libcurl-openssl4`            | X          | X      |
| `libexpat1`                   | X          |        |
| `libgcc`                      | X          | X      |
| `libidn2`                     | X          | X      |
| `libnghttp2-14`               | X          | X      |
| `libpcre2-8-0`                | X          |        |
| `libproc-2-0`                 | X          | X      |
| `libpsl`                      | X          | X      |
| `libssl3`                     | X          | X      |
| `libstdc++`                   | X          | X      |
| `libunistring`                | X          | X      |
| `libxcrypt`                   | X          | X      |
| `ncurses`                     | X          | X      |
| `ncurses-terminfo-base`       | X          | X      |
| `openssl-config-fipshardened` | X          | X      |
| `openssl-provider-fips`       | X          | X      |
| `procps`                      | X          | X      |
| `rabbitmq-server-compat`      | X          | X      |
| `rabbitmq-server-fips`        | X          | X      |
| `tzdata`                      | X          | X      |
| `wget`                        | X          |        |
| `wolfi-baselayout`            | X          | X      |
| `zlib`                        | X          | X      |

