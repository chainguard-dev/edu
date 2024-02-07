---
title: "Image Overview: spark-operator"
linktitle: "spark-operator"
type: "article"
layout: "single"
description: "Overview: spark-operator Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-02-07 00:17:48
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
A minimal, Wolfi-based image for Spark Operator. Facilitates the deployment and management of Apache Spark applications in Kubernetes environments.
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

> Spark Operator expects to be deployed in a Kubernetes cluster, where an
> instance of Apache Spark is running, on which it will schedule jobs.


Installation using helm chart, replacing with the Chainguard image:

Below is an example of how to install the spark operator using helm, with the
chainguard image:

```bash
helm repo add spark-operator https://googlecloudplatform.github.io/spark-on-k8s-operator

helm install spark-operator spark-operator/spark-operator \
  --namespace spark \
  --create-namespace \
  --set image.repository=cgr.dev/chainguard/spark-operator \
  --set image.tag=latest
```

For more detail, please refer to the [Spark Operator installation documentation](https://github.com/GoogleCloudPlatform/spark-on-k8s-operator?tab=readme-ov-file#installation).
<!--body:end-->

