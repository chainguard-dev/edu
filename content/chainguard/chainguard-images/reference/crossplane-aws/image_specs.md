---
title: "crossplane-aws Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public crossplane-aws Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/crossplane-aws/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/crossplane-aws/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/crossplane-aws/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/crossplane-aws/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **crossplane-aws** Image.

## Variants Compared
The **crossplane-aws** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest              |
|--------------|---------------------|
| Default User | `nonroot`           |
| Entrypoint   | `/usr/bin/provider` |
| CMD          | not specified       |
| Workdir      | not specified       |
| Has apk?     | no                  |
| Has a shell? | no                  |

Check the [tags history page](/chainguard/chainguard-images/reference/crossplane-aws/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                   | latest |
|-----------------------------------|--------|
| `ca-certificates-bundle`          | X      |
| `crossplane-provider-aws`         | X      |
| `crossplane-provider-aws-family`  | X      |
| `terraform`                       | X      |
| `terraform-compat`                | X      |
| `terraform-local-provider-config` | X      |
| `terraform-provider-aws`          | X      |
| `wolfi-baselayout`                | X      |

