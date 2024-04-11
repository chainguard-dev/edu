---
title: "Image Overview: newrelic-nri-statsd"
linktitle: "newrelic-nri-statsd"
type: "article"
layout: "single"
description: "Overview: newrelic-nri-statsd Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/newrelic-nri-statsd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/newrelic-nri-statsd/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/newrelic-nri-statsd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/newrelic-nri-statsd/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
The StatsD integration lets you easily get StatsD data into New Relic
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/newrelic-nri-statsd:latest
```


<!--body:start-->

## Usage

To run the container, you can use the following command:

```bash
docker run \
  -d --restart unless-stopped \
  --name newrelic-statsd \
  -h $(hostname) \
  -e NR_ACCOUNT_ID=YOUR_ACCOUNT_ID \
  -e NR_API_KEY=NEW_RELIC_LICENSE_KEY \
  -p 8125:8125/udp \
  cgr.dev/chainguard/newrelic-nri-statsd:latest
```

Here is the link to get more detail about it, [official documentation](https://docs.newrelic.com/docs/more-integrations/open-source-telemetry-integrations/statsd/statsd-monitoring-integration/).


<!--body:end-->

