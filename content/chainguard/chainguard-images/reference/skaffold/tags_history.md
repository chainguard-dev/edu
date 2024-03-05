---
title: "skaffold Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the skaffold Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-05 17:06:05
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/skaffold/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/skaffold/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/skaffold/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/skaffold/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 1st    | `sha256:f8ed7c73c32450f03e6951f00889579616c73a32dd3ff06f7216f702455dd55a` |
|  `latest`     | March 1st    | `sha256:cb7b1490d0e10d260d209a13d8864b4a82c8151f1851ec2509b449d93c02e419` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.10-dev` `2.10.1-dev` `latest-dev` `2-dev` | March 2nd    | `sha256:413f1f8408cf8dee00b78b0c6c47400de2f5a97ebee1f049d69ff975baf4ff86` |
|  `latest` `2` `2.10.1` `2.10`                 | March 1st    | `sha256:2716ac9cae3baf2f06b1344010c77da477cb54a111b7034151d9b79652edfb0b` |

