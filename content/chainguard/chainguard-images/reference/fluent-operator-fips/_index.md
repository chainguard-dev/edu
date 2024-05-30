---
title: "Image Overview: fluent-operator-fips"
linktitle: "fluent-operator-fips"
type: "article"
layout: "single"
description: "Overview: fluent-operator-fips Chainguard Image"
date: 2024-05-30 00:47:59
lastmod: 2024-05-30 00:47:59
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/fluent-operator-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/fluent-operator-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/fluent-operator-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/fluent-operator-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Operator for Fluent Bit and Fluentd - previously known as FluentBit Operator
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/fluent-operator-fips:latest
```


<!--body:start-->
The Fluent Operator is designed to deploy FluentBit Fluentd as a DaemonSet and StatefulSet respectively. It supports dynamic reconfiguration via CRDs and can be deployed using YAML or Helm.

To deploy the Chainguard Fluent Operator image, use the following Helm commands:

```
helm repo add fluent https://fluent.github.io/helm-charts
helm install fluent-operator \
    --create-namespace \
    -n fluent fluent/fluent-operator \
    --set operator.container.repository=cgr.dev/chainguard/fluent-operator \
    --set operator.container.tag=latest
```

Once the operator is deployed, follow the [Fluent Operator Walkthrough](https://github.com/kubesphere-sigs/fluent-operator-walkthrough) guides to configure FluentBit or Fluentd appropriately for your Kubernetes cluster.
<!--body:end-->

