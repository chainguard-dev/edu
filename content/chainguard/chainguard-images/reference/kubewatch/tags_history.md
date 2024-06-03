---
title: "kubewatch Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubewatch Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-03 00:46:08
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubewatch/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubewatch/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/kubewatch/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubewatch/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 1st     | `sha256:aa8ff2262d552242df8b0afcb921c6fd9f21efd7c1308da2c0d8c521291e4720` |
|  `latest`     | May 23rd     | `sha256:7948c71141113d22df1d1681dd84c62e507769460e5a9864c52729503f6f51f9` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2-dev` `2.6.0-dev` `latest-dev` `2.6-dev` | June 1st     | `sha256:a41be38a2536319dd8b82e4e73093e65ed8f3caf4ab33f42b882429f1b6afa4c` |
|  `2.6` `2` `2.6.0` `latest`                 | May 23rd     | `sha256:4a1236c42ec13811da1faca883342d72c24b50022652202bbc1352ab4b9529d5` |

