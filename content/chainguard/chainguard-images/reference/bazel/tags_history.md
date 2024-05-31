---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-31 00:48:45
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
|  `6` `6.5` `6.5.0`                          | May 30th     | `sha256:4a832c7683808a35125abb508d27c500306e7d0caede9f12bbdef0104cf29afb` |
|  `6.5-dev` `6-dev` `6.5.0-dev`              | May 30th     | `sha256:526d37122b4d4e4ffd395cc41705d5fc89407942c542cc110c8b4ec0ecbfdee1` |
|  `5` `5.4` `5.4.1`                          | May 30th     | `sha256:b8df8e223483887411ef901cd434676327544043bb97b1bcb4af14c6d582627e` |
|  `7.1.2` `7` `latest` `7.1`                 | May 30th     | `sha256:030683eedcbc09f0dacfc3ddf0ce295b9441dcd94e16947a8d5ac3ef8e6c6b4d` |
|  `5.4.1-dev` `5-dev` `5.4-dev`              | May 30th     | `sha256:1bc6217193823c779da964b59bec3b2f1a07a3dfdb16a86ba7f32a0b69ba6099` |
|  `7.1-dev` `7.1.2-dev` `latest-dev` `7-dev` | May 30th     | `sha256:63c2cd247c8e71650fdb7270da72bd2eb93ecc577e2ca8e1f92e09163e1b56ce` |
|  `7.1.1`                                    | May 9th      | `sha256:14417579783d4513144a3ed611a6b3dbb2c5cc51453ad7c11cf3cdb595d737b2` |
|  `7.1.1-dev`                                | May 9th      | `sha256:cdd252e8dac5c1ceccfa2b49bb2279867f4c5686a559e40122327b9b37a114f7` |
|  `6.1.2` `6.1`                              | May 22nd     | `sha256:eed2d4f320442b1498ee44dc54efd331844d9e2c7ec1a2ff0458bd2762172d0c` |

