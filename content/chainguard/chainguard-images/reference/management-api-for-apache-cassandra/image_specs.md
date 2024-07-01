---
title: "management-api-for-apache-cassandra Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public management-api-for-apache-cassandra Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-07-01 00:36:20
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/management-api-for-apache-cassandra/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/management-api-for-apache-cassandra/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/management-api-for-apache-cassandra/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/management-api-for-apache-cassandra/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **management-api-for-apache-cassandra** Image.

|              | latest-dev                               | latest                                   |
|--------------|------------------------------------------|------------------------------------------|
| Default User | `cassandra`                              | `cassandra`                              |
| Entrypoint   | `/sbin/tini -g -- /docker-entrypoint.sh` | `/sbin/tini -g -- /docker-entrypoint.sh` |
| CMD          | `mgmtapi`                                | `mgmtapi`                                |
| Workdir      | `/`                                      | `/`                                      |
| Has apk?     | yes                                      | no                                       |
| Has a shell? | yes                                      | yes                                      |

Check the [tags history page](/chainguard/chainguard-images/reference/management-api-for-apache-cassandra/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                                  | latest-dev | latest |
|--------------------------------------------------|------------|--------|
| `apk-tools`                                      | X          |        |
| `bash`                                           | X          | X      |
| `boost-atomic`                                   | X          | X      |
| `boost-filesystem`                               | X          | X      |
| `busybox`                                        | X          | X      |
| `c-ares`                                         | X          | X      |
| `ca-certificates`                                | X          | X      |
| `ca-certificates-bundle`                         | X          | X      |
| `cairo`                                          | X          | X      |
| `cassandra-4.1`                                  | X          | X      |
| `cassandra-4.1-compat`                           | X          | X      |
| `chainguard-baselayout`                          | X          | X      |
| `collectd`                                       | X          | X      |
| `cyrus-sasl`                                     | X          | X      |
| `fontconfig-config`                              | X          | X      |
| `freetype`                                       | X          | X      |
| `fribidi`                                        | X          | X      |
| `gdbm`                                           | X          | X      |
| `gdk-pixbuf`                                     | X          | X      |
| `git`                                            | X          |        |
| `glib`                                           | X          | X      |
| `glibc`                                          | X          | X      |
| `glibc-locale-posix`                             | X          | X      |
| `gpsd`                                           | X          | X      |
| `graphite2`                                      | X          | X      |
| `harfbuzz`                                       | X          | X      |
| `heimdal`                                        | X          | X      |
| `hiredis`                                        | X          | X      |
| `iproute2`                                       | X          | X      |
| `iptables`                                       | X          | X      |
| `java-cacerts`                                   | X          | X      |
| `java-common`                                    | X          | X      |
| `ld-linux`                                       | X          | X      |
| `libatasmart`                                    | X          | X      |
| `libblkid`                                       | X          | X      |
| `libbrotlicommon1`                               | X          | X      |
| `libbrotlidec1`                                  | X          | X      |
| `libbz2-1`                                       | X          | X      |
| `libcap`                                         | X          | X      |
| `libcrypt1`                                      | X          | X      |
| `libcrypto3`                                     | X          | X      |
| `libcurl-openssl4`                               | X          | X      |
| `libdbi`                                         | X          | X      |
| `libedit`                                        | X          | X      |
| `libelf`                                         | X          | X      |
| `libevent`                                       | X          | X      |
| `libexpat1`                                      | X          | X      |
| `libfdisk`                                       | X          | X      |
| `libffi`                                         | X          | X      |
| `libfontconfig1`                                 | X          | X      |
| `libgcc`                                         | X          | X      |
| `libgcrypt`                                      | X          | X      |
| `libgpg-error`                                   | X          | X      |
| `libidn2`                                        | X          | X      |
| `libjpeg-turbo`                                  | X          | X      |
| `libldap`                                        | X          | X      |
| `liblz4-1`                                       | X          | X      |
| `libmemcached`                                   | X          | X      |
| `libmnl`                                         | X          | X      |
| `libmodbus`                                      | X          | X      |
| `libmount`                                       | X          | X      |
| `libnftnl`                                       | X          | X      |
| `libnghttp2-14`                                  | X          | X      |
| `libnotify`                                      | X          | X      |
| `libpcap`                                        | X          | X      |
| `libpcre2-8-0`                                   | X          | X      |
| `libpng`                                         | X          | X      |
| `libpq-16`                                       | X          | X      |
| `libproc-2-0`                                    | X          | X      |
| `libpsl`                                         | X          | X      |
| `librdkafka`                                     | X          | X      |
| `libssl3`                                        | X          | X      |
| `libstdc++`                                      | X          | X      |
| `libtasn1`                                       | X          | X      |
| `libunistring`                                   | X          | X      |
| `libunwind`                                      | X          | X      |
| `libuuid`                                        | X          | X      |
| `libwebp`                                        | X          | X      |
| `libx11`                                         | X          | X      |
| `libxau`                                         | X          | X      |
| `libxcb`                                         | X          | X      |
| `libxcrypt`                                      | X          | X      |
| `libxdmcp`                                       | X          | X      |
| `libxext`                                        | X          | X      |
| `libxft`                                         | X          | X      |
| `libxml2`                                        | X          | X      |
| `libxrender`                                     | X          | X      |
| `libzstd1`                                       | X          | X      |
| `lm-sensors`                                     | X          | X      |
| `management-api-for-apache-cassandra-4.1`        | X          | X      |
| `management-api-for-apache-cassandra-4.1-compat` | X          | X      |
| `metric-collector-for-apache-cassandra`          | X          | X      |
| `mosquitto-libs`                                 | X          | X      |
| `mpdecimal`                                      | X          | X      |
| `ncurses`                                        | X          | X      |
| `ncurses-terminfo-base`                          | X          | X      |
| `net-snmp-agent-libs`                            | X          | X      |
| `net-snmp-libs`                                  | X          | X      |
| `openipmi`                                       | X          | X      |
| `openjdk-11-default-jvm`                         | X          | X      |
| `openjdk-11-jre`                                 | X          | X      |
| `openjdk-11-jre-base`                            | X          | X      |
| `openssl`                                        | X          | X      |
| `openssl-provider-legacy`                        | X          | X      |
| `owfs`                                           | X          | X      |
| `p11-kit`                                        | X          | X      |
| `p11-kit-trust`                                  | X          | X      |
| `pango`                                          | X          | X      |
| `pixman`                                         | X          | X      |
| `procps`                                         | X          | X      |
| `python-3.11`                                    | X          | X      |
| `python-3.11-base`                               | X          | X      |
| `rabbitmq-c`                                     | X          | X      |
| `readline`                                       | X          | X      |
| `rrdtool`                                        | X          | X      |
| `shared-mime-info`                               | X          | X      |
| `sqlite-libs`                                    | X          | X      |
| `systemd`                                        | X          | X      |
| `tiff`                                           | X          | X      |
| `tini`                                           | X          | X      |
| `varnish`                                        | X          | X      |
| `wget`                                           | X          |        |
| `wolfi-baselayout`                               | X          | X      |
| `xz`                                             | X          | X      |
| `yajl`                                           | X          | X      |
| `zlib`                                           | X          | X      |

