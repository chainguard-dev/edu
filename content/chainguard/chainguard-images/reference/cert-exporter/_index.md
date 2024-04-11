---
title: "Image Overview: cert-exporter"
linktitle: "cert-exporter"
type: "article"
layout: "single"
description: "Overview: cert-exporter Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/cert-exporter/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cert-exporter/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/cert-exporter/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cert-exporter/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
A minimal, wolfi-based image for cert-exporter: an application that exports certificate expiration metrics from disk, Kubernetes, and AWS Secrets Manager to Prometheus.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/cert-exporter:latest
```


<!--body:start-->
## Usage
For full instructions on how to run cert-exporter, please refer to the upstream
GitHub repositories [documentation](https://github.com/joe-elliott/cert-exporter).

> **NOTE:** cert-exporter is intended to run inside a Kubernetes cluster. If you
> attempt to run locally, it'll hang and doesn't print anything to the logs.

### Helm
To deploy via helm, please refer to the upstream
[helm charts documentation](https://github.com/joe-elliott/cert-exporter/tree/master/helm/cert-exporter)
for comprehensive instructions, which includes
[supported parameters](https://github.com/joe-elliott/cert-exporter/blob/master/helm/cert-exporter/values.yaml).

Below is an example of how to use the helm chart, overriding the image with the
chainguard image:

```bash
helm repo add cert-exporter https://joe-elliott.github.io/cert-exporter/

# The chart will error if this doesn't already exist, however it does not use this ns directly.
kubectl create namespace monitoring

helm install cert-exporter cert-exporter/cert-exporter  \
 --set image.repository=cgr.dev/chainguard/cert-exporter \
 --set image.tag=latest
```
<!--body:end-->

