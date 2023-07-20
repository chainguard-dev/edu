---
title: "Image Overview: tigera-operator"
type: "article"
description: "Overview: tigera-operator Chainguard Image"
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

[cgr.dev/chainguard/tigera-operator](https://github.com/chainguard-images/images/tree/main/images/tigera-operator)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 19th    | `sha256:92db7a0fbec89b005453418debc05fabba6be0fb14c818a3092845bb7818f3cd` |
|  `latest`     | July 14th    | `sha256:c57ee9b14679369e4f2fcd0999a46cf591810d06469917a97c1c4ece8cc05d84` |



Minimal Project Calico Tigera Operator Image

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/tigera-operator:latest
```

## Usage

This image is a drop-in replacement for the upstream image.
You can run it using the helm chart with:

```shell
helm repo add projectcalico https://projectcalico.docs.tigera.io/charts
helm repo update

helm install calico projectcalico/tigera-operator \
    --namespace tigera-operator \
    --create-namespace \
    --set autoDiscovery.clusterName=foo \
    --set tigeraOperator.registry=cgr.dev \
    --set tigeraOperator.image=chainguard/tigera-operator \
    --set tigeraOperator.version=latest

kubectl wait --namespace tigera-operator --for=condition=ready pod --selector name=tigera-operator --timeout=120s
```

