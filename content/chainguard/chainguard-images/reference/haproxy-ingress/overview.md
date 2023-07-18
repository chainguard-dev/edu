---
title: "Image Overview: haproxy-ingress"
type: "article"
description: "Overview: haproxy-ingress Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "images-reference"
weight: 500
toc: true
---

[cgr.dev/chainguard/haproxy-ingress](https://github.com/chainguard-images/images/tree/main/images/haproxy-ingress)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 18th    | `sha256:fefc7545da365455bd85758482f8768e8dcda37663c2023d6e9c67e491dcd5c2` |
|  `latest`     | July 18th    | `sha256:446d5dada29ac163e9563c9d14f4023f02f7915b55fff0ba4a4921503a7bb965` |
|               | July 12th    | `sha256:b84bc5efbd407665bdbc2849153f63d6ebdd960fd6ac33819063cec8c836c3ce` |
|               | July 7th     | `sha256:a07aaf00a89f6020b9ebd90f1dd22acc00a1d020c989d61dfbff9506ee1142e1` |
|               | July 7th     | `sha256:8b25150d3d7d645e8c343a5e7a578ff191a7466010efa890961e9e26e351c38a` |



# Usage

You can use this image with the [Helm Chart](https://artifacthub.io/packages/helm/haproxy-ingress/haproxy-ingress) of the project:

```shell
helm repo add haproxy-ingress https://haproxy-ingress.github.io/charts

helm repo update

helm install ingress haproxy-ingress/haproxy-ingress \
  --set controller.image.repository="cgr.dev/chainguard/haproxy-ingress" \
  --set controller.image.tag="latest"

kubectl wait --for=condition=ready pod --selector "app.kubernetes.io/name=haproxy-ingress" --timeout=120s
```

