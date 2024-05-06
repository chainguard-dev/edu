---
title: "elasticsearch-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public elasticsearch-fips Chainguard Image."
date: 2024-05-06 00:43:57
lastmod: 2024-05-06 00:43:57
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
| `busybox`                       | X      |
| `ca-certificates`               | X      |
| `ca-certificates-bundle`        | X      |
| `chainguard-baselayout`         | X      |
| `elasticsearch-fips-8`          | X      |
| `elasticsearch-fips-8-config`   | X      |
| `fontconfig-config`             | X      |
| `freetype`                      | X      |
| `glibc`                         | X      |
| `glibc-locale-posix`            | X      |
| `java-cacerts`                  | X      |
| `java-common`                   | X      |
| `ld-linux`                      | X      |
| `libbrotlicommon1`              | X      |
| `libbrotlidec1`                 | X      |
| `libbz2-1`                      | X      |
| `libcrypt1`                     | X      |
| `libcrypto3`                    | X      |
| `libexpat1`                     | X      |
| `libffi`                        | X      |
| `libfontconfig1`                | X      |
| `libpng`                        | X      |
| `libtasn1`                      | X      |
| `libxcrypt`                     | X      |
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

