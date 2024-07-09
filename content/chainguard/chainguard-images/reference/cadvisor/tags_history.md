---
title: "cadvisor Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cadvisor Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cadvisor/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cadvisor/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cadvisor/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cadvisor/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | July 8th     | `sha256:398185d5e74e0a05d7e6302f59d16e4dd88a302d780dc2a469f81358ee119b5a` |
|  `latest-dev` | July 8th     | `sha256:030bd616264fd858d97fe1bb6913d3f0372aee394a1a6431d5caec3d8b988c00` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `latest-dev` `0.49.1-dev` `0.49-dev` | July 8th     | `sha256:9ea3309dee219f622340d1c9718e1df38dc64e6f5fb03733faca5daa21476b36` |
|  `0` `0.49` `latest` `0.49.1`                 | July 8th     | `sha256:762ef31ed9a1ca31c0b375ac91668344218221afa90c7d9ee47e69c5cdc71d20` |

