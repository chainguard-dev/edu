---
title: "karpenter Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the karpenter Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-10 00:53:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/karpenter/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/karpenter/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/karpenter/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/karpenter/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 9th    | `sha256:a0b6e3a8a2cb5de1b1a942125376fa4c2fb6b17da8463cb0577e9ef3c138861a` |
|  `latest`     | April 4th    | `sha256:2325e5691523110621285f9d4839a21f6170121d9c3ed81bc415fe6f21d2deef` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `0.35-dev` `0-dev` `0.35.4-dev` | April 9th    | `sha256:8cc27be69489e27ab451f1fef40c01ae809b2d0e4d7497b07354e4d8468958fa` |
|  `0.35.4` `latest` `0` `0.35`                 | April 4th    | `sha256:6832ddcaf4b8f542b81bd5c3ba02ed4b9917688ae997a36e6168318e035a80cb` |
|  `0.35.2-dev`                                 | April 2nd    | `sha256:74e3f2c40db018adab0ec934cb1089d3506d311bf1eec2e1a23d2953649660b1` |
|  `0.35.2`                                     | March 28th   | `sha256:8ec243996c11256ac91c346a1c44b2d5691d37584b410739e57920bd65d699e2` |
|  `0.35.1-dev`                                 | March 14th   | `sha256:95a70555545ade8de2658610b8ac94c775f4c450ca9901914ad19d8bf89ee8ff` |
|  `0.35.1`                                     | March 14th   | `sha256:668d926c5c0cb5967c837c74e724c04ac0e2cca22c6c0a74b6092f250e6e4a7d` |

