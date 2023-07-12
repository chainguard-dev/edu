---
title: "Image Overview: Flux"
type: "article"
description: "Overview: Flux Chainguard Image"
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

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest-dev` | 20 hours ago | `sha256:6524cb1b94edf76539c8cae72e70995a172c1d6aff17321cb5721e9f6b077882` |
| `latest`     | 20 hours ago | `sha256:bd78e62f5bcb7ad9603abd79df7e9361f5480b05cc7b6768a7e2eb2d33895fe0` |



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
