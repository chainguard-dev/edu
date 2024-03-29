---
title: "helm Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the helm Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-29 00:47:42
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
|  `latest-dev` | March 28th   | `sha256:a6f695c75ab8ec8abc7c875f4f913fe7fa0638002ad6e1d70771f2aee4643ce5` |
|  `latest`     | March 28th   | `sha256:e67b1eae84bcbc63fdde1c9b5a6ef30d010a9c07c1d6117399d9f37fe6567b38` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.14.3-dev` `latest-dev` `3-dev` `3.14-dev` | March 28th   | `sha256:2276250b6e4f5e67814ff95e57ab94077d25a0b900e038ae1a611e6e0d2f1f52` |
|  `3.14.3` `latest` `3` `3.14`                 | March 28th   | `sha256:6416350fd102cb17a81843d4af8d0455ccdf577b200e86ae5e92e30f8489d443` |
|  `3.14.2-dev`                                 | March 12th   | `sha256:bf5622787e582b6d786ba9d0e9892ef34c60cc56ff7ce9c12e771a9519049e95` |
|  `3.14.2`                                     | March 8th    | `sha256:6be617c0521ef1cd7b08dac99818f3f950bf9034fdfd567d600e402502a7d8c7` |

