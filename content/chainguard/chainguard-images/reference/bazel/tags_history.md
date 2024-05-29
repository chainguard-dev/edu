---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-29 00:38:53
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
|  `latest`     | May 23rd     | `sha256:578a2e1df1ec219f686c6a05196f0d0b1d28ea411effb32cf50f509f0ebed0ce` |
|  `latest-dev` | May 23rd     | `sha256:8bc941dfd87f0b316df65af6fb6d7e601e79d4793df1fdb0dd662474eb689992` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `7.1.2` `7.1` `7`                 | May 28th     | `sha256:d6f413d969e7b12f1eabd75a62c653e978ef29f0fd7d562c8e020e00818e6c2b` |
|  `5.4` `5` `5.4.1`                          | May 28th     | `sha256:f13578be56f666b666fb70d3777b007e7fb27894c952b9539baffbfe908265e3` |
|  `5.4-dev` `5-dev` `5.4.1-dev`              | May 28th     | `sha256:f68e3b250e510cce31a9a6d50031c497ac0ccedade28ca46d0f8b86b5d2a09f6` |
|  `6.5-dev` `6.5.0-dev` `6-dev`              | May 28th     | `sha256:412b671ddb52e13e33e00311b304766fd4f7dc624f587798caba513bbe6f41cd` |
|  `7.1.2-dev` `latest-dev` `7.1-dev` `7-dev` | May 28th     | `sha256:1f9f7d6403ea78b741c95606ce1c2fa0d7e13e09d08660a1334e12510ab1ab2f` |
|  `6.5.0` `6.5` `6`                          | May 28th     | `sha256:d7275ddfe59244282f151f9c0166602fa9a31ed15969d94e06cdd941c7373204` |
|  `7.1.1`                                    | May 9th      | `sha256:14417579783d4513144a3ed611a6b3dbb2c5cc51453ad7c11cf3cdb595d737b2` |
|  `7.1.1-dev`                                | May 9th      | `sha256:cdd252e8dac5c1ceccfa2b49bb2279867f4c5686a559e40122327b9b37a114f7` |
|  `6.1.2` `6.1`                              | May 22nd     | `sha256:eed2d4f320442b1498ee44dc54efd331844d9e2c7ec1a2ff0458bd2762172d0c` |

