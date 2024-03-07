---
title: "grype Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the grype Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-07 00:51:54
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/grype/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/grype/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/grype/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/grype/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | March 6th    | `sha256:d8b0b066b10b6466c26e09a4ae375ee0a94933b7163e808bc016126b6083d5b0` |
|  `latest-dev` | March 6th    | `sha256:702bf2ebc5694be36fbfaddce486558a0e8df3a05c84231098beebef94502251` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed  | Digest                                                                    |
|-----------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `0.74-dev` `latest-dev` `0-dev` `0.74.7-dev` | March 6th     | `sha256:4c550a96cebde749283e72537ca1db053f286a1f5347e9fc350835dd96e83112` |
|  `0.74` `latest` `0` `0.74.7`                 | March 6th     | `sha256:16745d0d8dc752879514bb709cfd1847f0502785f07ee36e5e6c77b062ada734` |
|  `0.74.6-dev`                                 | February 24th | `sha256:d5387724ca01f846d1ac86307b01a3d8ea87380305977ac662ea89e48e65f176` |
|  `0.74.6`                                     | February 15th | `sha256:dbfda491a10443aecc872cfc99de41775b740b6d3c58f11bc69735df348e26f5` |
|  `0.74.5-dev`                                 | February 13th | `sha256:1637bc03700fb4e4bcb769d55fe9179bbca98f32aa3c585796a1eb0cf598341f` |
|  `0.74.5`                                     | February 8th  | `sha256:ae6c12ac8cd08bc2821ef16598e7f923ae8cac110daeeaed80def08eb1517e8e` |

