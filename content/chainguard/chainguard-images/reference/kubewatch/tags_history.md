---
title: "kubewatch Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubewatch Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-30 00:52:22
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
|  `latest-dev` | April 29th   | `sha256:e822717b6303cdfb685d6a6601195e547d2692bbdbd91cbf80944902dad1d4d6` |
|  `latest`     | April 24th   | `sha256:0b5e191bb38165bb18ca8fded779a0baa6a0ebfeee7b61c7db98c59712cb5547` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.5-dev` `2-dev` `latest-dev` `2.5.0-dev` | April 29th   | `sha256:b31ae3c9fd5235766e84dcb86f217880c6e4532f62623a6b21e1ba4ba6ad84fc` |
|  `2.5.0` `2.5` `2` `latest`                 | April 24th   | `sha256:6345d0bcd6c021e082664a5bb63e255852fd318a6b8132f94407c7d3c8466425` |

