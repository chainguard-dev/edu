---
title: "Image Overview: grafana"
linktitle: "grafana"
type: "article"
layout: "single"
description: "Overview: grafana Chainguard Image"
date: 2023-12-15 00:37:05
lastmod: 2023-12-15 00:37:05
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/grafana/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/grafana/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/grafana/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/grafana/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
A minimal wolfi-based image for grafana, which is an open-source monitoring and observability application
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/grafana:latest
```
<!--getting:end-->

<!--body:start-->
## Upstream documentation
For more information on grafana, refer to the [grafana documentation](https://grafana.com/docs/).
Additionally the grafana GitHub reposiory can be [found here](https://github.com/grafana/grafana).

## Helm
grafana can be deployed using the following helm chart:
- [https://artifacthub.io/packages/helm/grafana/grafana](https://artifacthub.io/packages/helm/grafana/grafana)

Follow the instructions in the link above to deploy grafana using helm. Note you
will need to override the default image and tag used, replacing with the
chainguard image, example:

```bash
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

helm install grafana https://grafana.github.io/helm-charts \
  --set image.repository=cgr.dev/chainguard/grafana \
  --set image.tag=latest
```

Refer to the [helm chart documentation](https://artifacthub.io/packages/helm/grafana/grafana)
for full instructions on how to use the helm chart.

## Docker
grafana can be launched using docker. Refer to the
[grafana docker image documentation](https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker)
for full instructions.

Example:

```bash
docker run --name=local-grafana -p 3000:3000 cgr.dev/chainguard/grafana:latest
```

The grafana Web UI would be accessible via:
- [http://localhost:3000](http://localhost:3000)
<!--body:end-->

