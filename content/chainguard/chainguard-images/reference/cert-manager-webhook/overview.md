---
title: "Image Overview: Cert-manager-webhook"
type: "article"
description: "Overview: Cert-manager-webhook Chainguard Image"
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

[cgr.dev/chainguard/cert-manager-webhook](https://github.com/chainguard-images/images/tree/main/images/cert-manager-webhook)


[Cert Manager](https://cert-manager.io/) Automatically provision and manage TLS certificates in Kubernetes

## Get It

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/cert-manager-webhook
```

## Using Cert Manager

This image is part of the `cert-manager` controller stack, and is used following the standard `cert-manager` installation ([here](https://cert-manager.io/docs/installation/)), and replacing them with the Chainguard images.

This image is part of the `cert-manager` stack, and can be used as a drop in replacement for the images following the standard `cert-manager` [installation](https://cert-manager.io/docs/installation/).

For example, we can use these images with the helm installation and the following values:

```yaml
# just this image
webhook:
    image:
        repository: cgr.dev/chainguard/cert-manager-webhook
        tag: latest

# all the images
image:
    repository: cgr.dev/chainguard/cert-manager-controller
    tag: latest
cainjector:
    image:
        repository: cgr.dev/chainguard/cert-manager-cainjector
        tag: latest
acmesolver:
    image:
        repository: cgr.dev/chainguard/cert-manager-acmesolver
        tag: latest
```
