---
title: "newrelic-k8s-events-forwarder Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public newrelic-k8s-events-forwarder Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-02-29 16:25:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/newrelic-k8s-events-forwarder/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/newrelic-k8s-events-forwarder/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/newrelic-k8s-events-forwarder/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/newrelic-k8s-events-forwarder/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **newrelic-k8s-events-forwarder** Image.

|              | latest-dev                        | latest                            |
|--------------|-----------------------------------|-----------------------------------|
| Default User | `nonroot`                         | `nonroot`                         |
| Entrypoint   | `/sbin/tini --`                   | `/sbin/tini --`                   |
| CMD          | `/usr/bin/newrelic-infra-service` | `/usr/bin/newrelic-infra-service` |
| Workdir      | not specified                     | not specified                     |
| Has apk?     | yes                               | no                                |
| Has a shell? | yes                               | no                                |

Check the [tags history page](/chainguard/chainguard-images/reference/newrelic-k8s-events-forwarder/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                 | latest-dev | latest |
|---------------------------------|------------|--------|
| `apk-tools`                     | X          |        |
| `bash`                          | X          |        |
| `busybox`                       | X          |        |
| `ca-certificates-bundle`        | X          | X      |
| `chainguard-baselayout`         | X          | X      |
| `curl`                          | X          | X      |
| `git`                           | X          |        |
| `glibc`                         | X          | X      |
| `glibc-locale-posix`            | X          | X      |
| `ld-linux`                      | X          | X      |
| `libbrotlicommon1`              | X          | X      |
| `libbrotlidec1`                 | X          | X      |
| `libcrypt1`                     | X          |        |
| `libcrypto3`                    | X          | X      |
| `libcurl-openssl4`              | X          | X      |
| `libexpat1`                     | X          |        |
| `libidn2`                       | X          | X      |
| `libnghttp2-14`                 | X          | X      |
| `libpcre2-8-0`                  | X          |        |
| `libpsl`                        | X          | X      |
| `libssl3`                       | X          | X      |
| `libunistring`                  | X          | X      |
| `ncurses`                       | X          |        |
| `ncurses-terminfo-base`         | X          |        |
| `newrelic-infrastructure-agent` | X          | X      |
| `openssl-config`                | X          | X      |
| `tini`                          | X          | X      |
| `wget`                          | X          |        |
| `wolfi-baselayout`              | X          | X      |
| `zlib`                          | X          | X      |

