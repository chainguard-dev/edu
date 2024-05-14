---
title: "dragonfly Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the dragonfly Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-14 00:46:23
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
|  `latest`     | May 13th     | `sha256:cfda6c64e0e41e230e68eaadca1e76e0e46bb3bb6f4eb88ddd6b7e77010283ce` |
|  `latest-dev` | May 13th     | `sha256:e2276daa00c262eebf08d3290c8eb7f2a141780d052f7d8980fcb73f5d06dcd0` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1` `1.18.0` `1.18` `latest`                 | May 13th     | `sha256:acb72a1a7fca3863bffeea36a0977376909a44643b29c0cc7803f55ee6944ba0` |
|  `1.18.0-dev` `latest-dev` `1-dev` `1.18-dev` | May 13th     | `sha256:0d767209a08031d5438aa29f3e776024284371f888911ce94d2d307903322345` |
|  `1.17.1` `1.17`                              | May 2nd      | `sha256:2efcb588f91b183225fdc1664e4b9df10c92ccefda954bc7536765266f154c1e` |
|  `1.17-dev` `1.17.1-dev`                      | May 2nd      | `sha256:3b433d913451ff8590ef27dd52edd977776e5ec318d0905abfd09da79bdb9b1e` |
|  `1.15.1-dev` `1.15-dev`                      | April 30th   | `sha256:73085a96dac9b4eecf03b4cda6cdd035a2946bd7bf296d3ef922b8982ad10431` |
|  `1.15` `1.15.1`                              | April 30th   | `sha256:c13eaa4e42c9658886271ab0127ef4e41002aad7c3da491912769c58bb2d992f` |

