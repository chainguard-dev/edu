---
title: "ingress-nginx-controller-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public ingress-nginx-controller-fips Chainguard Image."
date: 2024-02-29 16:25:55
lastmod: 2024-02-29 16:25:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/ingress-nginx-controller-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **ingress-nginx-controller-fips** Image.

|              | latest-dev                  | latest                      |
|--------------|-----------------------------|-----------------------------|
| Default User | `root`                      | `root`                      |
| Entrypoint   | `/nginx-ingress-controller` | `/nginx-ingress-controller` |
| CMD          | `/usr/bin/dumb-init ---`    | `/usr/bin/dumb-init ---`    |
| Workdir      | `/etc/nginx`                | `/etc/nginx`                |
| Has apk?     | yes                         | no                          |
| Has a shell? | yes                         | no                          |

Check the [tags history page](/chainguard/chainguard-images/reference/ingress-nginx-controller-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                        | latest-dev | latest |
|----------------------------------------|------------|--------|
| `aom-libs`                             | X          | X      |
| `apk-tools`                            | X          |        |
| `bash`                                 | X          |        |
| `brotli`                               | X          | X      |
| `busybox`                              | X          |        |
| `ca-certificates`                      | X          | X      |
| `ca-certificates-bundle`               | X          | X      |
| `chainguard-baselayout`                | X          | X      |
| `curl`                                 | X          | X      |
| `fontconfig-config`                    | X          | X      |
| `freetype`                             | X          | X      |
| `gd`                                   | X          | X      |
| `geoip`                                | X          | X      |
| `git`                                  | X          |        |
| `glibc`                                | X          | X      |
| `glibc-locale-posix`                   | X          | X      |
| `ingress-nginx-controller-fips`        | X          | X      |
| `ingress-nginx-controller-fips-compat` | X          | X      |
| `ld-linux`                             | X          | X      |
| `libavif`                              | X          | X      |
| `libbrotlicommon1`                     | X          | X      |
| `libbrotlidec1`                        | X          | X      |
| `libbrotlienc1`                        | X          | X      |
| `libbz2-1`                             | X          | X      |
| `libcrypt1`                            | X          | X      |
| `libcrypto3`                           | X          | X      |
| `libcurl-openssl4`                     | X          | X      |
| `libdav1d`                             | X          | X      |
| `libedit`                              | X          | X      |
| `libexpat1`                            | X          | X      |
| `libfontconfig1`                       | X          | X      |
| `libgcc`                               | X          | X      |
| `libgcrypt`                            | X          | X      |
| `libgd`                                | X          | X      |
| `libgpg-error`                         | X          | X      |
| `libidn2`                              | X          | X      |
| `libjpeg-turbo`                        | X          | X      |
| `libmaxminddb`                         | X          | X      |
| `libmaxminddb-libs`                    | X          | X      |
| `libnghttp2-14`                        | X          | X      |
| `libpcre2-8-0`                         | X          |        |
| `libpng`                               | X          | X      |
| `libpsl`                               | X          | X      |
| `libssl3`                              | X          | X      |
| `libstdc++`                            | X          | X      |
| `libunistring`                         | X          | X      |
| `libwebp`                              | X          | X      |
| `libx11`                               | X          | X      |
| `libxau`                               | X          | X      |
| `libxcb`                               | X          | X      |
| `libxdmcp`                             | X          | X      |
| `libxml2`                              | X          | X      |
| `libxpm`                               | X          | X      |
| `libxslt`                              | X          | X      |
| `libzstd1`                             | X          | X      |
| `lua-cjson`                            | X          | X      |
| `lua-resty-balancer`                   | X          | X      |
| `lua-resty-cache`                      | X          | X      |
| `lua-resty-cookie`                     | X          | X      |
| `lua-resty-core`                       | X          | X      |
| `lua-resty-dns`                        | X          | X      |
| `lua-resty-global-throttle`            | X          | X      |
| `lua-resty-http`                       | X          | X      |
| `lua-resty-ipmatcher`                  | X          | X      |
| `lua-resty-lock`                       | X          | X      |
| `lua-resty-memcached`                  | X          | X      |
| `lua-resty-redis`                      | X          | X      |
| `lua-resty-string`                     | X          | X      |
| `lua-resty-upload`                     | X          | X      |
| `luajit`                               | X          | X      |
| `mimalloc`                             | X          | X      |
| `modsecurity`                          | X          | X      |
| `modsecurity-config`                   | X          | X      |
| `msgpack-cxx`                          | X          | X      |
| `ncurses`                              | X          | X      |
| `ncurses-terminfo-base`                | X          | X      |
| `openssh-client`                       | X          | X      |
| `openssl`                              | X          | X      |
| `openssl-config-fipshardened`          | X          | X      |
| `openssl-dev`                          | X          | X      |
| `openssl-provider-fips`                | X          | X      |
| `openssl-provider-legacy`              | X          | X      |
| `pcre`                                 | X          | X      |
| `ssdeep`                               | X          | X      |
| `tiff`                                 | X          | X      |
| `wget`                                 | X          |        |
| `wolfi-baselayout`                     | X          | X      |
| `xz`                                   | X          | X      |
| `yaml-cpp`                             | X          | X      |
| `zlib`                                 | X          | X      |

