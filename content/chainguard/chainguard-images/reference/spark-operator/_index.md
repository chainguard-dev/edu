---
title: "Image Overview: spark-operator"
linktitle: "spark-operator"
type: "article"
layout: "single"
description: "Overview: spark-operator Chainguard Image"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/spark-operator/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/spark-operator/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/spark-operator/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/spark-operator/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based Spark Operator image for managing the lifecycle of Apache Spark applications on Kubernetes.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/spark-operator:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

The easiest way to install the Kubernetes Operator for Apache Spark is to use the Helm chart.

```bash
$ helm repo add spark-operator https://googlecloudplatform.github.io/spark-on-k8s-operator

$ helm install my-release spark-operator/spark-operator --namespace spark-operator --create-namespace --set image.repository=cgr.dev/chainguard/spark-operator --set image.tag=latest
```

For more detail, please refer to the [Spark Operator installation documentation](https://github.com/GoogleCloudPlatform/spark-on-k8s-operator?tab=readme-ov-file#installation).
<!--body:end-->

