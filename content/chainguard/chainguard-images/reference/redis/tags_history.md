---
title: "redis Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the redis Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-13 00:52:18
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/redis/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/redis/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/redis/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/redis/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 12th   | `sha256:ef0cb67f706f78ad8fa48fbc2655b9b41861db8efe20aae5a6c7b4dbf6803896` |
|  `latest`     | March 8th    | `sha256:5a351b571f86b7ee69aa1cb7a4f6761aaa19ed3728e6b72fe5d89895123541d8` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `7.0.15-dev` `7.0-dev`                     | March 12th   | `sha256:69000140542d1f677b21c2e7ce2df5eff062d6ff976380a7b2195da38de2f5c8` |
|  `latest-dev` `7-dev` `7.2-dev` `7.2.4-dev` | March 12th   | `sha256:567277eeea27691c47f8b4bd2805eee9861b4ac17f3e794ab1bfa44fc999a340` |
|  `6.2-dev` `6.2.14-dev` `6-dev`             | March 12th   | `sha256:5c634273d8ca1be84a1ccdc0386758b9e58b1b7c5af763d9adbb559835fefd45` |
|  `6.0-dev` `6.0.20-dev`                     | March 12th   | `sha256:ea9dc02d29d5c5a1eea049da5dc118363b2e26278f10f4cd9c93fa9751ab80c8` |
|  `7.0` `7.0.15`                             | March 8th    | `sha256:3e82e9ac163f665d1d0a89af4c7ef13ba1afdbe1d5a131fadb70b3d965a8adf9` |
|  `6.2` `6` `6.2.14`                         | March 8th    | `sha256:ded7f100eb479de0cbfad8fc71d3c42a541999b9702acb0f569f8964b233dd56` |
|  `7` `latest` `7.2.4` `7.2`                 | March 8th    | `sha256:cbe95db042fea63742b55eb288adbbe8de2ebc0bd522d8e994c8529a45584516` |
|  `6.0` `6.0.20`                             | March 8th    | `sha256:a70ce9e3469a791fc44794160df434b36ae3decae7e0c1d7f668320a5e8086e0` |

