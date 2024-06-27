---
title: "node-lts Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node-lts Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-27 00:41:27
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/node-lts/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/node-lts/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/node-lts/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/node-lts/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                  | Last Changed | Digest                                                                    |
|--------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `next-dev` | June 26th    | `sha256:dc8334b6f7fefc575afdff76cc9deb573098b5dd5c5d8f3eb28add8009f6ac44` |
|  `latest`                | June 26th    | `sha256:b12b298b499f62d4e1f57f2875a03d14ca1526cd797985980a5e8ec4c35eb73d` |
|  `next`                  | June 26th    | `sha256:794c2bbba630d76d7c0f54552b2632e8525bf5917b7f4b21a13606c04fa9d386` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                     | Last Changed | Digest                                                                    |
|-------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `next-dev` `20-dev` `latest-dev` `20.15-dev` `20.15.0-dev` | June 26th    | `sha256:af411da35720b68abf7c84510014b5ff9f1bc6d796c86718366d18792801514b` |
|  `20.15.0` `latest` `20` `20.15`                            | June 26th    | `sha256:4f8ba369668e89cb233aa1da517fb05f769ecfc18bd1b1aceaffc8fe5e1479d8` |
|  `next`                                                     | June 26th    | `sha256:2f7946a87a2d24f8a7c9d93aaf6b291a3399bdafe5f7640bef74adada4f95f76` |
|  `20.14.0-dev` `20.14-dev`                                  | June 20th    | `sha256:1bd3303c076c8ec56df3ef088bc78efddc289b1119614d5d21324e7ee6473f1a` |
|  `20.14.0` `20.14`                                          | June 20th    | `sha256:6c1f47f8b698917c5ffd08be5840e974b02750448840fce37db90a888c222e23` |

