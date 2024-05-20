---
title: "Image Overview: rabbitmq-default-user-credential-updater"
linktitle: "rabbitmq-default-user-credential-updater"
type: "article"
layout: "single"
description: "Overview: rabbitmq-default-user-credential-updater Chainguard Image"
date: 2024-05-20 00:48:18
lastmod: 2024-05-20 00:48:18
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/rabbitmq-default-user-credential-updater/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/rabbitmq-default-user-credential-updater/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/rabbitmq-default-user-credential-updater/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/rabbitmq-default-user-credential-updater/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image with [default-user-credential-updater](https://github.com/rabbitmq/default-user-credential-updater)
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/rabbitmq-default-user-credential-updater:latest
```


<!--body:start-->
## Usage

This image is a drop-in replacement for the upstream image.
For example, you can run it using the upstream RabbitMQ Cluster Operator deployment by
defining the `DEFAULT_USER_UPDATER_IMAGE` environment variable:

```shell
cat <<EOF > kustomization.yaml
resources:
- https://github.com/rabbitmq/cluster-operator/releases/latest/download/cluster-operator.yml
patches:
- patch: |-
    - op: add
      path: "/spec/template/spec/containers/0/env/-"
      value: 
        name: DEFAULT_USER_UPDATER_IMAGE
        value: cgr.dev/chainguard/rabbitmq-default-user-credential-updater:latest
  target:
    kind: Deployment
    namespace: rabbitmq-system
    name: rabbitmq-cluster-operator
EOF

kustomize build . | kubectl apply -f -
```
<!--body:end-->

