---
title: "newrelic-k8s-events-forwarder Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public newrelic-k8s-events-forwarder Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/newrelic-k8s-events-forwarder/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/newrelic-k8s-events-forwarder/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/newrelic-k8s-events-forwarder/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/newrelic-k8s-events-forwarder/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **newrelic-k8s-events-forwarder** Image.

## Variants Compared
The **newrelic-k8s-events-forwarder** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

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
| `libnghttp2-14`                 | X          | X      |
| `libpcre2-8-0`                  | X          |        |
| `libssl3`                       | X          | X      |
| `ncurses`                       | X          |        |
| `ncurses-terminfo-base`         | X          |        |
| `newrelic-infrastructure-agent` | X          | X      |
| `openssl-config`                | X          | X      |
| `tini`                          | X          | X      |
| `wolfi-baselayout`              | X          | X      |
| `zlib`                          | X          | X      |

