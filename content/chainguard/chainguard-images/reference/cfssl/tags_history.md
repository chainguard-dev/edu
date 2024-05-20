---
title: "cfssl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cfssl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-20 00:48:18
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cfssl/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cfssl/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cfssl/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cfssl/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 17th     | `sha256:cc7b26803877ecced1a581101f8ae0beab6dbb5396b563b49f2ca38c0bc4140f` |
|  `latest-dev` | May 17th     | `sha256:1204ccf05e6e81d1091b285201058d7798f2e38065243d09fc98ea9f3c31498a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.6-dev` `latest-dev` `1.6.5-dev` `1-dev` | May 19th     | `sha256:b8b278627b2c3dda311e2edcb2807897721d33d4d94d6d8e9229f56ba6f3dcb7` |
|  `1.6` `1` `latest` `1.6.5`                 | May 17th     | `sha256:0cc820b4c86c769b552b55341b6e02e7db987c0fd1e7323a87f9b04237be9212` |

