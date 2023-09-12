---
title: "Image Overview: coredns"
type: "article"
description: "Overview: coredns Chainguard Image"
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

[cgr.dev/chainguard/coredns](https://github.com/chainguard-images/images/tree/main/images/coredns)

| Tag (s)       | Last Changed   | Digest                                                                    |
|---------------|----------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 11th | `sha256:c9a19a0dfd0bac590b6b893cf80ddb71d91d4f5ef6b3730113ddffed3d59df8f` |
|  `latest`     | September 11th | `sha256:ce0c618332f0c3b2754fcad543a238459d07c2327adcf285d840281a81cfc0ce` |



## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/coredns:latest
```

## Using CoreDNS

The Chainguard CoreDNS image is a drop-in replacement for the upstream image.
See the [upstream documentation](https://coredns.io/) for usage information specific to your environment.

Below is a quickstart example using the upstream helm chart:

```bash
helm repo add coredns https://coredns.github.io/helm
helm install coredns coredns/coredns \
	--set image.repository="cgr.dev/chainguard/coredns" \
	--set image.tag="latest" \
	--set isClusterService=false
```

