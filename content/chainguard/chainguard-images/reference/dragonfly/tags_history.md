---
title: "dragonfly Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the dragonfly Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-22 00:47:17
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/dragonfly/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/dragonfly/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/dragonfly/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/dragonfly/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 21st     | `sha256:1f6701e42fd89e246f424ea9f79dac985a816d902e9b863a1cb81f2a131e17d6` |
|  `latest-dev` | May 21st     | `sha256:e551c051e473f52f42a4e6c84ab48d46ff445ec114532b8e4a1b8b30d04f9d79` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `1.18` `1.18.1` `1`                 | May 21st     | `sha256:8757199c6a195d52c6833643fb3c141c410b602c40d73ddcebeb53e3cca9d74e` |
|  `1.18.1-dev` `latest-dev` `1.18-dev` `1-dev` | May 21st     | `sha256:4d1165d92fa532f138c2e205ee8503aeab9b39b499d92b1b713a83c878261520` |
|  `1.18.0-dev`                                 | May 16th     | `sha256:fc5dcfd9d45aa14c01e7e9bc88ac63e0ab6131d4bd3b3c7af7e1e3367ed6b259` |
|  `1.18.0`                                     | May 15th     | `sha256:b4d94620a7d2c4d3765846d627c0807ec80dcf95c274915f4b827561bc3b6d91` |
|  `1.17.1` `1.17`                              | May 2nd      | `sha256:2efcb588f91b183225fdc1664e4b9df10c92ccefda954bc7536765266f154c1e` |
|  `1.17-dev` `1.17.1-dev`                      | May 2nd      | `sha256:3b433d913451ff8590ef27dd52edd977776e5ec318d0905abfd09da79bdb9b1e` |
|  `1.15.1-dev` `1.15-dev`                      | April 30th   | `sha256:73085a96dac9b4eecf03b4cda6cdd035a2946bd7bf296d3ef922b8982ad10431` |
|  `1.15` `1.15.1`                              | April 30th   | `sha256:c13eaa4e42c9658886271ab0127ef4e41002aad7c3da491912769c58bb2d992f` |

