---
title: "Image Overview: meilisearch"
linktitle: "meilisearch"
type: "article"
layout: "single"
description: "Overview: meilisearch Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-07-03 00:33:11
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/meilisearch/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/meilisearch/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/meilisearch/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/meilisearch/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal meilisearch image.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/meilisearch:latest
```


<!--compatibility:start-->
## Compatibility Notes

The image specifies a default non-root `meilisearch` user (UID 999), and a data and dump directory at `/var/data.ms`, owned by that `meilisearch` user, accessible to all users.
<!--compatibility:end-->

<!--body:start-->
## Usage Example

Run a meilisearch container with the following command:

```
docker run \
  --rm \
  -d \
  -p 7700:7700 \
  cgr.dev/chainguard/meilisearch:latest \
  --db-path /var/data.ms
  --dump-dir /var/data.ms/dumps \
  --http-addr 0.0.0.0:7700
```

Then you can follow the [meilisearch quick start guide](https://www.meilisearch.com/docs/learn/getting_started/quick_start#add-documents) and start adding documents.
<!--body:end-->

