---
title: "Image Overview: crossplane-azure"
type: "article"
description: "{{ description }}"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "images-reference"
weight: 500
toc: true
---



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

