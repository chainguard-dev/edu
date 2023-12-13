---
title: "Image Overview: postgres-helm-compat"
linktitle: "postgres-helm-compat"
type: "article"
layout: "single"
description: "Overview: postgres-helm-compat Chainguard Image"
date: 2023-12-13 00:32:10
lastmod: 2023-12-13 00:32:10
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/postgres-helm-compat/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/postgres-helm-compat/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/postgres-helm-compat/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/postgres-helm-compat/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
PostgreSQL image compatible with helm charts.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/postgres-helm-compat:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

This image is a variant of [PostgreSQL](../postgres/README.md) that is compatible with Helm charts.

To install it, use the following values:

```bash
helm install postgresql postgresql --repo oci://registry-1.docker.io/bitnamicharts --values - <<EOF
image:
  registry: cgr.dev
  repository: chainguard/postgres-helm-compat
EOF
```

<!--body:end-->

