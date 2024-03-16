---
title: "karpenter Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the karpenter Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-16 00:33:13
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
|  `latest-dev` | March 15th   | `sha256:929808128b644b4eb37ffc61d0b9495d00c2d8216094690efd0e1a2dcbef32f3` |
|  `latest`     | March 15th   | `sha256:66519b9e4f452944e60881094db25cf2774af1c33a16b3d5a5ae9cfd021abb6c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed  | Digest                                                                    |
|-----------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `0` `0.35.2` `latest` `0.35`                 | March 14th    | `sha256:7873c9feb6f9d8188f56508ff8d4ebdd34210c028953968aa62ce041eb974f40` |
|  `0-dev` `0.35-dev` `0.35.2-dev` `latest-dev` | March 14th    | `sha256:8ed6a3d750cd0a63bec7b4f7454dbf549035d3e90d468cb140dbd0bb5b6b1b00` |
|  `0.35.1-dev`                                 | March 14th    | `sha256:95a70555545ade8de2658610b8ac94c775f4c450ca9901914ad19d8bf89ee8ff` |
|  `0.35.1`                                     | March 14th    | `sha256:668d926c5c0cb5967c837c74e724c04ac0e2cca22c6c0a74b6092f250e6e4a7d` |
|  `0.35.0-dev`                                 | March 8th     | `sha256:7067122f87bbd96f941e48c4fa7f9919ca226002fcbefed01a9b8be9ef8cce5f` |
|  `0.35.0`                                     | March 8th     | `sha256:4468e9595d5c475dd4b9d4ebcf561eb8c05c019eebd949eca287fa8e92a155ab` |
|  `0.34-dev` `0.34.1-dev`                      | February 26th | `sha256:ea6f1b7b07c884e7be07c3a93c716465b8220fbe2bf84a7f49cc1bf440c35865` |
|  `0.34` `0.34.1`                              | February 26th | `sha256:825d24feda8cac13f08fc41114b873f8a42b46b3037eabeb39f0de8a6ab20e08` |
|  `0.34.0-dev`                                 | February 17th | `sha256:bc792a458800ee813131a0f93d7621e8a6bd926b5a28fe296e502d5b23b22480` |

