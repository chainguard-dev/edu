---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
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
|  `latest-dev` | July 3rd     | `sha256:cabe2a68bc6995c5c1ca6ed03c13b9451fb4961d9f19ad7e05666fdc14fe5604` |
|  `latest`     | July 3rd     | `sha256:dfe3f3f79374050773824bd1c4dfdd4928c72215bcb0567d5276c8a5535220a9` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `5.4.1-dev` `5.4-dev` `5-dev`              | July 4th     | `sha256:5dc361b741c9fc3a0e13e36f95a0f7b8a1dc4662d4676851221ae795ba003129` |
|  `7.2-dev` `latest-dev` `7.2.1-dev` `7-dev` | July 4th     | `sha256:e262a95d5e228103574ccf51970c5db172d06abd09cf44f938e7ace1d1a82c14` |
|  `5.4` `5.4.1` `5`                          | July 4th     | `sha256:14720962b010df79a2d1cb9c75b7bac16956d13a0294d7d258af422455383cba` |
|  `7.2.1` `7` `7.2` `latest`                 | July 4th     | `sha256:05de04df479b9d89812c0be3a4f3c4f5730ce11188485b22d437285e31d5a7b8` |
|  `6.5-dev` `6-dev` `6.5.0-dev`              | July 4th     | `sha256:56ccec1058af72c1e611eecdb55d27d2ce6486349cb3549f10557f7eb0a5f32c` |
|  `6.5` `6` `6.5.0`                          | July 4th     | `sha256:c9234e4d1c54e937e5af8879572a3ca298bca6670f74939038421d46747e70bf` |

