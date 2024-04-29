---
title: "aws-for-fluent-bit Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public aws-for-fluent-bit Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-04-29 00:53:42
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/aws-for-fluent-bit/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/aws-for-fluent-bit/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/aws-for-fluent-bit/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/aws-for-fluent-bit/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **aws-for-fluent-bit** Image.

|              | latest-dev-flb-1                                                                                                       | latest-dev                                                                                                             | latest-flb-1                                                                                                           | latest                                                                                                                 |
|--------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Default User | `root`                                                                                                                 | `root`                                                                                                                 | `root`                                                                                                                 | `root`                                                                                                                 |
| Entrypoint   | `/fluent-bit/bin/fluent-bit`                                                                                           | `/fluent-bit/bin/fluent-bit`                                                                                           | `/fluent-bit/bin/fluent-bit`                                                                                           | `/fluent-bit/bin/fluent-bit`                                                                                           |
| CMD          | `-e /fluent-bit/firehose.so -e /fluent-bit/cloudwatch.so -e /fluent-bit/kinesis.so -c /fluent-bit/etc/fluent-bit.conf` | `-e /fluent-bit/firehose.so -e /fluent-bit/cloudwatch.so -e /fluent-bit/kinesis.so -c /fluent-bit/etc/fluent-bit.conf` | `-e /fluent-bit/firehose.so -e /fluent-bit/cloudwatch.so -e /fluent-bit/kinesis.so -c /fluent-bit/etc/fluent-bit.conf` | `-e /fluent-bit/firehose.so -e /fluent-bit/cloudwatch.so -e /fluent-bit/kinesis.so -c /fluent-bit/etc/fluent-bit.conf` |
| Workdir      | not specified                                                                                                          | not specified                                                                                                          | not specified                                                                                                          | not specified                                                                                                          |
| Has apk?     | yes                                                                                                                    | yes                                                                                                                    | no                                                                                                                     | no                                                                                                                     |
| Has a shell? | yes                                                                                                                    | yes                                                                                                                    | no                                                                                                                     | no                                                                                                                     |

Check the [tags history page](/chainguard/chainguard-images/reference/aws-for-fluent-bit/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                 | latest-dev-flb-1 | latest-dev | latest-flb-1 | latest |
|---------------------------------|------------------|------------|--------------|--------|
| `apk-tools`                     | X                | X          |              |        |
| `aws-flb-cloudwatch`            | X                | X          | X            | X      |
| `aws-flb-cloudwatch-compat`     | X                | X          | X            | X      |
| `aws-flb-firehose`              | X                | X          | X            | X      |
| `aws-flb-firehose-compat`       | X                | X          | X            | X      |
| `aws-flb-kinesis`               | X                | X          | X            | X      |
| `aws-flb-kinesis-compat`        | X                | X          | X            | X      |
| `aws-for-fluent-bit-1.9`        | X                |            | X            |        |
| `aws-for-fluent-bit-compat-1.9` | X                |            | X            |        |
| `bash`                          | X                | X          |              |        |
| `busybox`                       | X                | X          |              |        |
| `ca-certificates-bundle`        | X                | X          | X            | X      |
| `chainguard-baselayout`         | X                | X          | X            | X      |
| `fluent-bit-1.9`                | X                |            | X            |        |
| `git`                           | X                | X          |              |        |
| `glibc`                         | X                | X          | X            | X      |
| `glibc-locale-posix`            | X                | X          | X            | X      |
| `ld-linux`                      | X                | X          | X            | X      |
| `libbrotlicommon1`              | X                | X          |              |        |
| `libbrotlidec1`                 | X                | X          |              |        |
| `libcap`                        | X                | X          | X            | X      |
| `libcrypt1`                     | X                | X          |              |        |
| `libcrypto3`                    | X                | X          | X            | X      |
| `libcurl-openssl4`              | X                | X          |              |        |
| `libexpat1`                     | X                | X          |              |        |
| `libgcc`                        | X                | X          | X            | X      |
| `libidn2`                       | X                | X          |              |        |
| `libnghttp2-14`                 | X                | X          |              |        |
| `libpcre2-8-0`                  | X                | X          |              |        |
| `libpq-16`                      | X                | X          | X            | X      |
| `libpsl`                        | X                | X          |              |        |
| `libssl3`                       | X                | X          | X            | X      |
| `libsystemd`                    | X                | X          | X            | X      |
| `libunistring`                  | X                | X          |              |        |
| `libxcrypt`                     | X                | X          |              |        |
| `ncurses`                       | X                | X          |              |        |
| `ncurses-terminfo-base`         | X                | X          |              |        |
| `openssl-config`                | X                | X          | X            | X      |
| `wget`                          | X                | X          |              |        |
| `wolfi-baselayout`              | X                | X          | X            | X      |
| `yaml`                          | X                | X          | X            | X      |
| `zlib`                          | X                | X          | X            | X      |
| `aws-for-fluent-bit`            |                  | X          |              | X      |
| `aws-for-fluent-bit-compat`     |                  | X          |              | X      |
| `fluent-bit-3.0`                |                  | X          |              | X      |

