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

| Tag (s)       | Last Changed   | Digest                                                                    |
|---------------|----------------|---------------------------------------------------------------------------|
|  `latest`     | September 11th | `sha256:7c35df5abaa0aad56400f209c679e8ab5f3701b313b4f5b6560e51b34e65862c` |
|  `latest-dev` | September 11th | `sha256:922e5b6186e83f6fca2f6b61985d7fead5240dc55e4f7643a67ec709ea59fe68` |



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

