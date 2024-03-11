---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-11 00:52:51
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/bazel/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/bazel/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/bazel/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/bazel/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)   | Last Changed | Digest                                                                    |
|-----------|--------------|---------------------------------------------------------------------------|
|  `latest` | March 9th    | `sha256:464db12a84e624f4e8b0bd2a9c2be1598c9dce47a4b539057d65c1fdf3199861` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `6.5-dev` `6.5.0-dev` `latest-dev` `6-dev` | March 10th   | `sha256:c37000f2b4a95e46edef2164936f839d461b6698cf61ba62d38625b45fa223d2` |
|  `5.4-dev` `5.4.1-dev` `5-dev`              | March 10th   | `sha256:ae5bfb69dfc7687d8cf8b4b7ec60cd01d032e79792ae19fa884110a2cbb755e2` |
|  `6.5` `6` `6.5.0` `latest`                 | March 9th    | `sha256:fb0905be97e909b79f1173cfb34a5e7261495e5d5d23ec83e65170998029fa3d` |
|  `5.4` `5` `5.4.1`                          | March 9th    | `sha256:069e10c11a4f4dff9a6d994b34e433455352039238471b61e479104055c0a6e0` |

