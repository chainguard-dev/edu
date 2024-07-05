---
title: "gitness Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gitness Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gitness/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gitness/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/gitness/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gitness/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | June 28th    | `sha256:ec0ef27c4ba9fdd4f63aca2b819fd3e402db06a6b4b9fc28bb5cca7f0123b138` |
|  `latest-dev` | June 28th    | `sha256:da7cedee05eb3e906db9132b0f9f3d54d93d2b3d89c97b75e240b4a394983821` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                           | Last Changed | Digest                                                                    |
|---------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.0.0_beta6` `3` `3.0` `latest`                 | July 3rd     | `sha256:8f9101e3e5d9a5087a128a7e1a90565faa3669688ad2a684bab1b7f82b5b34f7` |
|  `3.0-dev` `latest-dev` `3.0.0_beta6-dev` `3-dev` | July 3rd     | `sha256:d2410f2b23ca39e781e23cebf83eca531a7f33d2cc71bedc0d986c70360c15d9` |

