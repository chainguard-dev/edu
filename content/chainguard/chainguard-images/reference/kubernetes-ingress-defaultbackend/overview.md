---
title: "Image Overview: kubernetes-ingress-defaultbackend"
type: "article"
description: "Overview: kubernetes-ingress-defaultbackend Chainguard Image"
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

[cgr.dev/chainguard/kubernetes-ingress-defaultbackend](https://github.com/chainguard-images/images/tree/main/images/kubernetes-ingress-defaultbackend)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 31st  | `sha256:75becb8bfdb4923a476f9b3b3dbbfbfcab7f07116a28fdbb0a40baa7a8844883` |
|  `latest`     | August 31st  | `sha256:cce9565f89c8e725aaf242dbc0fdbb0e9d2034aabda5be8f4ae0124f5acfaff0` |



Minimal image that acts as a drop-in replacement for the `registry.k8s.io/defaultbackend` image. Used in some ingresses like https://github.com/kubernetes/ingress-gce and https://github.com/kubernetes/ingress-nginx

The image runs as `non-root`.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kubernetes-ingress-defaultbackend:latest
```

You can run it with the standard deployment using nginx-ingress with something like:

```
helm install <RELEASE_NAME> ingress-nginx/ingress-nginx \
  --set defaultBackend.image.registry=cgr.dev/chainguard \
  --set defaultBackend.image.image=kubernetes-ingress-defaultbackend \
  --set defaultBackend.image.tag=latest
```

