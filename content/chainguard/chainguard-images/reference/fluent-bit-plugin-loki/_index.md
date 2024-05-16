---
title: "Image Overview: fluent-bit-plugin-loki"
linktitle: "fluent-bit-plugin-loki"
type: "article"
layout: "single"
description: "Overview: fluent-bit-plugin-loki Chainguard Image"
date: 2024-05-16 00:37:58
lastmod: 2024-05-16 00:37:58
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/fluent-bit-plugin-loki/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/fluent-bit-plugin-loki/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/fluent-bit-plugin-loki/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/fluent-bit-plugin-loki/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
The Fluent Bit Loki plugin allows you to send your log or events to a Loki service.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/fluent-bit-plugin-loki:latest
```


<!--body:start-->
## Usage

### Docker

You can run a Fluent Bit container with the Loki output plugin pre-installed using the following command:

```bash
docker run -v /var/log:/var/log \
    -e LOG_PATH="/var/log/*.log" -e LOKI_URL="http://localhost:3100/loki/api/v1/push" \
    cgr.dev/chainguard/fluent-bit-plugin-loki:latest
```
The [GitHub repository](https://github.com/grafana/loki/tree/main/clients/cmd/fluent-bit) has more details on running the fluent-bit plugin.  
**Note:** The default loki plugin config can be found at `/fluent-bit/etc/fluent-bit-loki.conf`.

### Helm
The plugin can also be installed using the fluent-bit helm chart by configuring the image values:

```yaml
image:
  repository: cgr.dev/chainguard/fluent-bit-plugin-loki
  tag: latest
```
For detailed instructions on setting up the Fluent Bit Loki plugin, refer to the [Loki documentation](https://grafana.com/docs/loki/latest/send-data/fluentbit/).

<!--body:end-->

