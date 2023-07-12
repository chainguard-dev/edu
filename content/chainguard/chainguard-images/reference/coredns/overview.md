---
title: "Image Overview: Coredns"
type: "article"
description: "Overview: Coredns Chainguard Image"
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

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest`     | 20 hours ago | `sha256:8646ba2a16b25c7230ce446d12d4aa730c868d46c8c83e56db0fb13b2c92103c` |
| `latest-dev` | 20 hours ago | `sha256:cc17a6a80ebd8189dea121f32c8d2ca6da3667177fb29a4425bca629490bb622` |



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
