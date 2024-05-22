---
title: "karpenter Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the karpenter Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-22 00:47:17
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
|  `latest-dev` | May 21st     | `sha256:de410a19cb23f5222b18a2704145a64ee172f62b1a03c6b9a159b1298eb2d9a4` |
|  `latest`     | May 21st     | `sha256:7a628c84996cc08e162ada14c7c2e8ea532b2133f2d26424421cc9fee89c711f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.35.5-dev` `0.35-dev`                      | May 21st     | `sha256:451a636c952d64a15af2d9a0a2108ae8ede03d02c503b950c60446cc31ed4cbf` |
|  `0` `0.36.2` `0.36` `latest`                 | May 21st     | `sha256:4602f760a62784b516830e44313295abc87712b30c0746b75c65d69b89c790a5` |
|  `0-dev` `0.36-dev` `0.36.2-dev` `latest-dev` | May 21st     | `sha256:4bf0f5c95261a83c894107ea8cb8d4aa385e4b3eb3ee280395e0766608b671c3` |
|  `0.35.5` `0.35`                              | May 21st     | `sha256:defba893d03306218f0f929f16a3c59a4b45b6cb383dcfd0d706d1eea3fdb341` |
|  `0.36.1`                                     | May 17th     | `sha256:0a935ec98ddc791e0c1b8fc34fdb9594afea1c18d65a2af5401820e988bb4ea6` |
|  `0.35.4-dev`                                 | May 17th     | `sha256:c94fc93a28c5f83b4d9534a965357c7609dcd2eff547f6371ac33837846d7317` |
|  `0.36.1-dev`                                 | May 17th     | `sha256:e3f10653dc220b01fc118dd7d136b6ebca81747e0a3a28e7e13add5f1a5747a9` |
|  `0.35.4`                                     | May 17th     | `sha256:48a59e7c1f99300ac662026149d8102240b75823f36a6f104484b0cd525f12e4` |
|  `0.36.0-dev`                                 | April 24th   | `sha256:1b83625e12dddb2f149638a7285b740842a4170620be390641c328f205d033f2` |
|  `0.36.0`                                     | April 24th   | `sha256:0f1a24830639d33071b2b664059e959446c245422e297d1e10767a05c8d45df5` |
|  `0.27.3-dev`                                 | May 18th     | `sha256:a405e263d57806202ab82af5746b7440c3b6b4e0bf41332cbc4f65e97906c47b` |
|  `0.27.3`                                     | May 18th     | `sha256:f85daa0707bf2bd1d3ebfd6a7965801d74da50d29910d2ef4c74d6b9c1b90f56` |

