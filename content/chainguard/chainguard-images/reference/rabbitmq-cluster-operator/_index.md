---
title: "Image Overview: rabbitmq-cluster-operator"
linktitle: "rabbitmq-cluster-operator"
type: "article"
layout: "single"
description: "Overview: rabbitmq-cluster-operator Chainguard Image"
date: 2022-11-01T11:07:52+02:00
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/rabbitmq-cluster-operator/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/rabbitmq-cluster-operator/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/rabbitmq-cluster-operator/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/rabbitmq-cluster-operator/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
RabbitMQ Cluster Kubernetes Operator
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/rabbitmq-cluster-operator:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

This image is a drop-in replacement for the upstream image.
You can run it using kustomize with:

```shell
LATEST=$(curl -s "https://api.github.com/repos/rabbitmq/cluster-operator/releases/latest" | jq -r '.tag_name')

cat <<EOF > kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - "https://github.com/rabbitmq/cluster-operator/releases/download/${LATEST}/cluster-operator.yml"
patches:
  - patch: |
      - op: replace
        path: /spec/template/spec/containers/0/image
        value: cgr.dev/chainguard/rabbitmq-cluster-operator:latest
    target:
      version: v1
      kind: Deployment
      name: rabbitmq-cluster-operator
      namespace: rabbitmq-system
EOF

kubectl apply -f .
```
<!--body:end-->

