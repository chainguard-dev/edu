---
title: "helm Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the helm Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-19 00:54:00
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
|  `latest`     | March 18th   | `sha256:5a95b2c87f99d85047bcbbe3d4aff48a66a36c0fdcac1cd01d6cb405650a899c` |
|  `latest-dev` | March 18th   | `sha256:291e6ea31cc586eda9570eb0001381bd79ae4ec3ca0e076050d4bba2324f14b5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.14` `latest` `3.14.3` `3`                 | March 18th   | `sha256:0d64bbfabfc93d48a06d2cda2e4e02fd2d9a35d4bdd0267de385860aff807734` |
|  `3-dev` `latest-dev` `3.14-dev` `3.14.3-dev` | March 18th   | `sha256:08a261de1e09071e1770a261946fa653a287b0c8cf7dd1768c96eb6863348730` |
|  `3.14.2-dev`                                 | March 12th   | `sha256:bf5622787e582b6d786ba9d0e9892ef34c60cc56ff7ce9c12e771a9519049e95` |
|  `3.14.2`                                     | March 8th    | `sha256:6be617c0521ef1cd7b08dac99818f3f950bf9034fdfd567d600e402502a7d8c7` |

