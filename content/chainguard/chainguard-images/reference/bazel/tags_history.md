---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-27 00:43:34
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
|  `5.4.1-dev` `5.4-dev` `5-dev`              | May 24th     | `sha256:6232b2b84012a102e6b33b5827b9d55cb8ce56aaa75f3eaf04ee44be5598f41f` |
|  `7-dev` `7.1-dev` `7.1.2-dev` `latest-dev` | May 24th     | `sha256:095ae0f0fed5bcf6f1ab45f6a4838bf5bc48c67dddb7688d27d14b784ad58750` |
|  `5.4.1` `5.4` `5`                          | May 24th     | `sha256:869435507aa61b6ccca836a49722364151ded73246f45f77c7824c2bb4f616c0` |
|  `6.5.0` `6` `6.5`                          | May 24th     | `sha256:27cb2307bc554daa30e8219f27382d2848318aeff99e2b4e4cd95987c881ea9d` |
|  `6-dev` `6.5.0-dev` `6.5-dev`              | May 24th     | `sha256:778cd425487777acf5f7bb9035b93ee3fad0f33a746751fe6ae62d9cb77cd15b` |
|  `7.1` `latest` `7.1.2` `7`                 | May 24th     | `sha256:954bec51389cd541472df27ecc88581601be999e8f553b2fed70d4e6730020b0` |
|  `7.1.1`                                    | May 9th      | `sha256:14417579783d4513144a3ed611a6b3dbb2c5cc51453ad7c11cf3cdb595d737b2` |
|  `7.1.1-dev`                                | May 9th      | `sha256:cdd252e8dac5c1ceccfa2b49bb2279867f4c5686a559e40122327b9b37a114f7` |
|  `6.1.2` `6.1`                              | May 22nd     | `sha256:eed2d4f320442b1498ee44dc54efd331844d9e2c7ec1a2ff0458bd2762172d0c` |
|  `6.1.1`                                    | April 28th   | `sha256:e779a5ec7dfce8190755a7c683f3f8fed331ac6909ec52270d35362fba8df214` |

