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
The **crossplane-aws** Chainguard Image currently has 4 public variants: 

- `iam-latest`
- `latest`
- `rds-latest`
- `s3-latest`

The table has detailed information about each of these variants.

|              | iam-latest                | latest                    | rds-latest                | s3-latest                 |
|--------------|---------------------------|---------------------------|---------------------------|---------------------------|
| Default User | `65532`                   | `65532`                   | `65532`                   | `65532`                   |
| Entrypoint   | `/usr/local/bin/provider` | `/usr/local/bin/provider` | `/usr/local/bin/provider` | `/usr/local/bin/provider` |
| CMD          | not specified             | not specified             | not specified             | not specified             |
| Workdir      | not specified             | not specified             | not specified             | not specified             |
| Has apk?     | no                        | no                        | no                        | no                        |
| Has a shell? | no                        | no                        | no                        | no                        |

Check the [tags history page](/chainguard/chainguard-images/reference/crossplane-aws/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                   | iam-latest | latest | rds-latest | s3-latest |
|-----------------------------------|------------|--------|------------|-----------|
| `ca-certificates-bundle`          | X          | X      | X          | X         |
| `crossplane-provider-aws`         | X          | X      | X          | X         |
| `crossplane-provider-aws-iam`     | X          |        |            |           |
| `terraform`                       | X          | X      | X          | X         |
| `terraform-compat`                | X          | X      | X          | X         |
| `terraform-local-provider-config` | X          | X      | X          | X         |
| `terraform-provider-aws`          | X          | X      | X          | X         |
| `wolfi-baselayout`                | X          | X      | X          | X         |
| `crossplane-provider-aws-family`  |            | X      |            |           |
| `crossplane-provider-aws-rds`     |            |        | X          |           |
| `crossplane-provider-aws-s3`      |            |        |            | X         |

