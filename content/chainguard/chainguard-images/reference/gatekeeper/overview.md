---
title: "Image Overview: gatekeeper"
type: "article"
description: "Overview: gatekeeper Chainguard Image"
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

[cgr.dev/chainguard/gatekeeper](https://github.com/chainguard-images/images/tree/main/images/gatekeeper)

| Tag (s)       | Last Changed   | Digest                                                                    |
|---------------|----------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 11th | `sha256:7a8904aea2833eb15cb6a774144b3c12a761ee5f38a64611dcd4908956f532e4` |
|  `latest`     | September 11th | `sha256:364caa25c64357b06cf7e8f57d7f54c969319111854d29bed5d4efc977651ddd` |



Minimalist Wolfi-based Gatekeeper which is a policy controller for Kubernetes

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/gatekeeper:latest
```

## Usage

This image should be a drop-in replacement for the upstream `opa/gatekeeper` image.
See the [full documentation](https://open-policy-agent.github.io/gatekeeper/website/) for installation and usage.

See for the [examples](https://open-policy-agent.github.io/gatekeeper/website/docs/examples).

We can use the Chainguard image that we've built for Gatekeeper with the Helm chart of the project using the following commands.

First, you need to install the Helm repository:

```shell
helm repo add gatekeeper https://open-policy-agent.github.io/gatekeeper/charts
```

Once you did this, you can install Gatekeeper to the target cluster:

```shell
   helm install --name-template=gatekeeper \
		--namespace gatekeeper-system \
		--create-namespace \
	    --set image.repository="cgr.dev/chainguard/gatekeeper" \
	    --set image.release="latest" \
        gatekeeper/gatekeeper
```

