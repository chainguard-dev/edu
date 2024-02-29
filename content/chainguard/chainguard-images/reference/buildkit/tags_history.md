---
title: "buildkit Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the buildkit Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-02-29 16:25:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/buildkit/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/buildkit/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/buildkit/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/buildkit/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)            | Last Changed  | Digest                                                                    |
|--------------------|---------------|---------------------------------------------------------------------------|
|  `latest-root`     | February 27th | `sha256:67573ef65117ca64ee9eb8569efa27bb233fab9b57cc9e2d0f34f1fdb8dc9548` |
|  `latest-root-dev` | February 27th | `sha256:4ec79560c36151cbf5e0bcbf966ca1534c7f7d7d3a7a46128d93689d63739fe2` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **[Production Images](https://www.chainguard.dev/chainguard-images)**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)            | Last Changed  | Digest                                                                    |
|--------------------|---------------|---------------------------------------------------------------------------|
|  `latest-root-dev` | February 15th | `sha256:fbdaabead056fc1bff769880be0f207ec52f27a465cf8f22ecc8f39af6651241` |
|  `latest-root`     | February 7th  | `sha256:d85d6775bcfa58d9b36bb6cd38f797621a5dbf3bb9bd0a43c260256d8ebabe86` |

