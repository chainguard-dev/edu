---
title: "Image Overview: spdx-tools"
linktitle: "spdx-tools"
type: "article"
layout: "single"
description: "Overview: spdx-tools Chainguard Image"
date: 2024-06-01 00:50:07
lastmod: 2024-06-01 00:50:07
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/spdx-tools/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/spdx-tools/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/spdx-tools/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/spdx-tools/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Check SPDX SBOM for validity
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/spdx-tools:latest
```


<!--body:start-->
This image contains the SPDX tool available from here: https://github.com/spdx/tools-java

Using this tool you can verify the SPDX SBOM for validity:

```
docker run -v $(pwd):/tmp cgr.dev/chainguard/spdx-tools:latest Verify /tmp/sbom.json
```

You can also compare docs, "pretty-print" an SPDX SBOM, and more.
<!--body:end-->

