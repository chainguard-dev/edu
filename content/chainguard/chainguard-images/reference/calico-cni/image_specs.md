---
title: "calico-cni Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public calico-cni Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/calico-cni/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/calico-cni/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/calico-cni/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/calico-cni/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **calico-cni** Image.

## Variants Compared
The **calico-cni** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                 |
|--------------|------------------------|
| Default User | `root`                 |
| Entrypoint   | `/opt/cni/bin/install` |
| CMD          | not specified          |
| Workdir      | not specified          |
| Has apk?     | no                     |
| Has a shell? | no                     |

Check the [tags history page](/chainguard/chainguard-images/reference/calico-cni/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                 | latest |
|---------------------------------|--------|
| `ca-certificates-bundle`        | X      |
| `calico-cni`                    | X      |
| `calico-cni-compat`             | X      |
| `cni-plugins-bandwidth`         | X      |
| `cni-plugins-bandwidth-compat`  | X      |
| `cni-plugins-host-local`        | X      |
| `cni-plugins-host-local-compat` | X      |
| `cni-plugins-loopback`          | X      |
| `cni-plugins-loopback-compat`   | X      |
| `cni-plugins-portmap`           | X      |
| `cni-plugins-portmap-compat`    | X      |
| `cni-plugins-tuning`            | X      |
| `cni-plugins-tuning-compat`     | X      |
| `flannel-cni-plugin`            | X      |
| `flannel-cni-plugin-compat`     | X      |
| `wolfi-baselayout`              | X      |

