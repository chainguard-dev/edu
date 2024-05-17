---
title: "gatekeeper Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gatekeeper Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-17 00:44:46
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gatekeeper/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gatekeeper/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/gatekeeper/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gatekeeper/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 29th   | `sha256:8fda4e163563d17db0f5633bfbc203024b348da4bb4c5ce34876bc91e02de90e` |
|  `latest`     | April 21st   | `sha256:991a66ae28c5cf2cf28d3ab1ae5443aa02e9cf23f83f4e49706236d8299682eb` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.12-dev` `3.12.0-dev`                      | May 16th     | `sha256:02da592de09d9e20fa8f23231ed48b0f48f723bd8c11458e9a637b99d2aa8140` |
|  `latest-dev` `3.15-dev` `3-dev` `3.15.1-dev` | May 16th     | `sha256:319d54e328ea9907265e79d5668958422614e9ecbbe31f53de40a16fa65bbb32` |
|  `3.14-dev` `3.14.1-dev`                      | May 16th     | `sha256:8a2ba98b9ad9850f199471686cec9b613c04fcb6a3404d4836716bc908719204` |
|  `3.13.4-dev` `3.13-dev`                      | May 16th     | `sha256:c2c4eabb223ef37ff6d292784ce7af4f0d1c395617391608373ee2cbc33987d1` |
|  `3` `3.15` `latest` `3.15.1`                 | May 15th     | `sha256:21a6ad27ace7a163453d2d19ac35c563a2c55f38d00d923dd756b2948d902fef` |
|  `3.13` `3.13.4`                              | May 15th     | `sha256:5ecea83faaddc3fb2960069cc0b9ecdb0c8ec6f8e775fe8aaed1c23739134ac9` |
|  `3.12` `3.12.0`                              | May 15th     | `sha256:13e04435844210d74ea7974f483e9766f701c7146c780a7b14cf3138dca93061` |
|  `3.14` `3.14.1`                              | May 15th     | `sha256:c432a3d4bb0208e96d825473618dce8674fc15dff259c57254c06278bc97483f` |

