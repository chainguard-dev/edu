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
The **newrelic-k8s-events-forwarder** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                            |
|--------------|-----------------------------------|
| Default User | `nonroot`                         |
| Entrypoint   | `/sbin/tini --`                   |
| CMD          | `/usr/bin/newrelic-infra-service` |
| Workdir      | not specified                     |
| Has apk?     | no                                |
| Has a shell? | no                                |

Check the [tags history page](/chainguard/chainguard-images/reference/newrelic-k8s-events-forwarder/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                 | latest |
|---------------------------------|--------|
| `ca-certificates-bundle`        | X      |
| `curl`                          | X      |
| `glibc`                         | X      |
| `glibc-locale-posix`            | X      |
| `ld-linux`                      | X      |
| `libbrotlicommon1`              | X      |
| `libbrotlidec1`                 | X      |
| `libcrypto3`                    | X      |
| `libcurl-openssl4`              | X      |
| `libnghttp2-14`                 | X      |
| `libssl3`                       | X      |
| `newrelic-infrastructure-agent` | X      |
| `openssl-config`                | X      |
| `tini`                          | X      |
| `wolfi-baselayout`              | X      |
| `zlib`                          | X      |

