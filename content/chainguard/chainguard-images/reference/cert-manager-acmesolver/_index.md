---
title: "Image Overview: cert-manager-acmesolver"
linktitle: "cert-manager-acmesolver"
type: "article"
layout: "single"
description: "Overview: cert-manager-acmesolver Chainguard Image"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/cert-manager-acmesolver/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/cert-manager-acmesolver/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/cert-manager-acmesolver/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cert-manager-acmesolver/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[Cert Manager](https://cert-manager.io/) Automatically provision and manage TLS certificates in Kubernetes
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/cert-manager:latest
```
<!--getting:end-->

<!--body:start-->
## Using Cert Manager

These set of images are a drop in replacement for the standard `cert-manager` installation ([here](https://cert-manager.io/docs/installation/)), and replacing them with the Chainguard images.

For example, we can use these images with the helm installation and the following values:

```yaml
image:
    repository: cgr.dev/chainguard/cert-manager-controller
    tag: latest

cainjector:
    image:
        repository: cgr.dev/chainguard/cert-manager-cainjector
        tag: latest
acmesolver:
    image:
        repository: cgr.dev/chainguard/cert-manager-acmesolver
        tag: latest
webhook:
    image:
        repository: cgr.dev/chainguard/cert-manager-webhook
        tag: latest
```
<!--body:end-->

