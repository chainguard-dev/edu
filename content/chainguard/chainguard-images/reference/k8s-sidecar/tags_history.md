---
title: "k8s-sidecar Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the k8s-sidecar Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-11 00:42:18
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/k8s-sidecar/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/k8s-sidecar/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/k8s-sidecar/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/k8s-sidecar/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | June 10th    | `sha256:e3e06f7c39b4534a19e29697eed0c3618d1aa12daafd4a73c05d2a91fedcd171` |
|  `latest-dev` | June 10th    | `sha256:2ebc3a779ce801550dfe8c8af262a1652d839503e3b875ef2b150b9f194f9cd1` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1-dev` `latest-dev` `1.27-dev` `1.27.4-dev` | June 10th    | `sha256:194b045cfc44625b4c0c2609e935fd087b195148420303a4b58d6797cd90ac5d` |
|  `1.27.4` `1` `1.27` `latest`                 | June 10th    | `sha256:746083e9a738ece188a3cbacd663f5867fb63ca3947a303c8c1d1787b82d78d6` |
|  `1.27.2-dev`                                 | June 8th     | `sha256:be5114c2762d526652d8200774cac898cfe18d9f57c6f1c5305de8bc7ea023b7` |
|  `1.27.2`                                     | June 7th     | `sha256:05a1037de948e94fff3db1a7cc4b1a65a29e39bc4c87be14a5f810a65c22bc0e` |

