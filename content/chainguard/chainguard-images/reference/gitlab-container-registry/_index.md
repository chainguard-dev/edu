---
title: "Image Overview: gitlab-container-registry"
linktitle: "gitlab-container-registry"
type: "article"
layout: "single"
description: "Overview: gitlab-container-registry Chainguard Image"
date: 2024-07-10 00:36:03
lastmod: 2024-07-10 00:36:03
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/gitlab-container-registry/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gitlab-container-registry/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/gitlab-container-registry/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gitlab-container-registry/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
The GitLab Container Registry originated as a fork of the Docker Distribution Registry,now CNCF Distribution, both distributed under Apache License Version 2.0.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/gitlab-container-registry:latest
```


<!--body:start-->
## Usage

Please refer to the following helm chart documentation, for instructions on how to deploy GitLab in Kubernetes: [see here](https://docs.gitlab.com/charts/).

The GitLab helm chart, is composed of multiple [sub-charts](https://docs.gitlab.com/charts/charts/gitlab/index.html), one of which deploys the GitLab registry component.

Below is an example of how to deploy the helm chart, using the Chainguard image for GitLab registry.
Note, it is not intended to be a replacement for the [official documentation](https://docs.gitlab.com/charts):

```bash
helm repo add gitlab https://charts.gitlab.io/
helm repo update
helm upgrade --install gitlab gitlab/gitlab \
  --timeout 600s \
  --set registry.enabled=true \
  --set registry.image.repository=cgr.dev/chainguard-private/gitlab-container-registry \
  --set registry.image.tag=latest \
```

Also you can find the installation parameters related to the registrt sub-chart, [here](https://docs.gitlab.com/charts/charts/registry/#installation-parameters).
<!--body:end-->

