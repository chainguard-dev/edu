---
title: "Image Overview: gitlab-shell"
linktitle: "gitlab-shell"
type: "article"
layout: "single"
description: "Overview: gitlab-shell Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-11-27 16:34:14
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/gitlab-shell/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/gitlab-shell/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/gitlab-shell/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gitlab-shell/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
GitLab is an open source end-to-end software development platform with built-in version control, issue tracking, code review, CI/CD, and more.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/gitlab:latest
```
<!--getting:end-->

<!--body:start-->
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
<!--body:end-->

