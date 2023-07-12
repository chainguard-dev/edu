---
title: "Image Overview: Haproxy-ingress"
type: "article"
description: "Overview: Haproxy-ingress Chainguard Image"
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

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest`     | 20 hours ago | `sha256:cce9a44002f8073c38120c5c83e6020e40e668e6d660a67130b9e4c0a6020a4c` |
| `latest-dev` | 20 hours ago | `sha256:1c8bd3a6f4d2bab95e8a4e3a6e222140912110c49af2fef233eb490ad75bf7a9` |



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
