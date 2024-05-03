---
title: "Image Overview: kube-vip-fips"
linktitle: "kube-vip-fips"
type: "article"
layout: "single"
description: "Overview: kube-vip-fips Chainguard Image"
date: 2024-05-03 00:45:55
lastmod: 2024-05-03 00:45:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/kube-vip-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kube-vip-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kube-vip-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kube-vip-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Kubernetes Control Plane Virtual IP and Load-Balancer
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/kube-vip-fips:latest
```


<!--body:start-->
## Usage

## Deployment

kube-vip has [documentation](https://kube-vip.io/docs/installation) covering
deployments. They don't make any reference to helm charts, although there seems
to be one published separately (see section below).

The deploy instructions differ depending on your k8s environment. Refer to
the upstream docs](https://kube-vip.io/docs/installation) for the correct set
of instructions. Be sure to replace the image reference in any manifests to the
Chainguard image.

For reference, [here are some steps](https://github.com/chainguard-images/images/blob/main/images/kube-vip/TESTING.md)
we followed to setup a local test environment using a local k3d cluster.

### Helm

kube-vip publishes a [helm chart](https://artifacthub.io/packages/helm/kube-vip/kube-vip)
for deploying the image. **However**, they have commented out 'tag' in the
[values.yaml](https://github.com/kube-vip/helm-charts/blob/5f24093899db53f7c103bd95b0e41a112bbfb72b/charts/kube-vip/values.yaml#L8):

```bash
image:
  repository: ghcr.io/kube-vip/kube-vip
  pullPolicy: IfNotPresent
  # Overrides the image tag whose default is the chart appVersion.
  # tag: "v0.7.0"
```

If you wish to use this helm chart, you'll need to provide a custom values.yaml
file, which is updated to use the chainguard image and latest tag:

```bash
helm repo add kube-vip https://kube-vip.github.io/helm-charts/
helm install my-kube-vip kube-vip/kube-vip -f my-custom-values.yaml
```

> [!WARNING]
> During testing with the original (non-chainguard) image, we did not have
> much success getting a successful deployment. On occasions, our local k8s
> cluster to become unresponsive. If you are referring to this chart, we would
> advise you to test out in a non-production environment first.
<!--body:end-->

