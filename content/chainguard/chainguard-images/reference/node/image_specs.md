---
title: "node Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public node Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/node/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/node/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/node/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/node/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **node** Image.

## Variants Compared
The **node** Chainguard Image currently has 6 public variants: 

- `latest-dev`
- `latest`
- `problem-detector-latest-dev`
- `problem-detector-latest`
- `nodetaint-latest-dev`
- `nodetaint-latest`

The table has detailed information about each of these variants.

|              | latest-dev      | latest          | problem-detector-latest-dev                               | problem-detector-latest                                   | nodetaint-latest-dev | nodetaint-latest     |
|--------------|-----------------|-----------------|-----------------------------------------------------------|-----------------------------------------------------------|----------------------|----------------------|
| Default User | `65532`         | `65532`         | `0`                                                       | `0`                                                       | `65532`              | `65532`              |
| Entrypoint   | `/usr/bin/node` | `/usr/bin/node` | `/usr/bin/node-problem-detector`                          | `/usr/bin/node-problem-detector`                          | `/usr/bin/nodetaint` | `/usr/bin/nodetaint` |
| CMD          | `--help`        | `--help`        | `--config.system-log-monitor=/config/kernel-monitor.json` | `--config.system-log-monitor=/config/kernel-monitor.json` | not specified        | not specified        |
| Workdir      | `/app`          | `/app`          | not specified                                             | not specified                                             | not specified        | not specified        |
| Has apk?     | yes             | no              | no                                                        | no                                                        | yes                  | no                   |
| Has a shell? | yes             | yes             | yes                                                       | yes                                                       | yes                  | no                   |

Check the [tags history page](/chainguard/chainguard-images/reference/node/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                    | latest-dev | latest | problem-detector-latest-dev | problem-detector-latest | nodetaint-latest-dev | nodetaint-latest |
|------------------------------------|------------|--------|-----------------------------|-------------------------|----------------------|------------------|
| `apk-tools`                        | X          |        |                             |                         | X                    |                  |
| `bash`                             | X          |        |                             |                         | X                    |                  |
| `binutils`                         | X          |        |                             |                         |                      |                  |
| `build-base`                       | X          |        |                             |                         |                      |                  |
| `busybox`                          | X          | X      | X                           | X                       | X                    |                  |
| `c-ares`                           | X          | X      |                             |                         |                      |                  |
| `ca-certificates-bundle`           | X          | X      | X                           | X                       | X                    | X                |
| `gcc`                              | X          |        |                             |                         |                      |                  |
| `gdbm`                             | X          |        |                             |                         |                      |                  |
| `git`                              | X          |        |                             |                         | X                    |                  |
| `glibc`                            | X          | X      | X                           | X                       | X                    |                  |
| `glibc-dev`                        | X          |        |                             |                         |                      |                  |
| `glibc-locale-posix`               | X          | X      | X                           | X                       | X                    |                  |
| `gmp`                              | X          |        |                             |                         |                      |                  |
| `icu`                              | X          | X      |                             |                         |                      |                  |
| `isl`                              | X          |        |                             |                         |                      |                  |
| `ld-linux`                         | X          | X      | X                           | X                       | X                    |                  |
| `libatomic`                        | X          |        |                             |                         |                      |                  |
| `libbrotlicommon1`                 | X          | X      |                             |                         | X                    |                  |
| `libbrotlidec1`                    | X          | X      |                             |                         | X                    |                  |
| `libbrotlienc1`                    | X          | X      |                             |                         |                      |                  |
| `libbz2-1`                         | X          |        |                             |                         |                      |                  |
| `libcrypt1`                        | X          | X      | X                           | X                       | X                    |                  |
| `libcrypto3`                       | X          | X      |                             |                         | X                    |                  |
| `libcurl-openssl4`                 | X          |        |                             |                         | X                    |                  |
| `libev`                            | X          | X      |                             |                         |                      |                  |
| `libexpat1`                        | X          |        |                             |                         | X                    |                  |
| `libffi`                           | X          |        |                             |                         |                      |                  |
| `libgcc`                           | X          | X      |                             |                         |                      |                  |
| `libgo`                            | X          |        |                             |                         |                      |                  |
| `libgomp`                          | X          |        |                             |                         |                      |                  |
| `libnghttp2-14`                    | X          | X      |                             |                         | X                    |                  |
| `libpcre2-8-0`                     | X          |        |                             |                         | X                    |                  |
| `libssl3`                          | X          | X      |                             |                         | X                    |                  |
| `libstdc++`                        | X          | X      |                             |                         |                      |                  |
| `libstdc++-dev`                    | X          |        |                             |                         |                      |                  |
| `linux-headers`                    | X          |        |                             |                         |                      |                  |
| `make`                             | X          |        |                             |                         |                      |                  |
| `mpc`                              | X          |        |                             |                         |                      |                  |
| `mpdecimal`                        | X          |        |                             |                         |                      |                  |
| `mpfr`                             | X          |        |                             |                         |                      |                  |
| `ncurses`                          | X          |        |                             |                         | X                    |                  |
| `ncurses-terminfo-base`            | X          |        |                             |                         | X                    |                  |
| `nghttp2`                          | X          | X      |                             |                         |                      |                  |
| `nodejs-18`                        | X          | X      |                             |                         |                      |                  |
| `npm`                              | X          | X      |                             |                         |                      |                  |
| `nss-db`                           | X          |        |                             |                         |                      |                  |
| `nss-hesiod`                       | X          |        |                             |                         |                      |                  |
| `openssl-config`                   | X          | X      |                             |                         | X                    |                  |
| `pkgconf`                          | X          |        |                             |                         |                      |                  |
| `posix-cc-wrappers`                | X          |        |                             |                         |                      |                  |
| `python-3.11`                      | X          |        |                             |                         |                      |                  |
| `readline`                         | X          |        |                             |                         |                      |                  |
| `sqlite-libs`                      | X          |        |                             |                         |                      |                  |
| `wolfi-baselayout`                 | X          | X      | X                           | X                       | X                    | X                |
| `xz`                               | X          |        |                             |                         |                      |                  |
| `yarn`                             | X          |        |                             |                         |                      |                  |
| `zlib`                             | X          | X      |                             |                         | X                    |                  |
| `health-checker-0.8`               |            |        | X                           | X                       |                      |                  |
| `libblkid`                         |            |        | X                           | X                       |                      |                  |
| `libcap`                           |            |        | X                           | X                       |                      |                  |
| `libfdisk`                         |            |        | X                           | X                       |                      |                  |
| `libmount`                         |            |        | X                           | X                       |                      |                  |
| `libsystemd`                       |            |        | X                           | X                       |                      |                  |
| `libuuid`                          |            |        | X                           | X                       |                      |                  |
| `log-counter-0.8`                  |            |        | X                           | X                       |                      |                  |
| `node-problem-detector-0.8`        |            |        | X                           | X                       |                      |                  |
| `node-problem-detector-0.8-compat` |            |        | X                           | X                       |                      |                  |
| `systemd`                          |            |        | X                           | X                       |                      |                  |
| `systemd-dev`                      |            |        | X                           | X                       |                      |                  |
| `nodetaint`                        |            |        |                             |                         | X                    | X                |

