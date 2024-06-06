---
title: "istio-pilot Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the istio-pilot Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-06 00:48:16
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/istio-pilot/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/istio-pilot/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/istio-pilot/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/istio-pilot/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 5th     | `sha256:6d1faf1fcc3dc3f5d9393929cf3408dd1c48811bf662fa492e11ebede07bb165` |
|  `latest`     | June 5th     | `sha256:003d3604bf67deb0ad10aaab6b3d7801fa323b11d057b5a30b46baba75a86e05` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.20.6-dev` `1.20-dev`                      | June 5th     | `sha256:8e581f0f572171c8815b9463c5e0baafebc7daf7986b86d27dd5a6e95f09456e` |
|  `1.20` `1.20.6`                              | June 5th     | `sha256:3387049243931afc2a858587623a0c83cd6bdce0dcd54ec4c5849bb33a5dafbf` |
|  `1.21` `1.21.2`                              | June 5th     | `sha256:b8719eeb03f7789e58906da546110e87053003e4ad4b744e4d9842ffde3bef81` |
|  `1.21-dev` `1.21.2-dev`                      | June 5th     | `sha256:fe1444e4a78f0b54a25a2655959cb3a5646c42f3be53fbc10033664b624c8ca3` |
|  `1-dev` `latest-dev` `1.22-dev` `1.22.0-dev` | June 5th     | `sha256:6586c5a18589d885070c9cb66d73da4c311d3954d14e9aa36f40aea0e5f19f97` |
|  `1.22` `1` `latest` `1.22.0`                 | June 5th     | `sha256:1199a5cc4492ee9c7481c1fc936cb1a3caeb4f46c29cfe058f29eee386299705` |

