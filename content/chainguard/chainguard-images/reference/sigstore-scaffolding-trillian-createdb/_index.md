---
title: "Image Overview: sigstore-scaffolding-trillian-createdb"
linktitle: "sigstore-scaffolding-trillian-createdb"
type: "article"
layout: "single"
description: "Overview: sigstore-scaffolding-trillian-createdb Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/sigstore-scaffolding-trillian-createdb/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/sigstore-scaffolding-trillian-createdb/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/sigstore-scaffolding-trillian-createdb/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/sigstore-scaffolding-trillian-createdb/provenance_info/" >}}
{{</ tabs >}}



## Minimal Wolfi-based [Sigstore](https://sigstore.dev) images.

The images in this directory are just the "glue" for bootstrapping the stack,
but Chainguard offers minimal images for each of the elements needed by the
[Sigstore "scaffold" Helm chart](https://github.com/sigstore/helm-charts/tree/main/charts/scaffold)
for bootstrapping a full sigstore stack.

In addition to these images, the stack also pulls in images from:
- [`cosign`](../cosign)
- [`fulcio`](../fulcio/)
- [`rekor`](../rekor)
- [`trillian`](../trillian)
- [`ctlog`](../ctlog)
- (NYI) `timestamp-authority` (an optional component only used in some setups)

The stack also pulls in several support images:
- [`curl`](../curl)
- [`netcat`](../netcat)
- [`redis`](../redis)
- (NYI) `mysql` - Currently sigstore relies on the nearly EOL `mysql` 5.7

To see an example of how we substitute images into the `scaffold` Helm chart's
`values.yaml` see our [`values.tf`](./tests/values.tf) example.

