---
title: "dependency-track Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the dependency-track Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-27 00:43:34
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/dependency-track/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/dependency-track/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/dependency-track/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/dependency-track/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 24th     | `sha256:e87c5612c209ecb9979362b1da42fa9d44540d0d20351407552e267a45a72d25` |
|  `latest-dev` | May 24th     | `sha256:ee10030c04bb16a887c822ddf46b9b8540eb231d37b46f67503e31ca50cf2d37` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `4.11-dev` `4-dev` `latest-dev` `4.11.1-dev` | May 24th     | `sha256:cbcc34f170a14f93a1c3fb4ed5d27341d79ca5f43f86e8a4705b4cf4e8876ead` |
|  `4` `4.11.1` `latest` `4.11`                 | May 24th     | `sha256:fd461b2834cd93236f26b1773a6b8510782d41c5bece436af1499ba557eee150` |
|  `4.11.0`                                     | May 17th     | `sha256:006f45332a04ecd3c06f0eb9154c83efcb2d1d52f8a234598131d18e52385659` |
|  `4.11.0-dev`                                 | May 17th     | `sha256:1898d230cb795e6c56906d31b870992fd25ce537fdcb432eb53331a9f49ff23e` |
|  `4.10-dev` `4.10.1-dev`                      | May 2nd      | `sha256:c274b306b668e2d2a37122c866e927b6e574fdd6b669f137befae732c3d61fbb` |
|  `4.10.1` `4.10`                              | May 2nd      | `sha256:1d19779826424532fdd25332cdfa169d9909f037d015d4b606def95696e538d4` |

