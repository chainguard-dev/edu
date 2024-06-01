---
title: "loki Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the loki Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-01 00:50:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/loki/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/loki/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/loki/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/loki/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 31st     | `sha256:3d864585734ba8f57ae699cad511601839c6716eeca4efaa57a40a3da3e6feef` |
|  `latest`     | May 31st     | `sha256:52a0823f914f4377ae2dcbc3514ef3696f26996c037138a00bb14bd4d539b46b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.9` `2.9.8` `2`                          | May 31st     | `sha256:ac765caec4efcebaa3bd7676d8e93de3336990d85bb0b51adb4db07951b31905` |
|  `2.9-dev` `2-dev` `2.9.8-dev`              | May 31st     | `sha256:f9803987c177a057ff01d5e98c79240703737165dec65478eaa579bc1119cfaa` |
|  `3-dev` `3.0-dev` `3.0.0-dev` `latest-dev` | May 31st     | `sha256:851b580218f9d9120745d5e88008db599730648fce59abbf9c05aa236cefcd32` |
|  `3.0.0` `latest` `3.0` `3`                 | May 31st     | `sha256:5e8b233a34c3eb8bb80289a20ba886c027f01d881eaf0190913a3b54ebb8ee39` |

