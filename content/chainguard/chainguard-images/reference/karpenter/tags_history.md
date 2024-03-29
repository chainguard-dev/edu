---
title: "karpenter Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the karpenter Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-29 00:47:42
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
|  `latest`     | March 28th   | `sha256:d81145d34298f3a5317d3e94727a83f28e81ceb474773e094d222f165aae865d` |
|  `latest-dev` | March 28th   | `sha256:816e28a5a6440412e49271c5fcdf2f65f29056b425da7e38726ad369e97a2d5d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.35` `0` `latest` `0.35.2`                 | March 28th   | `sha256:8ec243996c11256ac91c346a1c44b2d5691d37584b410739e57920bd65d699e2` |
|  `0.35-dev` `latest-dev` `0.35.2-dev` `0-dev` | March 28th   | `sha256:74e3f2c40db018adab0ec934cb1089d3506d311bf1eec2e1a23d2953649660b1` |
|  `0.35.1-dev`                                 | March 14th   | `sha256:95a70555545ade8de2658610b8ac94c775f4c450ca9901914ad19d8bf89ee8ff` |
|  `0.35.1`                                     | March 14th   | `sha256:668d926c5c0cb5967c837c74e724c04ac0e2cca22c6c0a74b6092f250e6e4a7d` |
|  `0.35.0-dev`                                 | March 8th    | `sha256:7067122f87bbd96f941e48c4fa7f9919ca226002fcbefed01a9b8be9ef8cce5f` |
|  `0.35.0`                                     | March 8th    | `sha256:4468e9595d5c475dd4b9d4ebcf561eb8c05c019eebd949eca287fa8e92a155ab` |

