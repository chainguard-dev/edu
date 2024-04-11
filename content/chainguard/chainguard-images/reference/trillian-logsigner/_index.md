---
title: "Image Overview: trillian-logsigner"
linktitle: "trillian-logsigner"
type: "article"
layout: "single"
description: "Overview: trillian-logsigner Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/trillian-logsigner/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/trillian-logsigner/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/trillian-logsigner/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/trillian-logsigner/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[Trillian](https://github.com/google/trillian) is a Merkle tree implementation that is used as the backing for various functionalities including Certificate Transparency and the Sigstore Rekor transparency log.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/trillian-logsigner:latest
```


<!--body:start-->
## Sigstore

Trillian is also deployed as part of the sigstore stack.  For more information
on this see [`sigstore-scaffolding`](../sigstore-scaffolding/).
<!--body:end-->

