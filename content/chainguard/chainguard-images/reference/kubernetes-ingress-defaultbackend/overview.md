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
|  `latest-dev` | July 18th    | `sha256:56db2bdd1dbf9aa27a239e9c49583f50987e7d80c858607f8c0c7c479c18db25` |
|  `latest`     | July 14th    | `sha256:ff5690ee4e44dbada5aea757068c0273b9b69bb2f402b7affbce5e107193a884` |
|               | July 12th    | `sha256:681aff826ec3444a4357c4b4a4619e362b46ec2c8b986e584e9057e4f13d7902` |
|               | July 7th     | `sha256:05a3b1164328ced4bc1da095b4705718097e32949a623959e544155505e3405d` |
|               | July 7th     | `sha256:1dede93c46813b501d52c90d02f53be1c92196f71e92211ba1218663872c0390` |
|               | July 3rd     | `sha256:78b73f5e7e2b35e9b4312cb1e034b073371a5916e65645f232cc08b443c3be1d` |
|               | June 26th    | `sha256:d68b7033405b64e2e5521a53a383df6870de5eb8a0bf7b5036c3f9a394e66a65` |



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

