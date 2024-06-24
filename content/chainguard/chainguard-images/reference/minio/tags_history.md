---
title: "minio Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the minio Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-24 00:43:49
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
|  `latest`     | June 23rd    | `sha256:da401e751ee505b192dddf1a26cd7371800efdb846f9816fd6c65257d7f8ee95` |
|  `latest-dev` | June 23rd    | `sha256:2e0ec7f6ad54d482fb2ceb07d532a77f98817fb6fb20b668a53eee662012b775` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)               | Last Changed | Digest                                                                    |
|-----------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `latest-dev` | June 23rd    | `sha256:adbad8e405fa0d0b7eddc13330a0b534cec46c73840834883b277d553f13f036` |
|  `latest` `0`         | June 22nd    | `sha256:9827f4937fcb976d3da7629514561de7a1475e2360c18fc9f3e6a206e45c39c3` |

