---
title: "envoy Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public envoy Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/envoy/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/envoy/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/envoy/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/envoy/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **envoy** Image.

## Variants Compared
The **envoy** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                                    |
|--------------|-------------------------------------------|
| Default User | `envoy`                                   |
| Entrypoint   | `/var/lib/envoy/init/envoy-entrypoint.sh` |
| CMD          | not specified                             |
| Workdir      | not specified                             |
| Has apk?     | no                                        |
| Has a shell? | yes                                       |

Check the [tags history page](/chainguard/chainguard-images/reference/envoy/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `busybox`                | X      |
| `ca-certificates-bundle` | X      |
| `envoy`                  | X      |
| `envoy-config`           | X      |
| `envoy-oci-entrypoint`   | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `ld-linux`               | X      |
| `libcrypt1`              | X      |
| `su-exec`                | X      |
| `wolfi-baselayout`       | X      |

