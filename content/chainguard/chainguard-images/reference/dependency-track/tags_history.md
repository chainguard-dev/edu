---
title: "dependency-track Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the dependency-track Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-03 00:33:11
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
|  `latest-dev` | June 28th    | `sha256:b5338493128f6ac54f9cf5e951be01d329d2d9d9e4465c54162dc542b3957fc1` |
|  `latest`     | June 28th    | `sha256:6e1894a23b9f82077fe4a407be68495a184130926703288333fffe4cba385179` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `4.11-dev` `latest-dev` `4-dev` `4.11.4-dev` | July 2nd     | `sha256:f2bee7f74260914294b0d0dc2b9bf59b5fc1ceca368c7aaf878f66a64d3b7a11` |
|  `4` `latest` `4.11` `4.11.4`                 | July 2nd     | `sha256:514970e4dc2aab2a5de5a938724d00a4f655de65cae4db8f80451f7c8f280c15` |

