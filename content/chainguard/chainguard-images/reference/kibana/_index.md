---
title: "Image Overview: kibana"
linktitle: "kibana"
type: "article"
layout: "single"
description: "Overview: kibana Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/kibana/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kibana/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kibana/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kibana/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Your window into the Elastic Stack.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/kibana:latest
```


<!--compatibility:start-->
## Compatibility Notes

Note that Kibana only supports running the same major version as its backend Elasticsearch container, so be sure to run 8.x Kibana with an 8.x version of Elasticsearch. See the [Kibana Guide](https://www.elastic.co/guide/en/kibana/master/setup.html#elasticsearch-version) for more details.
<!--compatibility:end-->

<!--body:start-->
For details on how to run Kibana, refer to the Elastic documentation on [Installing Kibana with Docker](https://www.elastic.co/guide/en/kibana/master/docker.html).
<!--body:end-->

