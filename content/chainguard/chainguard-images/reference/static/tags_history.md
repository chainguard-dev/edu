---
title: "static Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the static Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
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
|  `latest-glibc` | July 8th     | `sha256:b2fc225f85e3a5fad4bead8a647ed7e8e80c659db027c2e8ad813c30b6561d8d` |
|  `latest`       | July 5th     | `sha256:d94c01c30dda455626c9642272b489adfc402982b99849149ca678ff4d45b267` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                  | Last Changed | Digest                                                                    |
|--------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-glibc` `latest` | July 8th     | `sha256:f48ae8fd738b0cbe64ea2e418dcd9eacb6fdaf97bb2abd7cf5218aa9f525c5ff` |

