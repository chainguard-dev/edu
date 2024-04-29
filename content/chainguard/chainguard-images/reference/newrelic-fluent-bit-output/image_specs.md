---
title: "newrelic-fluent-bit-output Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public newrelic-fluent-bit-output Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-04-29 00:53:42
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/newrelic-fluent-bit-output/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/newrelic-fluent-bit-output/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/newrelic-fluent-bit-output/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/newrelic-fluent-bit-output/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **newrelic-fluent-bit-output** Image.

|              | latest-dev                                                              | latest                                                                  |
|--------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Default User | `root`                                                                  | `root`                                                                  |
| Entrypoint   | `/usr/bin/fluent-bit`                                                   | `/usr/bin/fluent-bit`                                                   |
| CMD          | `-c /fluent-bit/etc/fluent-bit.conf -e /fluent-bit/bin/out_newrelic.so` | `-c /fluent-bit/etc/fluent-bit.conf -e /fluent-bit/bin/out_newrelic.so` |
| Workdir      | not specified                                                           | not specified                                                           |
| Has apk?     | yes                                                                     | no                                                                      |
| Has a shell? | yes                                                                     | no                                                                      |

Check the [tags history page](/chainguard/chainguard-images/reference/newrelic-fluent-bit-output/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                     | latest-dev | latest |
|-------------------------------------|------------|--------|
| `apk-tools`                         | X          |        |
| `bash`                              | X          |        |
| `busybox`                           | X          |        |
| `ca-certificates-bundle`            | X          | X      |
| `chainguard-baselayout`             | X          | X      |
| `fluent-bit-3.0`                    | X          | X      |
| `git`                               | X          |        |
| `glibc`                             | X          | X      |
| `glibc-locale-posix`                | X          | X      |
| `ld-linux`                          | X          | X      |
| `libbrotlicommon1`                  | X          |        |
| `libbrotlidec1`                     | X          |        |
| `libcap`                            | X          | X      |
| `libcrypt1`                         | X          |        |
| `libcrypto3`                        | X          | X      |
| `libcurl-openssl4`                  | X          |        |
| `libexpat1`                         | X          |        |
| `libgcc`                            | X          | X      |
| `libidn2`                           | X          |        |
| `libnghttp2-14`                     | X          |        |
| `libpcre2-8-0`                      | X          |        |
| `libpq-16`                          | X          | X      |
| `libpsl`                            | X          |        |
| `libssl3`                           | X          | X      |
| `libsystemd`                        | X          | X      |
| `libunistring`                      | X          |        |
| `libxcrypt`                         | X          |        |
| `ncurses`                           | X          |        |
| `ncurses-terminfo-base`             | X          |        |
| `newrelic-fluent-bit-output`        | X          | X      |
| `newrelic-fluent-bit-output-compat` | X          | X      |
| `openssl-config`                    | X          | X      |
| `wget`                              | X          |        |
| `wolfi-baselayout`                  | X          | X      |
| `yaml`                              | X          | X      |
| `zlib`                              | X          | X      |

