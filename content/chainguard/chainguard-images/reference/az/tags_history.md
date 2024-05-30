---
title: "az Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the az Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-30 00:47:59
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/az/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/az/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/az/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/az/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 27th     | `sha256:7784de8327481379ed1cbfca60dbe79d16836e61774f0e806fdfd9be105c8f41` |
|  `latest-dev` | May 23rd     | `sha256:424b984e8f14a122877b9ef750a6e02f1f874779405be05a1a2cb87dda66b3b4` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2-dev` `2.61-dev` `2.61.0-dev` `latest-dev` | May 29th     | `sha256:0c00b02bdf2d19f3078ce7a53f66c3936baf99a6315e81ab36a5e5f5eaa86d30` |
|  `latest` `2` `2.61` `2.61.0`                 | May 29th     | `sha256:b012edd4fbead49918a98959b209219657a00762b092cd8a491d3696c7a5a9ed` |
|  `2.60.0-dev` `2.60-dev`                      | May 19th     | `sha256:ebf4af5e8c9618e08a9d8d17cfcc446250833fd4b0fb8593179302879a9fd2b9` |
|  `2.60.0` `2.60`                              | May 17th     | `sha256:15ef99e92cea2e3acfa4c18d8cfea77d74684109d3c2a41ef1899924a800ff2a` |

