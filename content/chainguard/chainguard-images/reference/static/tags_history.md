---
title: "static Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the static Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-07 00:45:47
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/static/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/static/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/static/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/static/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)         | Last Changed | Digest                                                                    |
|-----------------|--------------|---------------------------------------------------------------------------|
|  `latest`       | May 6th      | `sha256:873e9709e2a83acc995ff24e71c100480f9c0368e0d86eaee9c3c7cb8fb5f0e0` |
|  `latest-glibc` | May 2nd      | `sha256:40eac219c658d4a0fe7535f583a89d42784ed00292db034310ebacb0f007d735` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                  | Last Changed | Digest                                                                    |
|--------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `latest-glibc` | May 2nd      | `sha256:918e0fcd489fcdb64e7370c914dee2d0f3dc29a3b23e445f7e75a25717cfee41` |

