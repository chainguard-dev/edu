---
title: "newrelic-prometheus Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public newrelic-prometheus Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/newrelic-prometheus/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/newrelic-prometheus/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/newrelic-prometheus/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/newrelic-prometheus/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **newrelic-prometheus** Image.

## Variants Compared
The **newrelic-prometheus** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                                  |
|--------------|-----------------------------------------|
| Default User | `nonroot`                               |
| Entrypoint   | `/sbin/tini -- /usr/bin/nri-prometheus` |
| CMD          | not specified                           |
| Workdir      | not specified                           |
| Has apk?     | no                                      |
| Has a shell? | yes                                     |

Check the [tags history page](/chainguard/chainguard-images/reference/newrelic-prometheus/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `busybox`                | X      |
| `ca-certificates-bundle` | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `ld-linux`               | X      |
| `libcrypt1`              | X      |
| `nri-prometheus`         | X      |
| `tini`                   | X      |
| `wolfi-baselayout`       | X      |

