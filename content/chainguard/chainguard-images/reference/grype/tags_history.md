---
title: "grype Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the grype Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-08 00:38:35
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/grype/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/grype/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/grype/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/grype/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 5th    | `sha256:8a5c4bc26f16386400f9e344069e075297c05c0a7b203baf19778ab00549a696` |
|  `latest`     | April 4th    | `sha256:ba52ae3459575d5930365b27bb91ed78bfa09efa7a913ea73265f921284abd57` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.75-dev` `latest-dev` `0.75.0-dev` `0-dev` | April 5th    | `sha256:3f74e6183983613a935573a97ce7a4c288ee87df507b4e2cba330c11d826ed1b` |
|  `0` `0.75` `0.75.0` `latest`                 | April 4th    | `sha256:cf42976650078eca72070ef8f882df8dda648ff6bccaa16c13bc9946692c07a4` |
|  `0.74.7-dev` `0.74-dev`                      | April 4th    | `sha256:2b7411ab77222fc8d3e7f91543150391404b4031e9f9342477e67448ee169adb` |
|  `0.74` `0.74.7`                              | April 4th    | `sha256:dd9f631c8fe8112e1f13b3feb4137e8cfcc5b41a748985d2aaaa6e724e2d28dd` |

