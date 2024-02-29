---
title: "Image Overview: sigstore-scaffolding-tsa-createcertchain"
linktitle: "sigstore-scaffolding-tsa-createcertchain"
type: "article"
layout: "single"
description: "Overview: sigstore-scaffolding-tsa-createcertchain Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-02-29 16:25:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/sigstore-scaffolding-tsa-createcertchain/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/sigstore-scaffolding-tsa-createcertchain/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/sigstore-scaffolding-tsa-createcertchain/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/sigstore-scaffolding-tsa-createcertchain/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal Wolfi-based [Sigstore](https://sigstore.dev) images.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/sigstore-scaffolding:latest
```
<!--getting:end-->

<!--body:start-->


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
<!--body:end-->

