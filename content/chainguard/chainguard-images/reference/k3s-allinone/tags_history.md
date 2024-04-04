---
title: "k3s-allinone Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the k3s-allinone Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-04 00:51:18
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/k3s-allinone/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/k3s-allinone/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/k3s-allinone/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/k3s-allinone/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 2nd    | `sha256:08e2e6c27ca7b29d53fe5809b23d2062caeaaae2c1d81e8d45e496167b9fd612` |
|  `latest`     | March 31st   | `sha256:0d909a6301d934caac897b8a0e027dc29a2a3c0d386132df2b23111423e68d74` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `1` `1.29.3` `1.29`                 | April 4th    | `sha256:507e89a0afc93b14db007c035c1c8e7ebdcc6979c7c3c4b6c8da17adab2864e5` |
|  `1-dev` `1.29.3-dev` `1.29-dev` `latest-dev` | April 4th    | `sha256:2a26f68da2ebc985abb5919947d84b5f16480efc6b4147509b90e22d08544ee0` |
|  `1.29.2`                                     | March 27th   | `sha256:6dab03d00a63cd4ba84a56502ae96f9dfa9743c5138aa3ed376fb996e7ac9d41` |
|  `1.29.2-dev`                                 | March 27th   | `sha256:3169600dc6e6346fffa697c1fdd9623e861b1da0f75324a976584ba2cd9a8b36` |

