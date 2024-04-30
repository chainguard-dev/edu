---
title: "harbor-core Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the harbor-core Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-30 00:52:22
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/harbor-core/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/harbor-core/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/harbor-core/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/harbor-core/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | April 29th   | `sha256:3a814a86291f75b71f03c22e457dca2b9ddf8e92176ac2622864267f791c333f` |
|  `latest-dev` | April 29th   | `sha256:93a65cc31f22fb1d3b8faf6d6d5a2c5da4d92896dc9c39e1a51e92adccf1f4ff` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                       | Last Changed | Digest                                                                    |
|-------------------------------|--------------|---------------------------------------------------------------------------|
|  `2-dev` `2.10.2-dev`         | April 29th   | `sha256:c5c7a8031974629d63794fc14798afcd2b384eba57b0bfbd7289d39e4e5c9f2a` |
|  `2.10-dev` `latest-dev`      | April 29th   | `sha256:383c319e01c6f5eca1ea3fd0703affb8e81cd411b566d53ac0f90e031b61aa53` |
|  `2.8-dev` `2.8.6-dev`        | April 29th   | `sha256:ffde7a4169f49808ea525442cc260bd8b4198f0d1b7744f3632d083495286f6a` |
|  `2.9-dev` `2.9.4-dev`        | April 29th   | `sha256:c5d8bb299adeeb0df6abc842e97bff23f0c9a955b97bda650d86d418b478b11b` |
|  `2.8` `2.8.6`                | April 29th   | `sha256:aaf0496273d7da493c60876b8afbac0a7e64103fd47d4f7b4d1e940516cc7a4d` |
|  `2.9` `2.9.4`                | April 29th   | `sha256:6556993658aa5b282bebf07a04d2200d29968506eaf3172dca84b1549a99dbf2` |
|  `2` `2.10.2` `2.10` `latest` | April 21st   | `sha256:09e96b3d77e31350565636a50a2e27c6816dc95607fe204279f6503926fc01c5` |
|  `2.8.5`                      | April 21st   | `sha256:0658ade46bdeda39ef4c73cb1b482e12054bec8d9d92b308519d94e65f7e376b` |
|  `2.8.5-dev`                  | April 21st   | `sha256:dc04549f03607e7f9ce712f17398058a98f1a19092042f922830d1190f976229` |

