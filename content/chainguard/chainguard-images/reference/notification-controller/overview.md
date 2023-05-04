---
title: "Image Overview: notification-controller"
type: "article"
description: "Overview: notification-controller Chainguard Images"
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

`experimental` [cgr.dev/chainguard/notification-controller](https://github.com/chainguard-images/images/tree/main/images/notification-controller)
| Tags         | Aliases                                            |
|--------------|----------------------------------------------------|
| `latest`     | `0`, `0.33`, `0.33.0`, `0.33.0-r1`                 |
| `latest-dev` | `0-dev`, `0.33-dev`, `0.33.0-dev`, `0.33.0-r1-dev` |



## Get It

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/notification-controller
```

## Using `notification-controller`

The `notification-controller` is part of the flux gitops toolkit components ([docs](https://fluxcd.io/flux/components/)). It is recommended to use this component in conjunction with the remaining toolkit components during install.

Although there are multiple methods of [installing](https://fluxcd.io/flux/installation/), the example below demonstrates using the `flux` cli, also available as a chainguard image (`cgr.dev/chainguard/flux`):

> NOTE: Installation assumes a properly connected `kubectl` context.

```bash
# Using a pre-installed flux cli
flux install --registry cgr.dev/chainguard

# OR using the provided flux chainguard image
docker run cgr.dev/chainguard/flux export --registry cgr.dev/chainguard | kubectl apply -f -
```

