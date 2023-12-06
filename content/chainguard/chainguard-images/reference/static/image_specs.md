---
title: "static Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public static Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/static/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/static/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/static/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/static/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **static** Image.

## Variants Compared
The **static** Chainguard Image currently has 2 public variants: 

- `latest-glibc`
- `latest`

The table has detailed information about each of these variants.

|              | latest-glibc  | latest        |
|--------------|---------------|---------------|
| Default User | `nonroot`     | `nonroot`     |
| Entrypoint   | not specified | not specified |
| CMD          | not specified | not specified |
| Workdir      | not specified | not specified |
| Has apk?     | no            | no            |
| Has a shell? | no            | no            |

Check the [tags history page](/chainguard/chainguard-images/reference/static/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-glibc | latest |
|--------------------------|--------------|--------|
| `ca-certificates-bundle` | X            | X      |
| `tzdata`                 | X            | X      |
| `wolfi-baselayout`       | X            |        |
| `alpine-baselayout-data` |              | X      |
| `alpine-keys`            |              | X      |
| `alpine-release`         |              | X      |

