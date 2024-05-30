---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-30 00:47:59
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
|  `latest-dev` `7.1.2-dev` `7.1-dev` `7-dev` | May 29th     | `sha256:05a5940fab37318320caf31ac22c9ea9097a430b5628864498209509a8b3f247` |
|  `7.1.2` `latest` `7` `7.1`                 | May 29th     | `sha256:3f4413a7ac2aa02d90428e08810e9bc64da63889abdd1d85f71884a2b941cee1` |
|  `5` `5.4.1` `5.4`                          | May 29th     | `sha256:73a3491016438c38d30f008ba3ad35afda9b36eae5814de697bee7c935453ee3` |
|  `6.5.0-dev` `6-dev` `6.5-dev`              | May 29th     | `sha256:0e9fc91e4e21cf09fa8f51c4b758a5a44495ea23ed18fafe9ec27f0eff3da9e6` |
|  `6.5` `6` `6.5.0`                          | May 29th     | `sha256:714cbba8e9cb22ab4899de34f981c48b5cf74f48a7fc320d526e5bc8514e8cd4` |
|  `5.4.1-dev` `5-dev` `5.4-dev`              | May 29th     | `sha256:8b823f31f8fe7a7d8a211aaf37876b6ab764e32522650e99a90538e284fd80c0` |
|  `7.1.1`                                    | May 9th      | `sha256:14417579783d4513144a3ed611a6b3dbb2c5cc51453ad7c11cf3cdb595d737b2` |
|  `7.1.1-dev`                                | May 9th      | `sha256:cdd252e8dac5c1ceccfa2b49bb2279867f4c5686a559e40122327b9b37a114f7` |
|  `6.1.2` `6.1`                              | May 22nd     | `sha256:eed2d4f320442b1498ee44dc54efd331844d9e2c7ec1a2ff0458bd2762172d0c` |

