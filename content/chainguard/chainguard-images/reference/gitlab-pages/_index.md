---
title: "Image Overview: gitlab-pages"
linktitle: "gitlab-pages"
type: "article"
layout: "single"
description: "Overview: gitlab-pages Chainguard Image"
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

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/gitlab-pages/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/gitlab-pages/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/gitlab-pages/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gitlab-pages/provenance_info/" >}}
{{</ tabs >}}



# GitLab Images

## Get It!

The images are available on `cgr.dev`, e.g. `gitlab-kas`:

```
docker pull cgr.dev/chainguard/gitlab-kas:latest
```

## Usage

This replaces the GitLab images used in the deployment by our Chainguard images for GitLab.
See the [full documentation](https://docs.gitlab.com/charts/) for installation and usage.

We can use the different GitLab Chainguard images that we've built for GitLab with the Helm chart of the project using the following commands.

First, you need to install the Helm repository:

```shell
helm repo add gitlab https://charts.gitlab.io/
helm repo update
```

Once you did this, you can install Gitlab Kas to the target cluster:

```shell
    helm upgrade --install gitlab gitlab/gitlab \
        --timeout 600s \
        --set global.hosts.domain=example.com \
        --set gitlab.kas.image.repository="cgr.dev/chainguard/gitlab-kas" \
        --set gitlab.kas.image.tag="latest" \
        --set global.hosts.externalIP=10.10.10.10 \
        --set certmanager-issuer.email=me@example.com \
        --set postgresql.image.tag=13.6.0
```

