---
title: "Image Overview: trillian-logserver"
linktitle: "trillian-logserver"
type: "article"
layout: "single"
description: "Overview: trillian-logserver Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-11-29 00:31:44
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/trillian-logserver/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/trillian-logserver/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/trillian-logserver/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/trillian-logserver/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[Trillian](https://github.com/google/trillian) is a Merkle tree implementation that is used as the backing for various functionalities including Certificate Transparency and the Sigstore Rekor transparency log.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/trillian:latest
```
<!--getting:end-->

<!--body:start-->
## Sigstore

Trillian is also deployed as part of the sigstore stack.  For more information
on this see [`sigstore-scaffolding`](../sigstore-scaffolding/).
<!--body:end-->

