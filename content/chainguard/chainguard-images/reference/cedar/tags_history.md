---
title: "cedar Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cedar Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-14 00:46:23
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cedar/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cedar/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cedar/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cedar/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 13th     | `sha256:05af9af4b6e8970b555d208350572ee3de114c2b0c5dfb88048a52df6a3358ee` |
|  `latest`     | May 2nd      | `sha256:b4348c91fd22b61c5e1f9bb4ee37ece5984955c83f6f9aec725466cd1aa21978` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3-dev` `latest-dev` `3.1-dev` `3.1.3-dev` | May 13th     | `sha256:d780b171d8e36d9f2a5db3ff6cd7314fc68516affbf835c0fb4ee41057a928ae` |
|  `3.1` `3` `latest` `3.1.3`                 | May 2nd      | `sha256:047960a37aba801d40e77bf80a1c78b2f3911ec431a123f78fe63312f7ba720a` |

