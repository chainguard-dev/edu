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

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 7th | `sha256:5ae5c5bd2e2b5cd5da11827dbbf81e1e1f909cac4c2f924b42259662651b99f6` |
|  `latest`     | September 7th | `sha256:3de26adb05f0fb848d4778de6d223431b4db3c858a99d068a25dd83826cf84b7` |



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

