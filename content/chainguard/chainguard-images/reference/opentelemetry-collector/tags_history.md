---
title: "opentelemetry-collector Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the opentelemetry-collector Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-01 00:50:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/opentelemetry-collector/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 31st     | `sha256:ff911fd357ee3df7917d46ab317660a23a83b2114874a3f72516434efb058e67` |
|  `latest`     | May 31st     | `sha256:22456c4d2694b043638d367310b81c77e57d3374b151ff1494a56e06c58c8d6d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                         | Last Changed | Digest                                                                    |
|---------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.101.0-dev` `latest-dev`     | June 1st     | `sha256:f1aef7c8b1d8b0a2addd2e5f060942e21f03fdc6fefc4ecd2fc39ec3611be6a0` |
|  `0.101.0` `latest` `0` `0.101` | May 30th     | `sha256:53282399aa71508aa1b6b5b28f75fc8ab540f2c0a95d0f5a6a410b0dd0c16c2b` |
|  `0-dev` `0.101-dev`            | May 30th     | `sha256:7f6fe2b9fe50f6a6849362f141319dc66ec96824aef551a02a60e76a389244d2` |
|  `0.100-dev` `0.100.0-dev`      | May 19th     | `sha256:62e7da8d25d5746dd92d883ce3a61a3a37037cb296e57e6bb5af447fb76a0b50` |
|  `0.100` `0.100.0`              | May 17th     | `sha256:5a965a8cc362879883a514a4fc84c31b59a88ffbbc110c17d054c87c8a404566` |
|  `0.99.0-dev` `0.99-dev`        | May 2nd      | `sha256:426134a7a289f9afe3b728103cacdb83437bb707653aada28f57fe1248380c7a` |
|  `0.99` `0.99.0`                | May 2nd      | `sha256:fd4edcdf64de8cfda943de5887d3a77d78c9fb9eeabceb281e38b693064dffbc` |

