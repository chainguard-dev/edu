---
title: "boring-registry Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the boring-registry Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-01 00:50:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/boring-registry/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/boring-registry/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/boring-registry/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/boring-registry/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 31st     | `sha256:464699b12f06c3637d12f92d2ab8f8c8f6efc37748d95e3f5a03525959cf1998` |
|  `latest`     | May 23rd     | `sha256:962d9c4d91642e81b13f6fb51ad78ffd742e9626d3f2f3f83a50bebf66f9ca54` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `latest-dev` `0.14-dev` `0.14.0-dev` | June 1st     | `sha256:cf1424906238944f6ba30343a693c5a98280088934c9d2f1aca8503c51ade9fa` |
|  `latest` `0.14.0` `0` `0.14`                 | May 23rd     | `sha256:712b8e20d468f2978e9887f7e98ab3dd08083c3c472bff0451edc73056187f76` |

