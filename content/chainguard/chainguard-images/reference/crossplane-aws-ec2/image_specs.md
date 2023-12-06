---
title: "crossplane-aws-ec2 Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public crossplane-aws-ec2 Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/crossplane-aws-ec2/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/crossplane-aws-ec2/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/crossplane-aws-ec2/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/crossplane-aws-ec2/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **crossplane-aws-ec2** Image.

## Variants Compared
The **crossplane-aws-ec2** Chainguard Image currently has one public variant: 

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

Check the [tags history page](/chainguard/chainguard-images/reference/crossplane-aws-ec2/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                   | latest |
|-----------------------------------|--------|
| `ca-certificates-bundle`          | X      |
| `crossplane-provider-aws`         | X      |
| `crossplane-provider-aws-ec2`     | X      |
| `terraform`                       | X      |
| `terraform-compat`                | X      |
| `terraform-local-provider-config` | X      |
| `terraform-provider-aws`          | X      |
| `wolfi-baselayout`                | X      |

