---
title: "jenkins Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jenkins Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-05 00:36:13
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jenkins/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jenkins/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jenkins/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jenkins/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | June 4th     | `sha256:683da9b997384dc90517f4e8fa2e7050161997f455eba0a877925009a8acd404` |
|  `latest-dev` | June 4th     | `sha256:67860f3c35b7911476dfb16a861e73c4f484b376f54fae7cdf155bed987562d1` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `2.461-dev` `2-dev` | June 4th     | `sha256:6888f4b56c5359f1e3ac2b562e99694032511707727945becb9ad25b229b0ca5` |
|  `latest` `2.461` `2`             | June 4th     | `sha256:1a3bd4931fec5707c24a1621420c8b3130317cdacc8bc8b00fb1134d5c259937` |
|  `2.460-dev`                      | June 4th     | `sha256:fc1f88b3cc5a1d62c344745ffffc3f042cfac76261be70ed698859fee0282d40` |
|  `2.460`                          | June 4th     | `sha256:3726fb8f8057d554174e0845da21bf1ed01915df7c3a569cb2733c9927d7b1d2` |
|  `2.459-dev`                      | May 30th     | `sha256:26e375b5d6fd31ba75d1e9c302144e75b4a3e1df7f4421b6785eae2f8d11c575` |
|  `2.459`                          | May 30th     | `sha256:fd907ad1e0fa7a863df75528aeca2c648fb234b3412265c8d0af7c06b08816e2` |

