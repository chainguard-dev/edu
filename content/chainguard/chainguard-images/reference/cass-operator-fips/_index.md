---
title: "Image Overview: cass-operator-fips"
linktitle: "cass-operator-fips"
type: "article"
layout: "single"
description: "Overview: cass-operator-fips Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/cass-operator-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cass-operator-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/cass-operator-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cass-operator-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[cass-operator](https://github.com/k8ssandra/cass-operator), is a Kubernetes operator for managing Apache Cassandra. It automates tasks like deployment, scaling, and configuration management, facilitating the integration of Cassandra clusters with Kubernetes environments.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/cass-operator-fips:latest
```


<!--body:start-->

## Usage
cass-operator is a Kubernetes operator, which can be deployed using helm. Refer to the [upstream repositories documentation](https://github.com/k8ssandra/cass-operator) for how to get started with cass-operator.

To use our minimal, wolfi-based image with this Helm chart you'll need to override the image used by the official helm chart and specify the chainguard image as per below example:

```shell
helm repo add k8ssandra https://helm.k8ssandra.io/stable
helm repo update

helm install cass-operator k8ssandra/cass-operator -n cass-operator
helm upgrade cass-operator \
    -n cass-operator \
    --set image.repository=cgr.dev/chainguard/cass-operator \
    --set image.tag=latest
    --wait \
    k8ssandra/cass-operator
}
```

As per [project documentation](https://github.com/k8ssandra/cass-operator/blob/master/README.md#installing-the-operator-with-helm), by default, the Helm installation requires cert-manager to be present in the Kubernetes installation. If you do not have cert-manager installed, follow the steps at (https://cert-manager.io/docs/installation/helm/)[cert-manager's] documentation.
<!--body:end-->

