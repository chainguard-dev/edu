---
title: "vault Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vault Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-26 00:35:03
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/vault/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/vault/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/vault/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/vault/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 24th    | `sha256:1cf8f49b58303f008cc9c201da50f460d5ab11ba41e5b1d40862bd993f80fe53` |
|  `latest`     | June 21st    | `sha256:f3bc598b1e1428471861d75269e3e5058634d798adfca1088001fc6612ba5183` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16-dev` `1.16.3-dev` `latest-dev` `1-dev` | June 25th    | `sha256:2b624a23c5c9608aa267f4e89bf1560769e0ebdb7a73293387de3bca47d4d91b` |
|  `latest` `1` `1.16` `1.16.3`                 | June 25th    | `sha256:913f54c94230a027e454601e3cd9befb61d34d5941ead77710b87593b6007d08` |
|  `1.15` `1.15.9`                              | June 25th    | `sha256:f71113d2e3c94cdf3a278cccf296387ddea9d933be57f71a77dd61c774a96079` |
|  `1.15-dev` `1.15.9-dev`                      | June 25th    | `sha256:0c689f41beccc5416ef4f08ecb025010960e7de62503071b86941fa861c51b89` |
|  `1.15.8-dev`                                 | June 21st    | `sha256:2aa0772ef8f77ee9cd5c96e55674b1be3aad54752f56e51c8dd6844cf83a4161` |
|  `1.15.8`                                     | June 21st    | `sha256:b803e534c5a02cdd9827b3e8ddb59c5d98f18e73442a8c9e2b5c58ddf8e07d71` |

