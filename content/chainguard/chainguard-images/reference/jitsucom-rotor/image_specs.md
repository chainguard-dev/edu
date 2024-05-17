---
title: "jitsucom-rotor Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public jitsucom-rotor Chainguard Image."
date: 2024-05-17 00:44:46
lastmod: 2024-05-17 00:44:46
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jitsucom-rotor/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/jitsucom-rotor/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/jitsucom-rotor/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jitsucom-rotor/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **jitsucom-rotor** Image.

|              | latest-dev                                             | latest                                                 |
|--------------|--------------------------------------------------------|--------------------------------------------------------|
| Default User | `nonroot`                                              | `nonroot`                                              |
| Entrypoint   | `/usr/local/bin/docker-entrypoint.sh`                  | `/usr/local/bin/docker-entrypoint.sh`                  |
| CMD          | `--no-node-snapshot --max-old-space-size=2048 main.js` | `--no-node-snapshot --max-old-space-size=2048 main.js` |
| Workdir      | `/app`                                                 | `/app`                                                 |
| Has apk?     | yes                                                    | no                                                     |
| Has a shell? | yes                                                    | yes                                                    |

Check the [tags history page](/chainguard/chainguard-images/reference/jitsucom-rotor/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                           | latest-dev | latest |
|---------------------------|------------|--------|
| `apk-tools`               | X          |        |
| `bash`                    | X          | X      |
| `busybox`                 | X          | X      |
| `c-ares`                  | X          | X      |
| `ca-certificates-bundle`  | X          | X      |
| `chainguard-baselayout`   | X          | X      |
| `curl`                    | X          | X      |
| `git`                     | X          |        |
| `glibc`                   | X          | X      |
| `glibc-locale-posix`      | X          | X      |
| `icu`                     | X          | X      |
| `jitsucom-jitsu`          | X          | X      |
| `jitsucom-jitsu-rotor`    | X          | X      |
| `ld-linux`                | X          | X      |
| `libbrotlicommon1`        | X          | X      |
| `libbrotlidec1`           | X          | X      |
| `libbrotlienc1`           | X          | X      |
| `libbsd`                  | X          | X      |
| `libcrypt1`               | X          | X      |
| `libcrypto3`              | X          | X      |
| `libcurl-openssl4`        | X          | X      |
| `libexpat1`               | X          |        |
| `libgcc`                  | X          | X      |
| `libidn2`                 | X          | X      |
| `libmd`                   | X          | X      |
| `libnghttp2-14`           | X          | X      |
| `libpcre2-8-0`            | X          |        |
| `libproc-2-0`             | X          | X      |
| `libpsl`                  | X          | X      |
| `libssl3`                 | X          | X      |
| `libstdc++`               | X          | X      |
| `libunistring`            | X          | X      |
| `libuv`                   | X          | X      |
| `libxcrypt`               | X          | X      |
| `ncurses`                 | X          | X      |
| `ncurses-terminfo-base`   | X          | X      |
| `netcat-openbsd`          | X          | X      |
| `nodejs-18`               | X          | X      |
| `openssl`                 | X          | X      |
| `openssl-provider-legacy` | X          | X      |
| `procps`                  | X          | X      |
| `wget`                    | X          |        |
| `wolfi-baselayout`        | X          | X      |
| `zlib`                    | X          | X      |

