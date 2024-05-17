---
title: "cosign Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cosign Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-17 00:44:46
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
|  `latest-dev` | May 16th     | `sha256:152b35aee2e6894e23d0ffed2ea333b8ffe479dc44b1979f6ca2592df81db3dc` |
|  `latest`     | May 15th     | `sha256:f08db80668bc8b48aea087dc486acbbfc2979bd2f43dfe8b09a47777a6ffc366` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `2.2-dev` `2.2.4-dev` `2-dev` | May 16th     | `sha256:8a48589cc92a7f45db3d82c6cecf300e451b68dd5545615be19898552f6195da` |
|  `latest` `2.2` `2.2.4` `2`                 | May 15th     | `sha256:1729d3bbdcf3ac4493e25fc0c1e35b0dadecb1619ba2dabbb333a07d8365686d` |
|  `2.0.1-dev`                                | April 25th   | `sha256:0f8ffca811eab50fbca70379a3316113075cc46b8a09e880f7d831bdb66f689e` |
|  `2.0.1`                                    | April 25th   | `sha256:1418e13c3479d1a8d068325a97a4a4fbf437d12cb6d5fbfb7160c2f40a239e0b` |

