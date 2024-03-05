---
title: "boring-registry Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the boring-registry Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-05 17:06:05
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/boring-registry/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/boring-registry/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/boring-registry/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/boring-registry/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 1st     | `sha256:d0020a21bff6cc9a750dd08bec2009c6ba56a03aff361ab17284d25f486e699f` |
|  `latest`     | February 27th | `sha256:d5929fdf72532b63b26b599a2aeba30093aa398aaa3ebb824e161212cab38b51` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.13.2-dev` `0.13-dev` `latest-dev` `0-dev` | March 2nd    | `sha256:666a729876711d6ed08a33eb81861778be88837ee2210a763d78ca69bc9ead47` |
|  `0` `0.13.2` `0.13` `latest`                 | March 1st    | `sha256:80496b90b33e2c798e0abb77724c1a056209d3d766638760d17c8850f2fae239` |

