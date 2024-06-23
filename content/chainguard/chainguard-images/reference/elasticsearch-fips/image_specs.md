---
title: "elasticsearch-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public elasticsearch-fips Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-06-23 00:43:06
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/elasticsearch-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/elasticsearch-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/elasticsearch-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/elasticsearch-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **elasticsearch-fips** Image.

|              | latest                                        |
|--------------|-----------------------------------------------|
| Default User | `elastic`                                     |
| Entrypoint   | `/sbin/tini -- /usr/bin/docker-entrypoint.sh` |
| CMD          | `eswrapper`                                   |
| Workdir      | not specified                                 |
| Has apk?     | no                                            |
| Has a shell? | yes                                           |

Check the [tags history page](/chainguard/chainguard-images/reference/elasticsearch-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                 | latest |
|---------------------------------|--------|
| `bash`                          | X      |
| `bouncycastle-fips`             | X      |
| `bouncycastle-pkix-fips`        | X      |
| `bouncycastle-tls-fips`         | X      |
| `ca-certificates`               | X      |
| `ca-certificates-bundle`        | X      |
| `chainguard-baselayout`         | X      |
| `coreutils`                     | X      |
| `curl`                          | X      |
| `elasticsearch-fips-8`          | X      |
| `elasticsearch-fips-8-config`   | X      |
| `fontconfig-config`             | X      |
| `freetype`                      | X      |
| `glibc`                         | X      |
| `glibc-locale-posix`            | X      |
| `grep`                          | X      |
| `java-cacerts`                  | X      |
| `java-common`                   | X      |
| `ld-linux`                      | X      |
| `libacl1`                       | X      |
| `libattr1`                      | X      |
| `libbrotlicommon1`              | X      |
| `libbrotlidec1`                 | X      |
| `libbz2-1`                      | X      |
| `libcap`                        | X      |
| `libcrypto3`                    | X      |
| `libcurl-openssl4`              | X      |
| `libexpat1`                     | X      |
| `libffi`                        | X      |
| `libfontconfig1`                | X      |
| `libidn2`                       | X      |
| `libnghttp2-14`                 | X      |
| `libpcre2-8-0`                  | X      |
| `libpng`                        | X      |
| `libpsl`                        | X      |
| `libssl3`                       | X      |
| `libsystemd`                    | X      |
| `libtasn1`                      | X      |
| `libunistring`                  | X      |
| `ncurses`                       | X      |
| `ncurses-terminfo-base`         | X      |
| `openjdk-17-default-jvm-bcfips` | X      |
| `openjdk-17-jre-base-bcfips`    | X      |
| `openjdk-17-jre-bcfips`         | X      |
| `openssl-config-fipshardened`   | X      |
| `openssl-provider-fips`         | X      |
| `p11-kit`                       | X      |
| `p11-kit-trust`                 | X      |
| `tini`                          | X      |
| `wolfi-baselayout`              | X      |
| `zlib`                          | X      |

