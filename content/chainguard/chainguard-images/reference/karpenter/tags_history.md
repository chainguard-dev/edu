---
title: "karpenter Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the karpenter Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/karpenter/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/karpenter/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/karpenter/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/karpenter/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | July 8th     | `sha256:e987ea0091911980433b61b9a985470eb19f7a2fafc41928e680aa1850e38ba7` |
|  `latest-dev` | July 8th     | `sha256:d613c9befd7845dbd79a2c776858978dac99807faf20258e6321e067646241e8` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.35` `0.35.5`                              | July 8th     | `sha256:7a25be93379de412cd3b183b1cfe50c3521735c482e642251ac50d379ec0eb05` |
|  `0-dev` `latest-dev` `0.37-dev` `0.37.0-dev` | July 8th     | `sha256:a0e41437db25382a6c45c5a9039a66c5136d15d45bf3ab44f9856acac714a5de` |
|  `0` `0.37` `0.37.0` `latest`                 | July 8th     | `sha256:aa4f4de624ee52d2a5cad883d649c0675514bad788ca4f86e2e9aeebf8ff3a48` |
|  `0.35-dev` `0.35.5-dev`                      | July 8th     | `sha256:de92ef5e0b3c817a818b0a5d9c6909ed8ba9fb38ec28fde7d661292487fc878e` |

