---
title: "Image Overview: cert-manager-controller-fips"
linktitle: "cert-manager-controller-fips"
type: "article"
layout: "single"
description: "Overview: cert-manager-controller-fips Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/cert-manager-controller-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cert-manager-controller-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/cert-manager-controller-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cert-manager-controller-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal, wolfi-based images for [Cert Manager](https://cert-manager.io): Provisions and manages TLS certificates in Kubernetes.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/cert-manager-controller-fips:latest
```


<!--body:start-->
## Images
Cert manager is composed of multiple container images. These can be deployed
separately, but are typically deployed together leveraging the official
[helm chart](https://cert-manager.io/docs/installation/helm/).

The chainguard provided images for Cert manager are as follows:

```bash
cgr.dev/chainguard/cert-manager-controller:latest
cgr.dev/chainguard/cert-manager-cainjector:latest
cgr.dev/chainguard/cert-manager-acmesolver:latest
cgr.dev/chainguard/cert-manager-webhook:latest
```

## Deploy using helm
Please refer to the [upstream documentation](https://cert-manager.io/docs/installation/helm/)
for full instructions on how to use and deploy Cert mananager via helm.

Below is an example of how to use the Chainguard images with the helm chart:

```bash
# Replace `--version`` accordingly, refer to helm chart documentation.
helm install \
  cert-manager jetstack/cert-manager \
    --namespace cert-manager \
    --create-namespace \
    --version v1.13.3 \
    --set image.repository=cgr.dev/chainguard/cert-manager-controller \
    --set image.tag=latest \
    --set cainjector.image.repository=cgr.dev/chainguard/cert-manager-cainjector \
    --set cainjector.image.tag=latest \
    --set acmesolver.image.repository=cgr.dev/chainguard/cert-manager-acmesolver \
    --set acmesolver.image.tag=latest \
    --set webhook.image.repository=cgr.dev/chainguard/cert-manager-webhook \
    --set webhook.image.tag=latest \
    --set installCRDs=true
```

> Note, if the required CRDs are not available in the cluster, the helm chart
> will fail if `--set installCRDs=true` is omitted.

<!--body:end-->

