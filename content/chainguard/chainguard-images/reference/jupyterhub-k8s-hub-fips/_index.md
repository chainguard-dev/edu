---
title: "Image Overview: jupyterhub-k8s-hub-fips"
linktitle: "jupyterhub-k8s-hub-fips"
type: "article"
layout: "single"
description: "Overview: jupyterhub-k8s-hub-fips Chainguard Image"
date: 2024-02-29 16:25:55
lastmod: 2024-02-29 16:25:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/jupyterhub-k8s-hub-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jupyterhub-k8s-hub-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/jupyterhub-k8s-hub-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jupyterhub-k8s-hub-fips/provenance_info/" >}}
{{</ tabs >}}

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/jupyterhub-k8s-hub-fips:latest
```

## Usage

The image is not intended to be used directly. It requires some configuration files to be mounted into the container. See the [JupyterHub documentation](https://z2jh.jupyter.org/en/stable/jupyterhub/installation.html) for more information.

Since the image is non-root, we are using `1000` as the UID and GID for the user. This user has
write access to `/usr/local/etc/jupyterhub`.

You can run the image using the Helm Chart with:

```shell
helm repo add jupyterhub https://hub.jupyter.org/helm-chart/
helm repo update
helm upgrade --install jupyterhub jupyterhub/jupyterhub \
  --set hub.image.name=cgr.dev/chainguard-private/jupyterhub-k8s-hub-fips \
  --set hub.image.tag=$VERSION \
  --set hub.config.JupyterHub.db_url=/usr/local/etc/jupyterhub/jupyterhub.sqlite
```

