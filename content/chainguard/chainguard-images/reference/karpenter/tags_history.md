---
title: "karpenter Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the karpenter Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-06 00:48:16
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/karpenter/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/karpenter/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/karpenter/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/karpenter/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 5th     | `sha256:0f3473185b1d4c3d00a7e15e4d65b89b07066088a6313b2f236b0ac801d6eed7` |
|  `latest`     | June 5th     | `sha256:19c10a4c18ac7c8c64cdd3e4efc88f5ad03adfefc6454d7d26ed4b6ae8b57e4a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.35-dev` `0.35.5-dev`                      | June 5th     | `sha256:352a70607e172062ecc696da42b595d7a73c2d2745dececaeed3d4d20578279f` |
|  `0.35` `0.35.5`                              | June 5th     | `sha256:13ccfd6ac8cd4d3016b4b0e0cb865ae93874637e28654dcf14fe7b7124561a08` |
|  `0.37-dev` `0-dev` `latest-dev` `0.37.0-dev` | June 5th     | `sha256:db294acfbdd629ed109a3b8070c04007fbfb47caf16f1c239761c169a8d6d6dd` |
|  `0.37.0` `0.37` `0` `latest`                 | June 5th     | `sha256:1537effb64da80fd3eadb0c93576367ff84e271a6c047f30d5c4d39e075f709a` |

