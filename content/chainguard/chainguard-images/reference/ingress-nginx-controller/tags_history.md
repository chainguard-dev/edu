---
title: "ingress-nginx-controller Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the ingress-nginx-controller Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-20 00:48:18
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/ingress-nginx-controller/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 17th     | `sha256:589c95e675d5c6d8888b264efbb9d8d29f1d4ff34df2b9cd4f19a28e34490645` |
|  `latest`     | May 17th     | `sha256:332907bd7380f3d47a0cdc88ed30b6ad110040079d12100bf1a0ecc433d1e2c0` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `1-dev` `1.10-dev` `1.10.1-dev` | May 19th     | `sha256:bc5acc0144d9d721227ad11601accdda0f4667be8f0f46a6e13be65fe31ad26d` |
|  `1.10` `1` `1.10.1` `latest`                 | May 19th     | `sha256:145aeaf0bd12b41ee519aec1d70a815f10c891b1314077aa8bb323352845a51d` |
|  `1.9-dev` `1.9.6-dev`                        | May 19th     | `sha256:bb643e29a5b9c7ffe3d26a782e7cd3b4f648b555cf86a0c67dcbeea5cd91b1c4` |
|  `1.9` `1.9.6`                                | May 19th     | `sha256:fac4c928f637740a6f3e59ef65076d78220d2de8582951a4fa53c3c32f2a02fd` |
|  `1.10.0-dev`                                 | April 20th   | `sha256:27f7a69e168ba4b48506041601641dafb87118758ef4b408eb01c0e6867d5553` |
|  `1.10.0`                                     | April 20th   | `sha256:2a323e07711fb6b5f9f201d89610035cebaf5be7ef2466d92efc8a8031dcfb71` |

