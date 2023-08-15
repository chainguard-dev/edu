---
title: "guacamole-server Image Variants"
type: "article"
description: "Detailed information about the public guacamole-server Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "guacamole-server"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **guacamole-server** Image.

## Variants Compared
The **guacamole-server** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

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
| `libatomic`               | X          | X      |
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
| `libjpeg-turbo`           | X          | X      |
| `libltdl`                 | X          | X      |
| `libmd`                   | X          | X      |
| `libmount`                | X          | X      |
| `libnghttp2-14`           | X          |        |
| `libogg`                  | X          | X      |
| `libpcre2-8-0`            | X          | X      |
| `libpng`                  | X          | X      |
| `libpulse`                | X          | X      |
| `libsndfile`              | X          | X      |
| `libssh2`                 | X          | X      |
| `libssl3`                 | X          | X      |
| `libswresample4`          | X          | X      |
| `libswscale7`             | X          | X      |
| `libtelnet`               | X          | X      |
| `libtheora`               | X          | X      |
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
| `wolfi-baselayout`        | X          | X      |
| `x264`                    | X          | X      |
| `zlib`                    | X          | X      |
