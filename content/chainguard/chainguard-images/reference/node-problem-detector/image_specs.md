---
title: "node-problem-detector Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public node-problem-detector Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-01-15 00:20:04
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/node-problem-detector/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/node-problem-detector/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/node-problem-detector/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/node-problem-detector/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **node-problem-detector** Image.

## Variants Compared
The **node-problem-detector** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                                | latest                                                    |
|--------------|-----------------------------------------------------------|-----------------------------------------------------------|
| Default User | `root`                                                    | `root`                                                    |
| Entrypoint   | `/usr/bin/node-problem-detector`                          | `/usr/bin/node-problem-detector`                          |
| CMD          | `--config.system-log-monitor=/config/kernel-monitor.json` | `--config.system-log-monitor=/config/kernel-monitor.json` |
| Workdir      | not specified                                             | not specified                                             |
| Has apk?     | yes                                                       | no                                                        |
| Has a shell? | yes                                                       | yes                                                       |

Check the [tags history page](/chainguard/chainguard-images/reference/node-problem-detector/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                    | latest-dev | latest |
|------------------------------------|------------|--------|
| `apk-tools`                        | X          |        |
| `bash`                             | X          |        |
| `busybox`                          | X          | X      |
| `ca-certificates-bundle`           | X          | X      |
| `git`                              | X          |        |
| `glibc`                            | X          | X      |
| `glibc-locale-posix`               | X          | X      |
| `health-checker-0.8`               | X          | X      |
| `ld-linux`                         | X          | X      |
| `libblkid`                         | X          | X      |
| `libbrotlicommon1`                 | X          |        |
| `libbrotlidec1`                    | X          |        |
| `libcap`                           | X          | X      |
| `libcrypt1`                        | X          | X      |
| `libcrypto3`                       | X          |        |
| `libcurl-openssl4`                 | X          |        |
| `libexpat1`                        | X          |        |
| `libfdisk`                         | X          | X      |
| `libidn2`                          | X          |        |
| `libmount`                         | X          | X      |
| `libnghttp2-14`                    | X          |        |
| `libpcre2-8-0`                     | X          |        |
| `libpsl`                           | X          |        |
| `libssl3`                          | X          |        |
| `libsystemd`                       | X          | X      |
| `libunistring`                     | X          |        |
| `libuuid`                          | X          | X      |
| `log-counter-0.8`                  | X          | X      |
| `ncurses`                          | X          |        |
| `ncurses-terminfo-base`            | X          |        |
| `node-problem-detector-0.8`        | X          | X      |
| `node-problem-detector-0.8-compat` | X          | X      |
| `openssl-config`                   | X          |        |
| `systemd`                          | X          | X      |
| `systemd-dev`                      | X          | X      |
| `wolfi-baselayout`                 | X          | X      |
| `zlib`                             | X          |        |

