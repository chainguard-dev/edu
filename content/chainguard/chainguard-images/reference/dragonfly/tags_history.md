---
title: "dragonfly Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the dragonfly Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-10 00:43:45
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
|  `latest-dev` | May 9th      | `sha256:d5e7c44eca3e64af2b4f38c4c86e2dbb2315eb2bc30ef23c5ff6beba7aa84437` |
|  `latest`     | May 9th      | `sha256:6a0eca2e8d992354b516f6218f60f49775499c74287d97e3755b90ac148b0b18` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1` `1.18` `1.18.0` `latest`                 | May 9th      | `sha256:d22cb9fac6ce3376cbe62fea0d8359ab2efa3a3348d867c32903e7fc971994b4` |
|  `1.18.0-dev` `latest-dev` `1.18-dev` `1-dev` | May 9th      | `sha256:4462bb6e557cff24ad26b449f39a4a8d073a3bbbf36d4531d855b611650ec4d3` |
|  `1.17.1` `1.17`                              | May 2nd      | `sha256:2efcb588f91b183225fdc1664e4b9df10c92ccefda954bc7536765266f154c1e` |
|  `1.17-dev` `1.17.1-dev`                      | May 2nd      | `sha256:3b433d913451ff8590ef27dd52edd977776e5ec318d0905abfd09da79bdb9b1e` |
|  `1.15.1-dev` `1.15-dev`                      | April 30th   | `sha256:73085a96dac9b4eecf03b4cda6cdd035a2946bd7bf296d3ef922b8982ad10431` |
|  `1.15` `1.15.1`                              | April 30th   | `sha256:c13eaa4e42c9658886271ab0127ef4e41002aad7c3da491912769c58bb2d992f` |

