---
title: "gitness Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gitness Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-13 00:52:18
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
|  `latest-dev` | March 12th   | `sha256:7c8ae155573f834c5f5644a7569c39055efbf0d1c77d5d888163e86ee9932271` |
|  `latest`     | March 8th    | `sha256:b5ed3e6a8aef041fc1499e6a70c1b67a632fdeddd5cf1b81eb9d2e230e3fe09a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                           | Last Changed | Digest                                                                    |
|---------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3-dev` `latest-dev` `3.0-dev` `3.0.0_beta5-dev` | March 12th   | `sha256:b6f34297792d9c81efdbb543e6a44b513a6b7f0d3b8a64471e43ecb9574b9f9b` |
|  `3` `3.0` `3.0.0_beta5` `latest`                 | March 8th    | `sha256:2930c15ac2ca0fde1b182eeb5de625f83c265ccb84f837f407a33a2cf53931e4` |

