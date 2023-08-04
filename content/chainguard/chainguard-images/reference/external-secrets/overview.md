---
title: "Image Overview: external-secrets"
type: "article"
description: "Overview: external-secrets Chainguard Image"
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

[cgr.dev/chainguard/external-secrets](https://github.com/chainguard-images/images/tree/main/images/external-secrets)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 3rd   | `sha256:d7eed46bf731211d438f63fcf26b57e97dac347d2c5eb7e6c432786f1540f7db` |
|  `latest`     | July 26th    | `sha256:0cbec0fab60fb39a01fe834f6a278205b8e2991aead30001c21607d42aebea07` |



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

