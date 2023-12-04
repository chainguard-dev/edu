---
title: "newrelic-infrastructure-bundle Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public newrelic-infrastructure-bundle Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-12-04 00:17:31
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/newrelic-infrastructure-bundle/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/newrelic-infrastructure-bundle/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/newrelic-infrastructure-bundle/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/newrelic-infrastructure-bundle/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **newrelic-infrastructure-bundle** Image.

## Variants Compared
The **newrelic-infrastructure-bundle** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                        | latest                            |
|--------------|-----------------------------------|-----------------------------------|
| Default User | `root`                            | `root`                            |
| Entrypoint   | `/sbin/tini --`                   | `/sbin/tini --`                   |
| CMD          | `/usr/bin/newrelic-infra-service` | `/usr/bin/newrelic-infra-service` |
| Workdir      | not specified                     | not specified                     |
| Has apk?     | yes                               | no                                |
| Has a shell? | yes                               | no                                |

Check the [tags history page](/chainguard/chainguard-images/reference/newrelic-infrastructure-bundle/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                   | latest-dev | latest |
|-----------------------------------|------------|--------|
| `alsa-lib`                        | X          | X      |
| `apk-tools`                       | X          |        |
| `bash`                            | X          |        |
| `busybox`                         | X          |        |
| `ca-certificates`                 | X          | X      |
| `ca-certificates-bundle`          | X          | X      |
| `fontconfig-config`               | X          | X      |
| `freetype`                        | X          | X      |
| `giflib`                          | X          | X      |
| `git`                             | X          |        |
| `glibc`                           | X          | X      |
| `glibc-locale-posix`              | X          | X      |
| `java-cacerts`                    | X          | X      |
| `java-common`                     | X          | X      |
| `keyutils-libs`                   | X          | X      |
| `kmod`                            | X          | X      |
| `krb5-conf`                       | X          | X      |
| `krb5-libs`                       | X          | X      |
| `lcms2`                           | X          | X      |
| `ld-linux`                        | X          | X      |
| `libbrotlicommon1`                | X          | X      |
| `libbrotlidec1`                   | X          | X      |
| `libbz2-1`                        | X          | X      |
| `libcom_err`                      | X          | X      |
| `libcrypt1`                       | X          |        |
| `libcrypto3`                      | X          | X      |
| `libcurl-openssl4`                | X          |        |
| `libexpat1`                       | X          | X      |
| `libffi`                          | X          | X      |
| `libfontconfig1`                  | X          | X      |
| `libgcc`                          | X          | X      |
| `libjpeg-turbo`                   | X          | X      |
| `libnghttp2-14`                   | X          |        |
| `libpcre2-8-0`                    | X          |        |
| `libpng`                          | X          | X      |
| `libssl3`                         | X          | X      |
| `libstdc++`                       | X          | X      |
| `libtasn1`                        | X          | X      |
| `libverto`                        | X          | X      |
| `libx11`                          | X          | X      |
| `libxau`                          | X          | X      |
| `libxcb`                          | X          | X      |
| `libxcomposite`                   | X          | X      |
| `libxdmcp`                        | X          | X      |
| `libxext`                         | X          | X      |
| `libxi`                           | X          | X      |
| `libxrender`                      | X          | X      |
| `libxtst`                         | X          | X      |
| `libzstd1`                        | X          | X      |
| `ncurses`                         | X          |        |
| `ncurses-terminfo-base`           | X          |        |
| `newrelic-infrastructure-agent`   | X          | X      |
| `newrelic-infrastructure-bundle`  | X          | X      |
| `nri-apache-compat`               | X          | X      |
| `nri-cassandra-compat`            | X          | X      |
| `nri-consul-compat`               | X          | X      |
| `nri-couchbase-compat`            | X          | X      |
| `nri-discovery-kubernetes-compat` | X          | X      |
| `nri-elasticsearch-compat`        | X          | X      |
| `nri-f5-compat`                   | X          | X      |
| `nri-haproxy-compat`              | X          | X      |
| `nri-jmx-compat`                  | X          | X      |
| `nri-kafka-compat`                | X          | X      |
| `nri-memcached-compat`            | X          | X      |
| `nri-mongodb-compat`              | X          | X      |
| `nri-mssql-compat`                | X          | X      |
| `nri-mysql-compat`                | X          | X      |
| `nri-nagios-compat`               | X          | X      |
| `nri-nginx-compat`                | X          | X      |
| `nri-postgresql-compat`           | X          | X      |
| `nri-rabbitmq-compat`             | X          | X      |
| `nri-redis-compat`                | X          | X      |
| `nrjmx`                           | X          | X      |
| `openjdk-17-jre`                  | X          | X      |
| `openjdk-17-jre-base`             | X          | X      |
| `openjdk-8`                       | X          | X      |
| `openjdk-8-default-jvm`           | X          | X      |
| `openjdk-8-jre`                   | X          | X      |
| `openssl-config`                  | X          | X      |
| `p11-kit`                         | X          | X      |
| `p11-kit-trust`                   | X          | X      |
| `tini`                            | X          | X      |
| `wolfi-baselayout`                | X          | X      |
| `xz`                              | X          | X      |
| `zlib`                            | X          | X      |

