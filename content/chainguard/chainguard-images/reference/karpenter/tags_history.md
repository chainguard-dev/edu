---
title: "karpenter Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the karpenter Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-27 00:48:55
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
|  `latest`     | March 18th   | `sha256:759320b32272c634d1bf57ed730775dfe6763c904d2674d17fb2c86f97c31121` |
|  `latest-dev` | March 18th   | `sha256:6ded0b71bbb992fb371ce92a244d29da912855d703f0d5b86b70ddd3584ffd94` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.35-dev` `latest-dev` `0-dev` `0.35.2-dev` | March 25th   | `sha256:7605013c0cecfc13be32ef9e97208eedb0d43e589c27b83e55d41b7a4ae26906` |
|  `0.35` `latest` `0.35.2` `0`                 | March 18th   | `sha256:de28b6faabe245531a873ac1395c7cf4bc9b37778427f13221e44d29770e70a8` |
|  `0.35.1-dev`                                 | March 14th   | `sha256:95a70555545ade8de2658610b8ac94c775f4c450ca9901914ad19d8bf89ee8ff` |
|  `0.35.1`                                     | March 14th   | `sha256:668d926c5c0cb5967c837c74e724c04ac0e2cca22c6c0a74b6092f250e6e4a7d` |
|  `0.35.0-dev`                                 | March 8th    | `sha256:7067122f87bbd96f941e48c4fa7f9919ca226002fcbefed01a9b8be9ef8cce5f` |
|  `0.35.0`                                     | March 8th    | `sha256:4468e9595d5c475dd4b9d4ebcf561eb8c05c019eebd949eca287fa8e92a155ab` |

