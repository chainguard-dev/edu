---
title: "Image Overview: kor"
linktitle: "kor"
type: "article"
layout: "single"
description: "Overview: kor Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-03-01 12:14:22
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/kor/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kor/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kor/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kor/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
A Golang Tool to discover unused Kubernetes Resources
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kor:latest
```
<!--getting:end-->

<!--body:start-->
# Kor - Kubernetes Orphaned Resources Finder

Kor is a tool to discover unused Kubernetes resources. Currently, Kor can identify and list unused:
- ConfigMaps  
- Secrets
- Services
- ServiceAccounts
- Deployments
- StatefulSets
- Roles
- HPAs
- PVCs
- Ingresses
- PDBs
- CRDs

![Kor Screenshot](/images/screenshot.png)

for more information refer [kor](https://github.com/yonahd/kor)

## Installation

### Docker
Run a container with your kubeconfig mounted:
```sh
docker run --rm -i cgr.dev/chainguard/kor:latest

docker run --rm -i -v "/path/to/.kube/config:/root/.kube/config" cgr.dev/chainguard/kor:latest all
```

### Helm
Run as a cronjob in your Cluster (with an option for sending slack updates)

```sh
git clone https://github.com/yonahd/kor.git
```

```sh
helm upgrade --install kor \
    --namespace kor \
    --create-namespace \
    --set cronJob.enabled=true \
    --set cronJob.image.repository=cgr.dev/chainguard/kor \
    --set cronJob.image.tag=latest \
    --set prometheusExporter.enabled=true \
    --set prometheusExporter.deployment.image.repository=cgr.dev/chainguard/kor \
    --set prometheusExporter.deployment.image.tag=latest \
    --wait \
    --timeout=300s \
    ./kor/charts/kor
```
<!--body:end-->

