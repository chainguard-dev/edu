---
title: "Image Overview: crossplane-azure-storage"
linktitle: "crossplane-azure-storage"
type: "article"
layout: "single"
description: "Overview: crossplane-azure-storage Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu: 
  docs: 
    parent: "images-reference"
weight: 500
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/crossplane-azure-storage/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/crossplane-azure-storage/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/crossplane-azure-storage/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/crossplane-azure-storage/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Crossplane lets you build a control plane with Kubernetes-style declarative and API-driven configuration and management for anything
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/crossplane-azure-storage:latest
```


<!--body:start-->
These images provide Crossplane providers for Azure.

| Upstream Image | Chainguard Image |
| -------------- | ---------------- |
| `xpkg.upbound.io/upbound/provider-azure` | `cgr.dev/chainguard/crossplane-azure` |
| `xpkg.upbound.io/upbound/provider-azure-authorization` | `cgr.dev/chainguard/crossplane-azure-authorization` |
| `xpkg.upbound.io/upbound/provider-azure-managedidentity` | `cgr.dev/chainguard/crossplane-azure-managedidentity` |
| `xpkg.upbound.io/upbound/provider-azure-sql` | `cgr.dev/chainguard/crossplane-azure-sql` |
| `xpkg.upbound.io/upbound/provider-azure-storage` | `cgr.dev/chainguard/crossplane-azure-storage` |

You can use them by following the [Azure Quickstart](https://docs.crossplane.io/latest/getting-started/provider-azure/) and using the Chainguard image instead of the upstream image:

```yaml
apiVersion: pkg.crossplane.io/v1
kind: Provider
metadata:
  name: provider-azure-sql
spec:
  package: cgr.dev/chainguard/crossplane-azure-sql:latest
```
<!--body:end-->

