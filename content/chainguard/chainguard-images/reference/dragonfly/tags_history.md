---
title: "dragonfly Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the dragonfly Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
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
|  `latest-dev` | July 3rd     | `sha256:81c66e43b94d323755c36f2d5e3638001117475106e7a659147e1a01eee8ff5d` |
|  `latest`     | July 3rd     | `sha256:3033d6f8be1915813a73618ccbfb5851a0e15fd8ac59477a99a8dc02096ece32` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.19.2-dev` `latest-dev` `1-dev` `1.19-dev` | July 3rd     | `sha256:af0af66429cb1ca7b58a1ba56ebe384d32f74c4fb97e31014c83ee140a58a919` |
|  `1.19.2` `1.19` `latest` `1`                 | July 3rd     | `sha256:c7e1bd987025f8df9e240cd4652193a6d053b1460f37bf82453345ae7db79c60` |
|  `1.19.0-dev`                                 | June 28th    | `sha256:f767f372ff7ad1495986d1e56829a1433847a32447664e1d65a8aeba112fa66f` |
|  `1.19.0`                                     | June 28th    | `sha256:2ebc14eac26efc11ec386dc0310a1c005a3313710adfecd2f57c8094b8103f8a` |

