---
title: "openscap Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the openscap Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-01 00:36:20
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/openscap/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/openscap/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/openscap/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/openscap/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | June 28th    | `sha256:ca1fecff8426de0e40925c1e94a35baeb4e7386adf2bbf508901f0dcd1c42b97` |
|  `latest-dev` | June 28th    | `sha256:d0f738c03b644d5ed8d60fb833aa370e97f39a3ce15793b1b9763cf7b8a12470` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.3-dev` `1-dev` `latest-dev` `1.3.10-dev` | June 28th    | `sha256:059112f4be0885cd3337596f573cbe48d4ec903658337019b3b28234b33771c3` |
|  `1` `latest` `1.3.10` `1.3`                 | June 28th    | `sha256:90753c36f3f688d3f6af81e8eec19096330d62c5cbc5da78895c069d20558a66` |

