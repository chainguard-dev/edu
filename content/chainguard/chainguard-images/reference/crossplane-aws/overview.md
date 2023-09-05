---
title: "Image Overview: crossplane-aws"
type: "article"
description: "Overview: crossplane-aws Chainguard Image"
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

[cgr.dev/chainguard/crossplane-aws](https://github.com/chainguard-images/images/tree/main/images/crossplane-aws)

| Tag (s)   | Last Changed  | Digest                                                                    |
|-----------|---------------|---------------------------------------------------------------------------|
|  `latest` | September 4th | `sha256:68a2e7e7f14e3158210fcc623f86bbf0b022583a147c2e9197a73e1e025d93ba` |



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

