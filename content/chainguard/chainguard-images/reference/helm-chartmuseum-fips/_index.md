---
title: "Image Overview: helm-chartmuseum-fips"
linktitle: "helm-chartmuseum-fips"
type: "article"
layout: "single"
description: "Overview: helm-chartmuseum-fips Chainguard Image"
date: 2024-07-02 00:32:13
lastmod: 2024-07-02 00:32:13
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/helm-chartmuseum-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/helm-chartmuseum-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/helm-chartmuseum-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/helm-chartmuseum-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image with [chartmuseum](https://github.com/helm/chartmuseum) binary.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/helm-chartmuseum-fips:latest
```


<!--body:start-->
## Usage

Create a helm chart, and package it into a `charts/` directory:

```
helm create hello
mkdir charts/
helm package hello -d ./charts
```

Start the chartmuseum server:

```
docker run --rm -p 8080:8080 -v $(pwd)/charts:/charts \
  cgr.dev/chainguard/chartmuseum:latest
```

From another terminal, use it as a helm repository:
```
helm repo add chartmuseum http://localhost:8080
helm search repo chartmuseum/
helm upgrade --install chartmuseum-demo chartmuseum/hello
```
<!--body:end-->

