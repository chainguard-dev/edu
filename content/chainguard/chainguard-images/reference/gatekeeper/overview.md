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

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest-dev` | July 12th    | `sha256:6245437b1cac331174ff0293850739e12ff5e7697e1f5845bcc08a2ddde389fe` |
| `latest`     | July 11th    | `sha256:02e519e4c71ae9b7fe064e2768a1f5d421fd7d8f443a1e1c52648979db899112` |



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
