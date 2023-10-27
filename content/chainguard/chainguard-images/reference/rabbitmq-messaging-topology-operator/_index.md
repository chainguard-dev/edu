---
title: "Image Overview: rabbitmq-messaging-topology-operator"
linktitle: "rabbitmq-messaging-topology-operator"
type: "article"
layout: "single"
description: "Overview: rabbitmq-messaging-topology-operator Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/rabbitmq-messaging-topology-operator/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/rabbitmq-messaging-topology-operator/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/rabbitmq-messaging-topology-operator/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/rabbitmq-messaging-topology-operator/provenance_info/" >}}
{{</ tabs >}}



Minimal Project RabbitMQ Messaging Topology Kubernetes Operator

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/rabbitmq-messaging-topology-operator:latest
```

## Usage

This image is a drop-in replacement for the upstream image.
You can run it using kustomize with:

```shell
LATEST=$(curl -s "https://api.github.com/repos/rabbitmq/messaging-topology-operator/releases/latest" | jq -r '.tag_name')

cat <<EOF > kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - "https://github.com/rabbitmq/messaging-topology-operator/releases/download/${LATEST}/messaging-topology-operator.yaml"
patches:
  - patch: |
      - op: replace
        path: /spec/template/spec/containers/0/image
        value: cgr.dev/chainguard/rabbitmq-messaging-topology-operator:latest
    target:
      version: v1
      kind: Deployment
      name:  messaging-topology-operator
      namespace: rabbitmq-system
EOF

kubectl apply -f .
```

