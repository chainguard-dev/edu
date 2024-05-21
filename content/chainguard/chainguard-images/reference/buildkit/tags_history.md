---
title: "buildkit Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the buildkit Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-21 00:38:36
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/buildkit/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/buildkit/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/buildkit/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/buildkit/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)            | Last Changed | Digest                                                                    |
|--------------------|--------------|---------------------------------------------------------------------------|
|  `latest-root-dev` | May 20th     | `sha256:541c4c8ee26b663792ecd408695ea62eb141a1934663b9a73353582b45f3c5d9` |
|  `latest-root`     | May 17th     | `sha256:6cfd6d449665eefa6aed5e8d587dfe24f978e6fe5c6fe16ebc1ab5b378443e0e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `0-dev` `0.13.2-dev` `0.13-dev` | May 19th     | `sha256:e522758db5ceaf6644e0222a82d12d3164f4f2f48e395b0bbdbca2156298185d` |
|  `latest` `0.13.2` `0` `0.13`                 | May 17th     | `sha256:528297c6da817a05e2659606601f05300167defd9ae4a2565d90b32adaa33661` |
|  `0.13.1`                                     | April 25th   | `sha256:54d7ef9f620df47c729766de5bdd8cf35a346c745369fedbe2f0a14c934ca238` |
|  `0.13.1-dev`                                 | April 25th   | `sha256:1d339d3636ee6b86c3d7a70f5ed6896b974f26e50858cca844b2ae5c962a7597` |

