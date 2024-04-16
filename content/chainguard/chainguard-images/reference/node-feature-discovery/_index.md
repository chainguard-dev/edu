---
title: "Image Overview: node-feature-discovery"
linktitle: "node-feature-discovery"
type: "article"
layout: "single"
description: "Overview: node-feature-discovery Chainguard Image"
date: 2024-04-16 00:44:43
lastmod: 2024-04-16 00:44:43
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/node-feature-discovery/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/node-feature-discovery/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/node-feature-discovery/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/node-feature-discovery/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
A minimal wolfi-based image for node-feature-discovery, Node feature discovery for Kubernetes
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/node-feature-discovery:latest
```


<!--body:start-->
## Upstream documentation
For more information on node-feature-discovery, refer to the [node-feature-discovery documentation](https://kubernetes-sigs.github.io/node-feature-discovery/stable/get-started/index.html).
Additionally the node-feature-discovery GitHub reposiory can be [found here](https://github.com/kubernetes-sigs/node-feature-discovery).

## Helm
Node-feature-discovery can be deployed using the following helm chart:
- [https://artifacthub.io/packages/helm/node-feature-discovery/node-feature-discovery](https://artifacthub.io/packages/helm/node-feature-discovery/node-feature-discovery)

Follow the instructions in the link above to deploy node-feature-discovery using helm. Note you
will need to override the default image and tag used, replacing with the
chainguard image, example:

```bash
helm repo add node-feature-discovery https://kubernetes-sigs.github.io/node-feature-discovery/charts
helm repo update

export NFD_NS=node-feature-discovery
helm install nfd/node-feature-discovery --namespace $NFD_NS --create-namespace --generate-name \
  --set image.repository=cgr.dev/chainguard/node-feature-discovery \
  --set image.tag=latest
```

Refer to the [helm chart documentation](https://artifacthub.io/packages/helm/node-feature-discovery/node-feature-discovery)
for full instructions on how to use the helm chart.

<!--body:end-->

