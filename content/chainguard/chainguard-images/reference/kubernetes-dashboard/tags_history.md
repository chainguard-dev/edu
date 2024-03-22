---
title: "kubernetes-dashboard Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubernetes-dashboard Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-22 00:34:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubernetes-dashboard/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubernetes-dashboard/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/kubernetes-dashboard/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubernetes-dashboard/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | March 18th   | `sha256:faac2847c0bbcf8d55b7fe8de8c3660ee8546fec1094ff81e31997a355d2dafa` |
|  `latest-dev` | March 18th   | `sha256:5d8c64632afafefd30491d3c9e3847f6c1f7975d9c8513463606a7fb4ecb4d56` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `1` `1.0.9` `1.0`                 | March 22nd   | `sha256:3330b98ed8be3ff07ce0419f27cdf10a6384ecf9a1c3478fffe57111393adeed` |
|  `latest-dev` `1.0.9-dev` `1.0-dev` `1-dev` | March 22nd   | `sha256:6461b61023b5e1a14d5681d403a5e3389c9b9bb0d51fe8145caf603abbf81d79` |
|  `2` `2.7.0` `2.7`                          | March 18th   | `sha256:29d67137b4baaefb3740dfd5978dd429ea6e46d5cfdf7b6f1e8541df3f0c065e` |
|  `2-dev` `2.7-dev` `2.7.0-dev`              | March 18th   | `sha256:aac025dacdac00fa62e6ff819da6e849b28d8a0e0dae84a7ff6de661cf8687c2` |

