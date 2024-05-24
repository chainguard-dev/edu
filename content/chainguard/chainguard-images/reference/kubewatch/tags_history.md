---
title: "kubewatch Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubewatch Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-24 00:45:45
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubewatch/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubewatch/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/kubewatch/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubewatch/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 23rd     | `sha256:d9a0ca74a520242a47e5d40724cd4572ff690eda2c54358e0ff4e0d108dbd609` |
|  `latest`     | May 23rd     | `sha256:7948c71141113d22df1d1681dd84c62e507769460e5a9864c52729503f6f51f9` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2-dev` `latest-dev` `2.6.0-dev` `2.6-dev` | May 23rd     | `sha256:7f6d6ba9410c82c57ac0e5f600ece022e4f7b018d2ce6db7ff9baaf0b01f8b75` |
|  `2.6` `2` `2.6.0` `latest`                 | May 23rd     | `sha256:4a1236c42ec13811da1faca883342d72c24b50022652202bbc1352ab4b9529d5` |
|  `2.5.0-dev` `2.5-dev`                      | April 30th   | `sha256:2b2b1ad2fcf6aa504ce03ca74c9dd7c52145617bd0acd9774d9fd495dd135e03` |
|  `2.5.0` `2.5`                              | April 24th   | `sha256:6345d0bcd6c021e082664a5bb63e255852fd318a6b8132f94407c7d3c8466425` |

