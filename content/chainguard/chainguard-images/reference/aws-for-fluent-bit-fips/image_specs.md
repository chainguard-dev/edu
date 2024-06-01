---
title: "aws-for-fluent-bit-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public aws-for-fluent-bit-fips Chainguard Image."
date: 2024-06-01 00:50:07
lastmod: 2024-06-01 00:50:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/aws-for-fluent-bit-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/aws-for-fluent-bit-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/aws-for-fluent-bit-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/aws-for-fluent-bit-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **aws-for-fluent-bit-fips** Image.

|              | latest-dev                                                                                                             | latest                                                                                                                 |
|--------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Default User | `root`                                                                                                                 | `root`                                                                                                                 |
| Entrypoint   | `/fluent-bit/bin/fluent-bit`                                                                                           | `/fluent-bit/bin/fluent-bit`                                                                                           |
| CMD          | `-e /fluent-bit/firehose.so -e /fluent-bit/cloudwatch.so -e /fluent-bit/kinesis.so -c /fluent-bit/etc/fluent-bit.conf` | `-e /fluent-bit/firehose.so -e /fluent-bit/cloudwatch.so -e /fluent-bit/kinesis.so -c /fluent-bit/etc/fluent-bit.conf` |
| Workdir      | not specified                                                                                                          | not specified                                                                                                          |
| Has apk?     | yes                                                                                                                    | no                                                                                                                     |
| Has a shell? | yes                                                                                                                    | no                                                                                                                     |

Check the [tags history page](/chainguard/chainguard-images/reference/aws-for-fluent-bit-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                  | latest-dev | latest |
|----------------------------------|------------|--------|
| `apk-tools`                      | X          |        |
| `aws-flb-cloudwatch-compat-fips` | X          | X      |
| `aws-flb-cloudwatch-fips`        | X          | X      |
| `aws-flb-firehose-compat-fips`   | X          | X      |
| `aws-flb-firehose-fips`          | X          | X      |
| `aws-flb-kinesis-compat-fips`    | X          | X      |
| `aws-flb-kinesis-fips`           | X          | X      |
| `aws-for-fluent-bit-compat-fips` | X          | X      |
| `aws-for-fluent-bit-fips`        | X          | X      |
| `bash`                           | X          |        |
| `busybox`                        | X          |        |
| `ca-certificates-bundle`         | X          | X      |
| `chainguard-baselayout`          | X          | X      |
| `fluent-bit-1.9`                 | X          | X      |
| `git`                            | X          |        |
| `glibc`                          | X          | X      |
| `glibc-locale-posix`             | X          | X      |
| `ld-linux`                       | X          | X      |
| `libbrotlicommon1`               | X          |        |
| `libbrotlidec1`                  | X          |        |
| `libcap`                         | X          | X      |
| `libcrypt1`                      | X          |        |
| `libcrypto3`                     | X          | X      |
| `libcurl-openssl4`               | X          |        |
| `libexpat1`                      | X          |        |
| `libgcc`                         | X          | X      |
| `libidn2`                        | X          |        |
| `libnghttp2-14`                  | X          |        |
| `libpcre2-8-0`                   | X          |        |
| `libpq-16`                       | X          | X      |
| `libpsl`                         | X          |        |
| `libssl3`                        | X          | X      |
| `libsystemd`                     | X          | X      |
| `libunistring`                   | X          |        |
| `libxcrypt`                      | X          |        |
| `ncurses`                        | X          |        |
| `ncurses-terminfo-base`          | X          |        |
| `openssl-config-fipshardened`    | X          | X      |
| `openssl-provider-fips`          | X          | X      |
| `wget`                           | X          |        |
| `wolfi-baselayout`               | X          | X      |
| `yaml`                           | X          | X      |
| `zlib`                           | X          | X      |

