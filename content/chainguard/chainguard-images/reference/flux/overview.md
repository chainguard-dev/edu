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
|  `latest-dev` | July 18th    | `sha256:5877d62d32090f31123945918f0e7a915e475b8bf19104f7a7735a17e6a18c12` |
|  `latest`     | July 14th    | `sha256:a7cd3a6872dd11489d78b2f188f380788a03190d641ca8cf7e0c5921041e67a4` |
|               | July 12th    | `sha256:62412f69dd8e86389bc13fbe78e715e8ef7cd751ed9745b873443e0c25e0fb79` |
|               | July 8th     | `sha256:cd731887ebca60fa5ff2a0dd4b1d2bb14b9ea1585513c8dd2605a76086fb65b1` |
|               | July 8th     | `sha256:b56dec6807fb26cd009433c0a86022cf30d90253e47c990db4c7b3ecd32d9897` |
|               | July 4th     | `sha256:fd9c25a32ff6d5a752f92172ef45826e7edf6112e8c9746806e5c1190d4d5eae` |
|               | July 4th     | `sha256:d4627a96a1045973f7c455c3be9033f24a6e02e20ef53ed16bed0a61463d5b8d` |
|               | June 26th    | `sha256:e827663f4da12b1645ce553451a2f9fe4b663603c624be6c0db33f8c1cce435e` |



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

