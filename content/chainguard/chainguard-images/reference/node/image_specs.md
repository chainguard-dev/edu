---
title: "node Image Variants"
type: "article"
description: "Detailed information about the public node Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "node"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **node** Image.

## Variants Compared
The **node** Chainguard Image currently has 4 public variants: 

- `latest-dev`
- `latest`
- `problem-detector-latest-dev`
- `problem-detector-latest`

The table has detailed information about each of these variants.

|              | latest-dev      | latest          | problem-detector-latest-dev                               | problem-detector-latest                                   |
|--------------|-----------------|-----------------|-----------------------------------------------------------|-----------------------------------------------------------|
| Default User | `node`          | `node`          | `root`                                                    | `root`                                                    |
| Entrypoint   | `/usr/bin/node` | `/usr/bin/node` | `/usr/bin/node-problem-detector`                          | `/usr/bin/node-problem-detector`                          |
| CMD          | `--help`        | `--help`        | `--config.system-log-monitor=/config/kernel-monitor.json` | `--config.system-log-monitor=/config/kernel-monitor.json` |
| Workdir      | `/app`          | `/app`          | not specified                                             | not specified                                             |
| Has apk?     | yes             | no              | no                                                        | no                                                        |
| Has a shell? | yes             | yes             | yes                                                       | yes                                                       |

Check the [tags history page](/chainguard/chainguard-images/reference/node/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                    | latest-dev | latest | problem-detector-latest-dev | problem-detector-latest |
|------------------------------------|------------|--------|-----------------------------|-------------------------|
| `apk-tools`                        | X          |        |                             |                         |
| `bash`                             | X          |        |                             |                         |
| `binutils`                         | X          |        |                             |                         |
| `build-base`                       | X          |        |                             |                         |
| `busybox`                          | X          | X      | X                           | X                       |
| `c-ares`                           | X          | X      |                             |                         |
| `ca-certificates-bundle`           | X          | X      | X                           | X                       |
| `gcc`                              | X          |        |                             |                         |
| `gdbm`                             | X          |        |                             |                         |
| `git`                              | X          |        |                             |                         |
| `glibc`                            | X          | X      | X                           | X                       |
| `glibc-dev`                        | X          |        |                             |                         |
| `glibc-locale-posix`               | X          | X      | X                           | X                       |
| `gmp`                              | X          |        |                             |                         |
| `icu`                              | X          | X      |                             |                         |
| `isl`                              | X          |        |                             |                         |
| `ld-linux`                         | X          | X      | X                           | X                       |
| `libatomic`                        | X          |        |                             |                         |
| `libbrotlicommon1`                 | X          | X      |                             |                         |
| `libbrotlidec1`                    | X          | X      |                             |                         |
| `libbrotlienc1`                    | X          | X      |                             |                         |
| `libbz2-1`                         | X          |        |                             |                         |
| `libcrypt1`                        | X          | X      | X                           | X                       |
| `libcrypto3`                       | X          | X      |                             |                         |
| `libcurl-openssl4`                 | X          |        |                             |                         |
| `libev`                            | X          | X      |                             |                         |
| `libexpat1`                        | X          |        |                             |                         |
| `libffi`                           | X          |        |                             |                         |
| `libgcc`                           | X          | X      |                             |                         |
| `libgo`                            | X          |        |                             |                         |
| `libgomp`                          | X          |        |                             |                         |
| `libnghttp2-14`                    | X          | X      |                             |                         |
| `libpcre2-8-0`                     | X          |        |                             |                         |
| `libssl3`                          | X          | X      |                             |                         |
| `libstdc++`                        | X          | X      |                             |                         |
| `libstdc++-dev`                    | X          |        |                             |                         |
| `linux-headers`                    | X          |        |                             |                         |
| `make`                             | X          |        |                             |                         |
| `mpc`                              | X          |        |                             |                         |
| `mpdecimal`                        | X          |        |                             |                         |
| `mpfr`                             | X          |        |                             |                         |
| `ncurses`                          | X          |        |                             |                         |
| `ncurses-terminfo-base`            | X          |        |                             |                         |
| `nghttp2`                          | X          | X      |                             |                         |
| `nodejs-18`                        | X          | X      |                             |                         |
| `npm`                              | X          | X      |                             |                         |
| `nss-db`                           | X          |        |                             |                         |
| `nss-hesiod`                       | X          |        |                             |                         |
| `openssl-config`                   | X          | X      |                             |                         |
| `pkgconf`                          | X          |        |                             |                         |
| `posix-cc-wrappers`                | X          |        |                             |                         |
| `python-3.11`                      | X          |        |                             |                         |
| `readline`                         | X          |        |                             |                         |
| `sqlite-libs`                      | X          |        |                             |                         |
| `wolfi-baselayout`                 | X          | X      | X                           | X                       |
| `xz`                               | X          |        |                             |                         |
| `yarn`                             | X          |        |                             |                         |
| `zlib`                             | X          | X      |                             |                         |
| `health-checker-0.8`               |            |        | X                           | X                       |
| `libblkid`                         |            |        | X                           | X                       |
| `libcap`                           |            |        | X                           | X                       |
| `libfdisk`                         |            |        | X                           | X                       |
| `libmount`                         |            |        | X                           | X                       |
| `libsystemd`                       |            |        | X                           | X                       |
| `libuuid`                          |            |        | X                           | X                       |
| `log-counter-0.8`                  |            |        | X                           | X                       |
| `node-problem-detector-0.8`        |            |        | X                           | X                       |
| `node-problem-detector-0.8-compat` |            |        | X                           | X                       |
| `systemd`                          |            |        | X                           | X                       |
| `systemd-dev`                      |            |        | X                           | X                       |

