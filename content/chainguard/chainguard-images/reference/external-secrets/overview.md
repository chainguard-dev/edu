---
title: "Image Overview: external-secrets"
type: "article"
description: "Overview: external-secrets Chainguard Images"
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

`stable` [cgr.dev/chainguard/external-secrets](https://github.com/chainguard-images/images/tree/main/images/external-secrets)
| Tags         | Aliases                                         |
|--------------|-------------------------------------------------|
| `latest`     | `0`, `0.8`, `0.8.3`, `0.8.3-r1`                 |
| `latest-dev` | `0-dev`, `0.8-dev`, `0.8.3-dev`, `0.8.3-r1-dev` |



Minimal External Secrets image 

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/external-secrets:latest
```

## Usage

This image is a drop-in replacement for the upstream image.
You can run it using the helm chart with:

```shell
  
$ helm repo add external-secrets https://charts.external-secrets.io
$ helm install external-secrets \
   external-secrets/external-secrets \
    -n external-secrets \
    --set image.repository=cgr.dev/chainguard/external-secrets  \
    --set image.tag=latest \
    --create-namespace 
    <other configuration parameters here>
```

See the [configuration](https://github.com/external-secrets/external-secrets/tree/main/deploy/charts/external-secrets) docs for more examples.

