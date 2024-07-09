---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/bazel/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/bazel/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/bazel/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/bazel/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 8th     | `sha256:f48af9129d00677c4975cf6502918d4cc60427f3356ea06f0b1bb4811387656d` |
|  `latest`     | July 8th     | `sha256:db936031d4f5ada0ebb6929defa3be8e46b78dc87c7e220b843cda551bc87572` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `7.2` `latest` `7` `7.2.1`                 | July 8th     | `sha256:3c613e2099280843a3d34020d1fbe4ab44ee1d02c3b31f1014c496e18e5a086d` |
|  `6` `6.5` `6.5.0`                          | July 8th     | `sha256:54001e1b8cdbc0f1620e521da2eb337d66d759c0ae34c0812bd6f50d260bebf1` |
|  `7-dev` `7.2.1-dev` `7.2-dev` `latest-dev` | July 8th     | `sha256:751f46c0bf867c701763a44f4d8ac8e8b67eed49c7d0ec7c70cd50238cb4d0af` |
|  `5.4.1` `5.4` `5`                          | July 8th     | `sha256:7d000050b63d7e2f5f759d8f5b3700914b1bc5cd8ce4cace110d08c64b123c35` |
|  `6.5-dev` `6-dev` `6.5.0-dev`              | July 8th     | `sha256:22b206afef94656b2e4f2c1b54ea09103e4ba0705dd82b39590ad8bf53c34e57` |
|  `5.4.1-dev` `5-dev` `5.4-dev`              | July 8th     | `sha256:1911d75b83f093b72802ff6da18489c6be2712163b46e96b729b3acf6c0ca32f` |

