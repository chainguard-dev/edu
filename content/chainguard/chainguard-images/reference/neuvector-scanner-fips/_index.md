---
title: "Image Overview: neuvector-scanner-fips"
linktitle: "neuvector-scanner-fips"
type: "article"
layout: "single"
description: "Overview: neuvector-scanner-fips Chainguard Image"
date: 2024-05-27 00:43:34
lastmod: 2024-05-27 00:43:34
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/neuvector-scanner-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/neuvector-scanner-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/neuvector-scanner-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/neuvector-scanner-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
NeuVector vulnerability scanner for the SUSE NeuVector Container Security Platform
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/neuvector-scanner-fips:latest
```


<!--body:start-->
Add the NeuVector Helm repository to your repositories list:

```shell
helm repo add neuvector https://neuvector.github.io/neuvector-helm/
helm repo update
```

Next, install the NeuVector Scanner with the following command:
```sh
helm install neuvector-scanner neuvector/core \
    --namespace neuvector \
    --create-namespace \
    --set cve.scanner.image.repository=cgr.dev/chainguard/neuvector-scanner \
    --set cve.scanner.image.tag=<set to the latest chainguard tag>
```

Jump to the official [Helm Chart](https://github.com/neuvector/neuvector-helm/blob/master/charts/core/README.md) for more detailed usage.

<!--body:end-->

