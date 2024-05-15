---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-15 00:39:35
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
|  `latest`     | May 14th     | `sha256:ed92931e716e1559128333da4bafa91cc3c1ff6e39bfd534baf02f03ea440743` |
|  `latest-dev` | May 14th     | `sha256:a20b61c855bf12db1d39f2ab7ef8ddf55e46f96146e8c177e4fbff1fac313521` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `6-dev` `6.5-dev` `6.5.0-dev`              | May 14th     | `sha256:adc5887ab92cb1a69ceacb7c85902bf75a3e78190062824f63c3026c7296242e` |
|  `6.5.0` `6.5` `6`                          | May 14th     | `sha256:6474f4e651651318febe6ecd2ae21cf9cdf6e269a944e0fcefcc3a5ca3ea7f03` |
|  `5` `5.4.1` `5.4`                          | May 14th     | `sha256:cd0d380961f11dcad8ca3c71c5064862f945e562827079d30c2004ee64b927a3` |
|  `7.1.2` `7` `latest` `7.1`                 | May 14th     | `sha256:299f65316b0d827752fcbfea3fb44bc930f01ad49dd5e3a72d778895fcdb0a23` |
|  `5-dev` `5.4-dev` `5.4.1-dev`              | May 14th     | `sha256:9c32eaa46509f1eadf9ff67946ee1dee64a2b60535f198793f7268a0fca5443e` |
|  `7.1.2-dev` `7.1-dev` `7-dev` `latest-dev` | May 14th     | `sha256:a466a6b1401022e4787384765c224dd1cb2b8471926c9bb919d77c342c458a80` |
|  `7.1.1`                                    | May 9th      | `sha256:14417579783d4513144a3ed611a6b3dbb2c5cc51453ad7c11cf3cdb595d737b2` |
|  `7.1.1-dev`                                | May 9th      | `sha256:cdd252e8dac5c1ceccfa2b49bb2279867f4c5686a559e40122327b9b37a114f7` |
|  `6.1.1`                                    | April 28th   | `sha256:e779a5ec7dfce8190755a7c683f3f8fed331ac6909ec52270d35362fba8df214` |

