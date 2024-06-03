---
title: "gatekeeper Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gatekeeper Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-03 00:46:08
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gatekeeper/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gatekeeper/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/gatekeeper/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gatekeeper/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 1st     | `sha256:8028637671482faa1ca03ed72397fa404d4c11474b60b7975a24d9dd80798dd4` |
|  `latest`     | May 31st     | `sha256:54f67bec928b96874ea6232415230cba5c49df6cdf6ceb6b2aeb7d674b80b3b6` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.15-dev` `3.15.1-dev`                      | June 1st     | `sha256:8f9e1df60fe9f66a3f20a669b917dc42095e9c08e6f7a5c0cc240737ac39e9bc` |
|  `3.15.1` `3.15`                              | June 1st     | `sha256:5a6f604ed31b47f01f31a6b194302e8ad79452791ffdefd4df3bb858624f1985` |
|  `3.13-dev` `3.13.4-dev`                      | June 1st     | `sha256:ee1851455e0c4f4e6ca9dc294a9fa7a75b896964cfb2a0c3e40f552538c31697` |
|  `3.12-dev` `3.12.0-dev`                      | June 1st     | `sha256:b09f07f72bd4dac43fa0156f033d785f71c1edaf5ec90307340646d2e6a5e57d` |
|  `3.16.3-dev` `3.16-dev` `3-dev` `latest-dev` | June 1st     | `sha256:e71f1fcb5ac478e4e910d1c597ba5487542af4e337ec733ac39ac38967cdee8e` |
|  `3.14.1-dev` `3.14-dev`                      | June 1st     | `sha256:723316c4f20144084c8498a6d0e307fd9124344942b7fd423caf47e3d2a46712` |
|  `3` `3.16.3` `latest` `3.16`                 | May 31st     | `sha256:fae5f0c1f6b37d5929f518f933111eecbdf99cbb08b7b1efce4f15608930ea92` |
|  `3.13.4` `3.13`                              | May 23rd     | `sha256:1a015091cc3bbddcfdcad787e0f8465950ebfa5e13e174657fa56fa4a9cc811d` |
|  `3.12` `3.12.0`                              | May 23rd     | `sha256:20c31059e0b3677227fe6e441d742ed16e7b96278e610dce1290c42aaad1929e` |
|  `3.14.1` `3.14`                              | May 23rd     | `sha256:149be9c2a6f16e05168eed28b2aaf7f9654438e2d2018d7cfd4696ba446f33f3` |

