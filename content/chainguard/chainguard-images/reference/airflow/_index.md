---
title: "Image Overview: airflow"
linktitle: "airflow"
type: "article"
layout: "single"
description: "Overview: airflow Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/airflow/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/airflow/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/airflow/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/airflow/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
A minimal, [wolfi](https://github.com/wolfi-dev)-based image for Apache Airflow.[Apache Airflow](https://github.com/apache/airflow) is a platform to programmatically author, schedule, and monitor workflows.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/airflow:latest
```


<!--body:start-->
## Deploying Apache Airflow with Helm

Deploying Apache Airflow with Chainguard's images is straightforward using the official Airflow Helm chart.

First, add the Airflow Helm repository:

```bash
helm repo add airflow-stable https://airflow-helm.github.io/charts
```
Deploy Airflow using:

```bash
helm install airflow airflow-stable/airflow \
  --set airflow.image.repository=cgr.dev/chainguard/airflow \
  --set airflow.image.tag=latest
```

You can also customize your Helm deployment by editing the values.yaml after fetching the chart:

```helm fetch airflow-stable/airflow --untar```

Then edit values.yaml to use Chainguard's images/tags:

```bash 
image:
  repository: cgr.dev/chainguard/airflow
  tag: latest
```

Deploy your customized Helm chart:

```bash
helm install airflow .
```
For detailed instructions on deploying Apache Airflow via Helm, consult the official Apache Airflow Helm chart documentation.

Usage
With Apache Airflow running, access the web interface by navigating to http://localhost:8080. Login with the default credentials or the ones you have configured.

You can now manage workflows, create DAGs, and monitor your tasks.

<!--body:end-->

