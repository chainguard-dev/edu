---
title: "kyverno-cli Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public kyverno-cli Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-01-08 00:20:41
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kyverno-cli/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/kyverno-cli/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kyverno-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kyverno-cli/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **kyverno-cli** Image.

## Variants Compared
The **kyverno-cli** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                     |
|--------------|----------------------------|
| Default User | `nonroot`                  |
| Entrypoint   | `/usr/bin/kubectl-kyverno` |
| CMD          | not specified              |
| Workdir      | not specified              |
| Has apk?     | no                         |
| Has a shell? | no                         |

Check the [tags history page](/chainguard/chainguard-images/reference/kyverno-cli/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `kubectl-1.28`           | X      |
| `kubectl-latest`         | X      |
| `kyverno-cli`            | X      |
| `wolfi-baselayout`       | X      |

