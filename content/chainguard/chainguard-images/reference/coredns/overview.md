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

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 27th    | `sha256:cd29f956e9463972091c03cdee5eb7b3c46a81a744ffcd6d5b18a13209b17e9f` |
|  `latest`     | July 27th    | `sha256:c1dd992085e0e46331190bda7cdf04077fa425ca4ad2e74718bf477794410a8a` |



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

