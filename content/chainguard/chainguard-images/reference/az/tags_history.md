---
title: "az Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the az Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-10 00:36:03
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
|  `latest-dev` | July 9th     | `sha256:17101745c7acd697d81273eba8b11c3577f8112fb20d2626581e34699e359332` |
|  `latest`     | July 9th     | `sha256:6ab815c6cd6d99bd21ba0fc93b5f1aff5e34cb5aa91202e9018dadfdcb5ed95a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.62.0-dev` `latest-dev` `2.62-dev` `2-dev` | July 9th     | `sha256:8fb916a63111753db2dd1b597bd20b0569a54a91c654bdbeb6ec1128b0477dfc` |
|  `2.62` `latest` `2.62.0` `2`                 | July 9th     | `sha256:efcdf81251caacb8b5bdf11080678ed24fc2d92a682c45dfb05a7fe104efbbdc` |
|  `2.61` `2.61.0`                              | July 8th     | `sha256:9ab7f514b9476c5709ae90bab366020e34b74ab42958b87b23e1d68f2e7b4c5d` |
|  `2.61.0-dev` `2.61-dev`                      | July 8th     | `sha256:46cc216d5e3b46ad73f90b2bec77484fcd4c85852d2f56cbc802841434f3f5cb` |

