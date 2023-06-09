---
title: "Image Overview: coredns"
type: "article"
description: "Overview: coredns Chainguard Images"
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

`stable` [cgr.dev/chainguard/coredns](https://github.com/chainguard-images/images/tree/main/images/coredns)
| Tags         | Aliases                                            |
|--------------|----------------------------------------------------|
| `latest`     | `1`, `1.10`, `1.10.1`, `1.10.1-r1`                 |
| `latest-dev` | `1-dev`, `1.10-dev`, `1.10.1-dev`, `1.10.1-r1-dev` |



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

