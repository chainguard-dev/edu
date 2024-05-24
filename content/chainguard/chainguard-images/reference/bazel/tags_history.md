---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-24 00:45:45
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
|  `7.1.2` `7.1` `7` `latest`                 | May 23rd     | `sha256:7f33093318f231784d06668aef6d5c547a28f6fc98cc50c24e77b11944109496` |
|  `latest-dev` `7.1.2-dev` `7.1-dev` `7-dev` | May 23rd     | `sha256:64fc844bf019725b3f2244d1b84e1a9bae57c30f051a1b69ec6f345678e5a0bd` |
|  `6.5` `6.5.0` `6`                          | May 23rd     | `sha256:f9a16ffb3a145e1c3baf1441f73a52864d0882688ca89c2a4d5b8a2c17118eeb` |
|  `6.5.0-dev` `6.5-dev` `6-dev`              | May 23rd     | `sha256:b18b014cd5cb74b7241bed0265fc0546d2754a272f767a56137d4309884bef07` |
|  `5.4.1` `5.4` `5`                          | May 23rd     | `sha256:3515e717db9c77b98e5d69e768eeafd668b9b84d0a576660b486c7b4e75e9a08` |
|  `5-dev` `5.4.1-dev` `5.4-dev`              | May 23rd     | `sha256:bf7d6a871747764e7a573d79c62336aa434558cf221500276ca1946914b33e49` |
|  `7.1.1`                                    | May 9th      | `sha256:14417579783d4513144a3ed611a6b3dbb2c5cc51453ad7c11cf3cdb595d737b2` |
|  `7.1.1-dev`                                | May 9th      | `sha256:cdd252e8dac5c1ceccfa2b49bb2279867f4c5686a559e40122327b9b37a114f7` |
|  `6.1.2` `6.1`                              | May 22nd     | `sha256:eed2d4f320442b1498ee44dc54efd331844d9e2c7ec1a2ff0458bd2762172d0c` |
|  `6.1.1`                                    | April 28th   | `sha256:e779a5ec7dfce8190755a7c683f3f8fed331ac6909ec52270d35362fba8df214` |

