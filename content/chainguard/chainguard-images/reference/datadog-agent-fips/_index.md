---
title: "Image Overview: datadog-agent-fips"
linktitle: "datadog-agent-fips"
type: "article"
layout: "single"
description: "Overview: datadog-agent-fips Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/datadog-agent-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/datadog-agent-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/datadog-agent-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/datadog-agent-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based Datadog Agent to collect events and metrics from hosts and send them to Datadog.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/datadog-agent-fips:latest
```


<!--body:start-->
## Usage

The Datadog Agent collects events and metrics from hosts and sends them to Datadog.

### Prerequisites

    * Create a Datadog account.
    * Have your Datadog API key on hand.

The DataDog Agent getting started guide is here: [docs.datadoghq.com/getting_started/agent/](https://docs.datadoghq.com/getting_started/agent/)

### Example Usage

```bash
docker run \
 --name dd-agent \
 -e DD_API_KEY=<xxxxxxxxxxxxxxxxxxx> \
 -e DD_SITE="datadoghq.com" \
 -e DD_APM_ENABLED=true \
 -e DD_APM_NON_LOCAL_TRAFFIC=true \
 -v /var/run/docker.sock:/var/run/docker.sock:ro \
 -v /proc/:/host/proc/:ro \
 -v /sys/fs/cgroup/:/host/sys/fs/cgroup:ro \
 -v /var/lib/docker/containers:/var/lib/docker/containers:ro \
 cgr.dev/chainguard/datadog-agent:latest
```

For more detail, please refer to the [DataDog Agent documentation](https://github.com/DataDog/datadog-agent).
<!--body:end-->

