---
title: "harbor-core Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the harbor-core Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-07 00:46:50
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/harbor-core/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/harbor-core/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/harbor-core/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/harbor-core/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 5th     | `sha256:41638621dc5f1814aa651a5b46b1fa666c9e4f5d645770cbace8f9b67bc4dfc2` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.10-dev` `2.10.2-dev`                    | June 6th     | `sha256:0ffae0e141fb18738a11e8f775850d31bec1baff2d1aabe8d4b1bb8862267757` |
|  `2.10.2` `2.10`                            | June 6th     | `sha256:8eb6e2917e7c06166d7b607b8966c0130dc54cf4d6ec5618996b5ad59224a287` |
|  `2.9.4-dev` `2.9-dev` `2-dev` `latest-dev` | June 5th     | `sha256:0c08e68d34343bb00e35b825492b192dd371cbcb48bb3a83db0a672a264c6b05` |
|  `2` `latest`                               | June 1st     | `sha256:295f4cf25e0a6c7faebeac36e6409080297dca36a77ab6d9506ad595926c7970` |
|  `2.8-dev` `2.8.6-dev`                      | June 1st     | `sha256:f2af6c17343f3565d52fda5ac866dcf9c3d0b519ce236797e5ad4aa0aeafdd7a` |

