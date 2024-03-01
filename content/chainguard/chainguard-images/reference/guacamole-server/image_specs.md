---
title: "guacamole-server Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public guacamole-server Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-03-01 12:14:22
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/guacamole-server/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/guacamole-server/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/guacamole-server/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/guacamole-server/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **guacamole-server** Image.

|              | latest-dev                                                        | latest                                                            |
|--------------|-------------------------------------------------------------------|-------------------------------------------------------------------|
| Default User | `65532`                                                           | `65532`                                                           |
| Entrypoint   | not specified                                                     | not specified                                                     |
| CMD          | `/bin/sh -c '/usr/sbin/guacd  -b 0.0.0.0 -L $GUACD_LOG_LEVEL -f'` | `/bin/sh -c '/usr/sbin/guacd  -b 0.0.0.0 -L $GUACD_LOG_LEVEL -f'` |
| Workdir      | not specified                                                     | not specified                                                     |
| Has apk?     | yes                                                               | no                                                                |
| Has a shell? | yes                                                               | yes                                                               |

Check the [tags history page](/chainguard/chainguard-images/reference/guacamole-server/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                           | latest-dev | latest |
|---------------------------|------------|--------|
| `alsa-lib`                | X          | X      |
| `aom-libs`                | X          | X      |
| `apk-tools`               | X          |        |
| `bash`                    | X          |        |
| `busybox`                 | X          | X      |
| `ca-certificates-bundle`  | X          | X      |
| `cairo`                   | X          | X      |
| `chainguard-baselayout`   | X          | X      |
| `cups-libs`               | X          | X      |
| `dbus-libs`               | X          | X      |
| `fontconfig-config`       | X          | X      |
| `freerdp-libs`            | X          | X      |
| `freetype`                | X          | X      |
| `fribidi`                 | X          | X      |
| `git`                     | X          |        |
| `glib`                    | X          | X      |
| `glibc`                   | X          | X      |
| `glibc-locale-posix`      | X          | X      |
| `graphite2`               | X          | X      |
| `gsm`                     | X          | X      |
| `guacamole-server`        | X          | X      |
| `harfbuzz`                | X          | X      |
| `ld-linux`                | X          | X      |
| `libasyncns`              | X          | X      |
| `libavcodec60`            | X          | X      |
| `libavformat60`           | X          | X      |
| `libavutil58`             | X          | X      |
| `libblkid`                | X          | X      |
| `libbrotlicommon1`        | X          | X      |
| `libbrotlidec1`           | X          | X      |
| `libbsd`                  | X          | X      |
| `libbz2-1`                | X          | X      |
| `libcrypt1`               | X          | X      |
| `libcrypto3`              | X          | X      |
| `libcurl-openssl4`        | X          |        |
| `libexpat1`               | X          | X      |
| `libffi`                  | X          | X      |
| `libflac`                 | X          | X      |
| `libfontconfig1`          | X          | X      |
| `libgcrypt`               | X          | X      |
| `libgomp`                 | X          | X      |
| `libgpg-error`            | X          | X      |
| `libguac-client-rdp`      | X          | X      |
| `libguac-client-ssh`      | X          | X      |
| `libguac-client-telnet`   | X          | X      |
| `libguac-client-vnc`      | X          | X      |
| `libidn2`                 | X          |        |
| `libjpeg-turbo`           | X          | X      |
| `libltdl`                 | X          | X      |
| `libmd`                   | X          | X      |
| `libmount`                | X          | X      |
| `libnghttp2-14`           | X          |        |
| `libogg`                  | X          | X      |
| `libpcre2-8-0`            | X          | X      |
| `libpng`                  | X          | X      |
| `libpsl`                  | X          |        |
| `libpulse`                | X          | X      |
| `libsndfile`              | X          | X      |
| `libssh2`                 | X          | X      |
| `libssl3`                 | X          | X      |
| `libswresample4`          | X          | X      |
| `libswscale7`             | X          | X      |
| `libtelnet`               | X          | X      |
| `libtheora`               | X          | X      |
| `libunistring`            | X          |        |
| `libusb`                  | X          | X      |
| `libuuid`                 | X          | X      |
| `libvncserver`            | X          | X      |
| `libvorbis`               | X          | X      |
| `libwebp`                 | X          | X      |
| `libx11`                  | X          | X      |
| `libxau`                  | X          | X      |
| `libxcb`                  | X          | X      |
| `libxdamage`              | X          | X      |
| `libxdmcp`                | X          | X      |
| `libxext`                 | X          | X      |
| `libxfixes`               | X          | X      |
| `libxft`                  | X          | X      |
| `libxinerama`             | X          | X      |
| `libxkb`                  | X          | X      |
| `libxrender`              | X          | X      |
| `ncurses`                 | X          |        |
| `ncurses-terminfo-base`   | X          |        |
| `netcat-openbsd`          | X          | X      |
| `openssl-config`          | X          | X      |
| `openssl-provider-legacy` | X          | X      |
| `opus`                    | X          | X      |
| `orc`                     | X          | X      |
| `pango`                   | X          | X      |
| `pixman`                  | X          | X      |
| `soxr`                    | X          | X      |
| `speexdsp`                | X          | X      |
| `tdb`                     | X          | X      |
| `ttf-dejavu`              | X          | X      |
| `wget`                    | X          |        |
| `wolfi-baselayout`        | X          | X      |
| `x264`                    | X          | X      |
| `zlib`                    | X          | X      |

