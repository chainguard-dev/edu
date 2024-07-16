---
title: "aws-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the aws-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-10 00:36:03
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/aws-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/aws-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/aws-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/aws-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | July 9th     | `sha256:4e594d0145e8759762147a175de42dac365a493646a9ce620bb0b38492942574` |
|  `latest-dev` | July 9th     | `sha256:d6be576aa14d003df20d475a6b4b1ed8b183189160a6b9838adde14fe81d066b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.32.71` `1` `latest` `1.32`                 | July 9th     | `sha256:e912be7a2c3941650b02c6d71742ff9ad51227ccf55f45b56269eed0eace4e90` |
|  `latest-dev` `1.32-dev` `1-dev` `1.32.71-dev` | July 9th     | `sha256:9f49cfb4529b04b618924419f831b1f37ed1695238563b6fbbc8d1fe7ba2f31b` |

