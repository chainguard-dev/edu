---
title: "karpenter Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the karpenter Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-15 03:08:24
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
|  `latest-dev` | April 11th   | `sha256:ba97bfcffee0fe9757abcc81300f7bb4fdcd495843b145f58c9795f8667b7237` |
|  `latest`     | April 11th   | `sha256:2fa1f66d366ae5d2f594c5942e6ed02007c2242ff7877c10a7f970a044ed35a5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `0.36.0-dev` `0.36-dev` `latest-dev` | April 11th   | `sha256:1b10d81376c94c274a90097f2f744d03f9d3914f19cd3d8e327f911eb6a6a957` |
|  `0` `0.36` `0.36.0` `latest`                 | April 11th   | `sha256:9435066652ea84fab4f6970eb8eacfc34c9962c28746767bb665ffdc8daac8de` |
|  `0.35-dev` `0.35.4-dev`                      | April 9th    | `sha256:8cc27be69489e27ab451f1fef40c01ae809b2d0e4d7497b07354e4d8468958fa` |
|  `0.35.4` `0.35`                              | April 4th    | `sha256:6832ddcaf4b8f542b81bd5c3ba02ed4b9917688ae997a36e6168318e035a80cb` |
|  `0.35.2-dev`                                 | April 2nd    | `sha256:74e3f2c40db018adab0ec934cb1089d3506d311bf1eec2e1a23d2953649660b1` |
|  `0.35.2`                                     | March 28th   | `sha256:8ec243996c11256ac91c346a1c44b2d5691d37584b410739e57920bd65d699e2` |

