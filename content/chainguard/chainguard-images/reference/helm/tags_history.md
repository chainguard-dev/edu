---
title: "helm Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the helm Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-16 00:33:13
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/helm/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/helm/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/helm/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/helm/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | March 16th   | `sha256:d59729e15527ae6d3c70b977a8630650a4abc820dee60c4f39ef3d195c78f2c5` |
|  `latest-dev` | March 15th   | `sha256:22b33f73b9eb646f285c6b198a3d262463381f0e33f6ea1f9544b31dcb3d52c8` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `3.14` `3` `3.14.3`                 | March 15th   | `sha256:302273f7a7962d1398f6eca146b772a0003d337e5a0d17033c7dfec6358bc7a0` |
|  `latest-dev` `3.14.3-dev` `3-dev` `3.14-dev` | March 15th   | `sha256:9f8e66dd577491077d19c51679cdff2f406200e1057b65118cc04e826c682992` |
|  `3.14.2-dev`                                 | March 12th   | `sha256:bf5622787e582b6d786ba9d0e9892ef34c60cc56ff7ce9c12e771a9519049e95` |
|  `3.14.2`                                     | March 8th    | `sha256:6be617c0521ef1cd7b08dac99818f3f950bf9034fdfd567d600e402502a7d8c7` |

