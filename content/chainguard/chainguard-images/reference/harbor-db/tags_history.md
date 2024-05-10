---
title: "harbor-db Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the harbor-db Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-10 00:43:45
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/harbor-db/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/harbor-db/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/harbor-db/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/harbor-db/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | April 29th   | `sha256:d33d7a54746a3aed2113b5faaa3262cc1115b64b8cfa8fbcb7fc0266572d80f4` |
|  `latest-dev` | April 29th   | `sha256:dbca9af7bbab9ca670d63838844c25596d959ea395377b23b66dc0816c0f5d09` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.8-dev` `2.8.6-dev`                        | May 9th      | `sha256:9529e895f7d4a0d2ee04b0e044adb2166ad511ef5376e86e390b43a50d14ce0c` |
|  `2.9-dev` `2.9.4-dev`                        | May 9th      | `sha256:573e9a304fd6af2f2ef5052b671f941606096628e9d5239def3ec7410ebf746c` |
|  `2.8` `2.8.6`                                | May 9th      | `sha256:987bac713c467c704345f8d23ba98abf3089963409bb027689b70e7292e313dc` |
|  `2.9.4` `2.9`                                | May 9th      | `sha256:ee8a9bccaef544551289f6df0e975d901718923ba834f56233f2d0259582e149` |
|  `2.10.2` `2` `2.10` `latest`                 | May 9th      | `sha256:3f3900e6bbcae25671479066763370a18e461b6a7f90b1c77bb773fda4a7a571` |
|  `latest-dev` `2-dev` `2.10-dev` `2.10.2-dev` | May 9th      | `sha256:3b8bd5780331dda14aac41787005b7d9ace0af8ecf597cc3b19cea71acd4c97f` |

