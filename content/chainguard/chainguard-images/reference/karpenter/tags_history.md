---
title: "karpenter Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the karpenter Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-08 00:34:55
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
|  `latest-dev` | July 3rd     | `sha256:3186a3117cdf5432ee8d33aae2065733227b43b1d370232d46375494b424651f` |
|  `latest`     | July 3rd     | `sha256:5f90ec99015ae1c9dcd180e102d3cf554841fc2b3d136fce1132b5d55c9dff4e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.37` `0.37.0` `latest` `0`                 | July 6th     | `sha256:167d760d0247c1bc7c9f8f418d5f05b7e83d0aea69b843a9f4b591355fb25fd9` |
|  `0.35.5` `0.35`                              | July 6th     | `sha256:fe7fc110e7baa3227b6f9d67cd5e2a15b7009876229a5aaf8a12ad2319a18efb` |
|  `0.37.0-dev` `latest-dev` `0-dev` `0.37-dev` | July 6th     | `sha256:3d746d3167337fe9f76609509a7e89585ecd97333ee1b5e65e5728001335a557` |
|  `0.35.5-dev` `0.35-dev`                      | July 6th     | `sha256:0a15f2c5a83fe34dda2369d948c31c86a087e6b722ea63a8a5b0ac756de6f8ed` |

