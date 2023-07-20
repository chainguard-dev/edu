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
|  `latest-dev` | July 19th    | `sha256:7894c62366257ec98dc6ab71b31e6d7f5a3c40a955639c9634b7fb748c430027` |
|  `latest`     | July 14th    | `sha256:a7cd3a6872dd11489d78b2f188f380788a03190d641ca8cf7e0c5921041e67a4` |



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

