---
title: "Image Overview: crossplane-aws-cloudwatchlogs"
linktitle: "crossplane-aws-cloudwatchlogs"
type: "article"
layout: "single"
description: "Overview: crossplane-aws-cloudwatchlogs Chainguard Image"
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

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/crossplane-aws-cloudwatchlogs/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/crossplane-aws-cloudwatchlogs/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/crossplane-aws-cloudwatchlogs/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/crossplane-aws-cloudwatchlogs/provenance_info/" >}}
{{</ tabs >}}



These images provide Crossplane providers for AWS.

| Upstream Image | Chainguard Image |
| -------------- | ---------------- |
| `xpkg.upbound.io/upbound/provider-aws` | `cgr.dev/chainguard/crossplane-aws` |
| `xpkg.upbound.io/upbound/provider-aws-iam` | `cgr.dev/chainguard/crossplane-aws-iam` |
| `xpkg.upbound.io/upbound/provider-aws-rds` | `cgr.dev/chainguard/crossplane-aws-rds` |
| `xpkg.upbound.io/upbound/provider-aws-s3` | `cgr.dev/chainguard/crossplane-aws-s3` |

You can use them by following the [AWS Quickstart](https://docs.crossplane.io/latest/getting-started/provider-aws/) and using the Chainguard image instead of the upstream image:

```yaml
apiVersion: pkg.crossplane.io/v1
kind: Provider
metadata:
  name: provider-aws-s3
spec:
  package: cgr.dev/chainguard/crossplane-aws-s3:latest
```

