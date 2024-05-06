---
title: "Image Overview: superset"
linktitle: "superset"
type: "article"
layout: "single"
description: "Overview: superset Chainguard Image"
date: 2024-05-06 00:43:57
lastmod: 2024-05-06 00:43:57
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/superset/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/superset/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/superset/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/superset/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
A minimal, [wolfi](https://github.com/wolfi-dev)-based image for Apache Superset. [Apache Superset](https://github.com/apache/superset/tree/master)is a Data Visualization and Data Exploration Platform
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/superset:latest
```


<!--body:start-->
## Deploying Apache Superset with Helm

Deploying Apache Superset with Chainguard's images is straightforward using the official Superset Helm chart.

First, add the Superset Helm repository:

```bash
helm repo add superset https://apache.github.io/superset

# Deploy Superset using:

helm install superset superset/superset \
  --set extraSecretEnv.SUPERSET_SECRET_KEY="$(openssl rand -base64 42)" \
  --set image.repository=cgr.dev/chainguard/superset \
  --set image.tag=latest
```

You can also customize your Helm deployment by editing the values.yaml after fetching the chart:

helm fetch superset/superset --untar
Then edit values.yaml to use Chainguard's images/tags:

```
image:
  repository: cgr.dev/chainguard/apache-superset
  tag: latest
```
Deploy your customized Helm chart:

```
helm install superset .
```

For detailed instructions on deploying Apache Superset via Helm, consult the official Apache Superset Helm chart documentation.


## Usage
With Apache Superset running, access the web interface by navigating to http://localhost:8088. Login with the default credentials or the ones you have configured.

You can now manage databases, create visualizations, and configure your dashboards.

<!--body:end-->

