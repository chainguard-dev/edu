---
title: "gitness Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gitness Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gitness/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gitness/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/gitness/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gitness/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 15th     | `sha256:fd39d3ff1553b22406dcf27ef39cfe8ee9f36948ef3174edaa1985c134a59371` |
|  `latest-dev` | May 15th     | `sha256:96253ec934ad8504f61f42edde6e8d0401f045d9293b2d3e11e482efbaeefe94` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                           | Last Changed | Digest                                                                    |
|---------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `3.0` `3.0.0_beta6` `3`                 | May 15th     | `sha256:f63144008e6d68ba0d217dd3bd7a90ca705418db1137aa0aeb88843437dcb1ac` |
|  `3.0-dev` `3.0.0_beta6-dev` `3-dev` `latest-dev` | May 15th     | `sha256:199f21b20bfbbb42fa9c4cbd2be2f4a124a8fc67e3e99a2a4afaf6155c2be4ac` |

