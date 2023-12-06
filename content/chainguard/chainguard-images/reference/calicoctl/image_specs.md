---
title: "calicoctl Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public calicoctl Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/calicoctl/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/calicoctl/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/calicoctl/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/calicoctl/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **calicoctl** Image.

## Variants Compared
The **calicoctl** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest               |
|--------------|----------------------|
| Default User | `nonroot`            |
| Entrypoint   | `/usr/bin/calicoctl` |
| CMD          | not specified        |
| Workdir      | not specified        |
| Has apk?     | no                   |
| Has a shell? | no                   |

Check the [tags history page](/chainguard/chainguard-images/reference/calicoctl/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `calicoctl`              | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `ld-linux`               | X      |
| `wolfi-baselayout`       | X      |

