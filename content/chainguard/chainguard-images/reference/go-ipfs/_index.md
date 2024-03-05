---
title: "Image Overview: go-ipfs"
linktitle: "go-ipfs"
type: "article"
layout: "single"
description: "Overview: go-ipfs Chainguard Image"
date: 2024-03-05 17:06:05
lastmod: 2024-03-05 17:06:05
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu: 
  docs: 
    parent: "images-reference"
weight: 500
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/go-ipfs/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/go-ipfs/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/go-ipfs/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/go-ipfs/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based image for `go-ipfs`.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/go-ipfs:latest
```
<!--getting:end-->

<!--body:start-->

kubo (also referred to a go-ipfs) is a widely used implementation of the [The InterPlanetary File System (IPFS)](https://docs.ipfs.io/) protocol. \

This kubo image has the following features:
* An IPFS daemon server
* An HTTP RPC API for controlling the node
* An HTTP Gateway for serving content to HTTP browsers

## Usage

To start using IPFS, you must first initialize IPFS's config files on your system using the `ipfs init` command.
See `ipfs init --help` for information on the optional arguments it takes. After initialization is complete, you can use `ipfs mount`, `ipfs add` and any of the other built in commands.

The following set of commands demonstrate how to initialize and run the `ipfs` image.

First, create a volume for the IPFS files and set the owner to `nonroot`:
```bash
docker run \
    --rm -t \
    -v ipfs-data:/home/nonroot/.ipfs \
    cgr.dev/chainguard/bash \
    'chown nonroot:nonroot /home/nonroot/.ipfs'
```

Next run `ipfs init` with the volume:

```bash
docker run --rm -t -v ipfs-data:/home/nonroot/.ipfs cgr.dev/chainguard/go-ipfs:latest init
```

Finally, run an IPFS container with the volume mounted:

```bash
docker run \
    -v ipfs-data:/home/nonroot/.ipfs \
    -d --rm \
    -p "5001:5001" \
    --name "ipfs" \
    cgr.dev/chainguard/go-ipfs:latest daemon --migrate=true
```


```bash
docker run cgr.dev/chainguard/go-ipfs:latest help
```

For more information, refer to the ipfs documentation:
- [Ipfs GitHub](https://github.com/ipfs/kubo)
<!--body:end-->

