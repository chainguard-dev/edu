---
title: "minio Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the minio Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-10 00:50:47
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/minio/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/minio/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/minio/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/minio/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 9th     | `sha256:5fe88ae36b899a0000a19bf3e77771b7f09a2a7bcee7f08945eee9c6d92b5905` |
|  `latest`     | June 7th     | `sha256:37e3291add425426995bc1c4c5c2e614c2a1702d805f1ecf08546bb8805d4f77` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)               | Last Changed | Digest                                                                    |
|-----------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `0-dev` | June 8th     | `sha256:3053e83ca387f5b9385dd36d003d178ee23808e2653edd3966d650c9a041323a` |
|  `0` `latest`         | June 7th     | `sha256:7332ef406088db5ad35837979e886e912673f7811f47854bd9ad659da494dfb6` |

