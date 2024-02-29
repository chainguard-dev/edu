---
title: "Image Overview: trillian-logsigner-fips"
linktitle: "trillian-logsigner-fips"
type: "article"
layout: "single"
description: "Overview: trillian-logsigner-fips Chainguard Image"
date: 2024-02-29 16:25:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/trillian-logsigner-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/trillian-logsigner-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/trillian-logsigner-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/trillian-logsigner-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[Trillian](https://github.com/google/trillian) is a Merkle tree implementation that is used as the backing for various functionalities including Certificate Transparency and the Sigstore Rekor transparency log.
<!--overview:end-->

<!--getting:start-->
## Download this Image
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

