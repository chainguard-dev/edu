---
title: "Image Overview: flux"
type: "article"
description: "Overview: flux Chainguard Image"
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

[cgr.dev/chainguard/flux](https://github.com/chainguard-images/images/tree/main/images/flux)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 28th    | `sha256:d809f9812816dc3e23fd10434dc9aab68ce483daa54209e1ae8ed06dc33e745a` |
|  `latest`     | July 26th    | `sha256:31f86ecdefb325625c4cdd1e8bbbf967a1906d83289e1ebddd80279ab5153fcc` |



## Get It

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/flux
```

## Using `flux`

The `flux` cli contains various functionality to interact with the flux gitops toolkit components in a running cluster.

> NOTE: Many `flux` commands assume a properly connected `kubectl` context, which isn't usually the case when running through docker.

```bash
# Install the flux gitops toolkit using chainguard images
docker run cgr.dev/chainguard/flux export --registry cgr.dev/chainguard | kubectl apply -f -
```

