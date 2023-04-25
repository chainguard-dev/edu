---
title: "Image Overview: helm-controller"
type: "article"
description: "Overview: helm-controller Chainguard Images"
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

`experimental` [cgr.dev/chainguard/helm-controller](https://github.com/chainguard-images/images/tree/main/images/helm-controller)
| Tags         | Aliases                                            |
|--------------|----------------------------------------------------|
| `latest`     | `0`, `0.32`, `0.32.2`, `0.32.2-r0`                 |
| `latest-dev` | `0-dev`, `0.32-dev`, `0.32.2-dev`, `0.32.2-r0-dev` |



## Get It

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/helm-controller
```

## Using `helm-controller`

The `helm-controller` is part of the flux gitops toolkit components ([docs](https://fluxcd.io/flux/components/)). It is recommended to use this component in conjunction with the remaining toolkit components during install.

Although there are multiple methods of [installing](https://fluxcd.io/flux/installation/), the example below will work using the `flux` cli, also available as a chainguard image (cgr.dev/chainguard/flux):

> NOTE: Installation assumes a properly connected `kubectl`

```bash
# Using a pre-installed flux cli
flux install --registry cgr.dev/chainguard

# OR using the provided flux chainguard image
docker run cgr.dev/chainguard/flux export --registry cgr.dev/chainguard | kubectl apply -f -
```

