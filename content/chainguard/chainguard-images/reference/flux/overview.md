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
|  `latest-dev` | August 31st  | `sha256:fd73c8545989e3dfd81ae12d623b195eb4794f9d82e9a6c541e02bd91f1f5dd2` |
|  `latest`     | August 31st  | `sha256:00d5f0a6453a68d6f731e34a6d7e7be1f6961ceaa611379da9ef8633bf041534` |



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

