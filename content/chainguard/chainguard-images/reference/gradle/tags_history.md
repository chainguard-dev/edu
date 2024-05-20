---
title: "gradle Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gradle Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-20 00:48:18
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gradle/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gradle/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/gradle/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gradle/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)   | Last Changed | Digest                                                                    |
|-----------|--------------|---------------------------------------------------------------------------|
|  `latest` | May 17th     | `sha256:40941d798065f111b2b58c408dfff72da0200ee83c832c0803a1aeaee285f3f7` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-17-dev` `openjdk-17-8-dev` `openjdk-17-8.7-dev` `openjdk-17-8.7.0-dev`              | May 19th     | `sha256:6131261f5513755e9a4005be7803a1efa98c4b9b51b85edb6e7f0e2f16a54ef4` |
|  `openjdk-21-8.7-dev` `latest-dev` `openjdk-21-dev` `openjdk-21-8.7.0-dev` `openjdk-21-8-dev` | May 19th     | `sha256:704653e5d174faa398ec303d58ab3bcd3225b96124e491f6cfba87b3cff2831c` |
|  `openjdk-21` `latest` `openjdk-21-8.7` `openjdk-21-8.7.0` `openjdk-21-8`                     | May 17th     | `sha256:6ae952cb6bf577b4f424dda7bfcf90ddf6f39a1c4e1c46a62faaac8f08848231` |
|  `openjdk-17` `openjdk-17-8.7.0` `openjdk-17-8.7` `openjdk-17-8`                              | May 17th     | `sha256:b533658d5902c0e06e9b4678d69edc56ceefa801eba6a03dff30125c5f5dcd41` |
|  `8.0.2` `8.0`                                                                                | April 27th   | `sha256:078793fd8f61815bf28eccefc651f9125f127b1221e1d353e3d6f4ee18e3f7bb` |

