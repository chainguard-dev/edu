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
|  `latest`     | August 15th  | `sha256:a65e698e9d2c8d7f298e8530507be8e7ac5eac397e3c3171661ce79f0a4690ce` |
|  `latest-dev` | August 15th  | `sha256:456fab5160ab26db221dc983071ca13bcb9c7ea06189c08b06ced918bb0d6380` |



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

