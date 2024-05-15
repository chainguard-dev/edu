---
title: "cosign Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cosign Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-15 00:39:35
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cosign/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cosign/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cosign/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cosign/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 14th     | `sha256:55e91b70d645a0a02e079fd7f8671ec7cdb518b85312cb6ff2afcbff0dd2cc2e` |
|  `latest`     | May 13th     | `sha256:76811e01b592cf518801e3d6bb490f9a1ff8831ab9142411c010ccd11176da70` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2-dev` `latest-dev` `2.2-dev` `2.2.4-dev` | May 14th     | `sha256:5b5f1f576cffa99f6ae78195e00ce54f99fa03efa0999b06730d8d50325c1018` |
|  `2` `2.2` `latest` `2.2.4`                 | May 13th     | `sha256:13d8cac50b538a54161b4d2813edeb6cb28c4b0ed5a3fd951011eac6f9000cef` |
|  `2.0.1-dev`                                | April 25th   | `sha256:0f8ffca811eab50fbca70379a3316113075cc46b8a09e880f7d831bdb66f689e` |
|  `2.0.1`                                    | April 25th   | `sha256:1418e13c3479d1a8d068325a97a4a4fbf437d12cb6d5fbfb7160c2f40a239e0b` |

