---
title: "newrelic-infrastructure-k8s Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public newrelic-infrastructure-k8s Chainguard Image."
date: 2024-02-29 16:25:55
lastmod: 2024-02-29 16:25:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/newrelic-infrastructure-k8s/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/newrelic-infrastructure-k8s/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/newrelic-infrastructure-k8s/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/newrelic-infrastructure-k8s/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **newrelic-infrastructure-k8s** Image.

|              | latest-dev                              | latest                                  |
|--------------|-----------------------------------------|-----------------------------------------|
| Default User | `root`                                  | `root`                                  |
| Entrypoint   | `/sbin/tini -- /usr/bin/newrelic-infra` | `/sbin/tini -- /usr/bin/newrelic-infra` |
| CMD          | not specified                           | not specified                           |
| Workdir      | not specified                           | not specified                           |
| Has apk?     | yes                                     | no                                      |
| Has a shell? | yes                                     | no                                      |

Check the [tags history page](/chainguard/chainguard-images/reference/newrelic-infrastructure-k8s/tags_history/) for the full list of available tags.

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
| `chainguard-baselayout`           | X          | X      |
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
| `libidn2`                         | X          |        |
| `libjpeg-turbo`                   | X          | X      |
| `libnghttp2-14`                   | X          |        |
| `libpcre2-8-0`                    | X          |        |
| `libpng`                          | X          | X      |
| `libpsl`                          | X          |        |
| `libssl3`                         | X          | X      |
| `libstdc++`                       | X          | X      |
| `libtasn1`                        | X          | X      |
| `libunistring`                    | X          |        |
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
| `nri-apache`                      | X          | X      |
| `nri-apache-compat`               | X          | X      |
| `nri-cassandra`                   | X          | X      |
| `nri-cassandra-compat`            | X          | X      |
| `nri-consul`                      | X          | X      |
| `nri-consul-compat`               | X          | X      |
| `nri-couchbase`                   | X          | X      |
| `nri-couchbase-compat`            | X          | X      |
| `nri-discovery-kubernetes`        | X          | X      |
| `nri-discovery-kubernetes-compat` | X          | X      |
| `nri-elasticsearch`               | X          | X      |
| `nri-elasticsearch-compat`        | X          | X      |
| `nri-f5`                          | X          | X      |
| `nri-f5-compat`                   | X          | X      |
| `nri-haproxy`                     | X          | X      |
| `nri-haproxy-compat`              | X          | X      |
| `nri-jmx`                         | X          | X      |
| `nri-jmx-compat`                  | X          | X      |
| `nri-kafka`                       | X          | X      |
| `nri-kafka-compat`                | X          | X      |
| `nri-kubernetes-2.13`             | X          | X      |
| `nri-kubernetes-2.13-compat`      | X          | X      |
| `nri-memcached`                   | X          | X      |
| `nri-memcached-compat`            | X          | X      |
| `nri-mongodb`                     | X          | X      |
| `nri-mongodb-compat`              | X          | X      |
| `nri-mssql`                       | X          | X      |
| `nri-mssql-compat`                | X          | X      |
| `nri-mysql`                       | X          | X      |
| `nri-mysql-compat`                | X          | X      |
| `nri-nagios`                      | X          | X      |
| `nri-nagios-compat`               | X          | X      |
| `nri-nginx`                       | X          | X      |
| `nri-nginx-compat`                | X          | X      |
| `nri-postgresql`                  | X          | X      |
| `nri-postgresql-compat`           | X          | X      |
| `nri-prometheus`                  | X          | X      |
| `nri-rabbitmq`                    | X          | X      |
| `nri-rabbitmq-compat`             | X          | X      |
| `nri-redis`                       | X          | X      |
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
| `wget`                            | X          |        |
| `wolfi-baselayout`                | X          | X      |
| `xz`                              | X          | X      |
| `zlib`                            | X          | X      |

