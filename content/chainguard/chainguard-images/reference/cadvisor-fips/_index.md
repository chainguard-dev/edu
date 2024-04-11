---
title: "Image Overview: cadvisor-fips"
linktitle: "cadvisor-fips"
type: "article"
layout: "single"
description: "Overview: cadvisor-fips Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/cadvisor-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cadvisor-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/cadvisor-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cadvisor-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[cAdvisor (Container Advisor)](https://github.com/google/cadvisor) provides container users an understanding of the resource usage and performance characteristics of their running containers.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/cadvisor-fips:latest
```


<!--body:start-->
## Usage

See the [RUNNING.md](https://github.com/google/cadvisor/blob/master/docs/running.md) for the instructions. For the [Kubernetes deployment](https://github.com/google/cadvisor/tree/master/deploy/kubernetes), you can use the Kustomize:

```bash
cat <<EOF >> kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - https://github.com/google/cadvisor/deploy/kubernetes/base?ref=master
images:
  - name: gcr.io/cadvisor/cadvisor
    newName: cgr.dev/chainguard/cadvisor
    newTag: latest
namespace: cadvisor
EOF
kubectl apply -k .
```
<!--body:end-->

