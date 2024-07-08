---
title: "Image Overview: jitsucom-ingest"
linktitle: "jitsucom-ingest"
type: "article"
layout: "single"
description: "Overview: jitsucom-ingest Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-07-08 00:34:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/jitsucom-ingest/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jitsucom-ingest/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/jitsucom-ingest/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jitsucom-ingest/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Service for bulk-loading data to databases with automatic schema management (Redshift, Snowflake, BigQuery, ClickHouse, Postgres, MySQL)
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/jitsucom-ingest:latest
```


<!--body:start-->
## Usage

```sh
helm upgrade --install jitsucom-bulker oci://registry-1.docker.io/stafftasticcharts/jitsu \
    -n jitsucom-bulker \
    --create-namespace \
    --set bulker.image.repository=cgr.dev/chainguard/jitsucom-bulker \
    --set bulker.image.tag=latest \
    --set ingest.image.repository=cgr.dev/chainguard/jitsucom-ingest \
    --set ingest.image.tag=latest \
    --set syncctl.image.repository=cgr.dev/chainguard/jitsucom-syncctl \
    --set syncctl.image.tag=latest \
    --set tokenGenerator.image.tag=1.30.0 # `:latest` tag doesn't not exist, so set to _latest_ version
```

* Refer to [values.yaml](https://github.com/stafftastic/jitsu-chart/blob/main/values.yaml) file for more configuration options.

> [!WARNING]
> The Helm Chart we used in the tests is the official, stable and is used to run Jitsu in production, according to maintainer's [comment](https://github.com/jitsucom/jitsu/issues/880#issuecomment-1987928495).
<!--body:end-->

