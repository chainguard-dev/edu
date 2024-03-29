---
title: "k3s Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the k3s Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-28 00:50:32
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/k3s/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/k3s/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/k3s/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/k3s/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | March 21st   | `sha256:055bf8db29bff169a5a22043f09b46a6bdfb02c42ed86b8d47dfad57fb9ad4f9` |
|  `latest-dev` | March 21st   | `sha256:b9821c1245083966c9dbdd37428bbc880dbcfee11fec0fa8a6799ada2ef543c9` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.29.2` `1.29` `latest` `1`                 | March 27th   | `sha256:6802353a8ce9d324acca6bccec57576188d3409c7368ee09dbd7da1dff406b15` |
|  `1.29-dev` `1-dev` `latest-dev` `1.29.2-dev` | March 27th   | `sha256:a32df5dfc4ffa58db6bd3f3b72540e543ed59a476840be94bf033f6448cf7ce4` |
|  `1.29.0-dev`                                 | March 2nd    | `sha256:b416758e770504a47b960f0ce1ef8909c0b4754fa1457a1b9d720b045cf971fb` |

