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
|  `latest`     | August 31st  | `sha256:fa314c749bb0182c6887341ad30685a485df6b8296dfe2b84be23238668ed213` |
|  `latest-dev` | August 31st  | `sha256:b53f474abbb21e4bfe95d92d2827686c7d085f1db544ef09ca6b1cd7ce6b3f4c` |



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

