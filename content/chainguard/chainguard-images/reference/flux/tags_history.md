---
title: "flux Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the flux Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-22 00:47:17
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/flux/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/flux/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/flux/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/flux/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 21st     | `sha256:3677398d7b20ff3f53fdd4d11eed1b7305c5c019e910447d2978322e8617924c` |
|  `latest-dev` | May 21st     | `sha256:f0ff07114b14f2c574333b7bf941bc2debd3ba61ba4ef8e4afa5174edff8db89` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `2` `2.3` `2.3.0`                 | May 21st     | `sha256:45922d344e0e87820d5673ee12daeda0a4ea43d5896d39960206c266b444271c` |
|  `2.3-dev` `latest-dev` `2.3.0-dev` `2-dev` | May 21st     | `sha256:5c3cd4ada7bfd6bbd83719033f979ab58f522b9b81941dd6aa3fe5fcb4dcabf3` |
|  `2.2.3` `2.2`                              | May 2nd      | `sha256:8cfe941351304bf758f74f25831dd5def0ee2616fe89f1f42d8326edb8180352` |
|  `2.2.3-dev` `2.2-dev`                      | May 2nd      | `sha256:fb040a1798a4c30e8c3abe5905f62da9f2721931d9505e4ceef40f53165488e3` |

