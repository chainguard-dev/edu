---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-01 00:36:20
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
|  `latest`     | June 29th    | `sha256:e8d32d9fb14b6665f3e6d611a504e11019f1ecab10ca6d306b0b549f73f60820` |
|  `latest-dev` | June 29th    | `sha256:108e364d4a4aa615b54ec20af1ef90d552292a179b28a4603e9b128078981842` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `6` `6.5.0` `6.5`                          | June 28th    | `sha256:c15723f7370db2cb8d4336122d00ed307caad8ae4369e1f6868c691108d356fb` |
|  `7.2` `latest` `7.2.1` `7`                 | June 28th    | `sha256:55431f03624b898c441f9b15d126f040cccf1f8309295cfb9e9965b9838b2028` |
|  `5.4.1-dev` `5.4-dev` `5-dev`              | June 28th    | `sha256:772f0027c6da6ea8b96f7cc3519f42a88ceb282a758a1f7efcc7ab3d7b9f8be9` |
|  `7-dev` `7.2-dev` `latest-dev` `7.2.1-dev` | June 28th    | `sha256:572b59ff261ac7cbf7eb8d83a4f50c1297ece603c14ab0868c9afba3b505d96c` |
|  `5` `5.4` `5.4.1`                          | June 28th    | `sha256:a0f4cc2cc84f8133cab9265d4363f697bb901510246c678cc63cf793d5db0052` |
|  `6.5.0-dev` `6.5-dev` `6-dev`              | June 28th    | `sha256:85495af73f59cd93e825e30cb1e484cd71bf2d9cff71cb223b2c40a56b0edcfe` |
|  `7.2.0`                                    | June 24th    | `sha256:f0608a7e45f91e7391a83575a0f8143a0da10e80aa8cccc1dcd385bc70410dac` |
|  `7.2.0-dev`                                | June 24th    | `sha256:4a2ccc4f894f2c6d7b3bb3556969292b1ea26a0d57efbe7ad2fe65057e49b965` |

