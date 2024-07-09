---
title: "go Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the go Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/go/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/go/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/go/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/go/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | July 3rd     | `sha256:54b74a40acfc93d62bd32c72e3afe19bc55e4b2db7baa09d5950f3e5878baf28` |
|  `latest-dev` | July 3rd     | `sha256:beea702e189375a029b9e4dacfd24a6313bdc710e61153d05747f7db5332c7e3` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.21.12` `1.21`                             | July 8th     | `sha256:b710fa7ed6cb00f6f9a4680cf6fde78827f80397f316d361885993c9a97ef834` |
|  `1.21.12-dev` `1.21-dev`                     | July 8th     | `sha256:4e191e06a5dbb47b4560e338e27100a65d787b83e998cd0349523629f41ee968` |
|  `1` `1.22` `1.22.5` `latest`                 | July 8th     | `sha256:75542d085d6e2d8a9a536c59322407687e3baa0ffeb756472cef05a813cea95a` |
|  `1.22.5-dev` `latest-dev` `1.22-dev` `1-dev` | July 8th     | `sha256:0796e527722ccc76466996d801aa1269965ee77dffb360702341509941cb0a8f` |

