---
title: "melange Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the melange Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/melange/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/melange/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/melange/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/melange/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | July 4th     | `sha256:30a4fa513ed79f1352491582b6c85639d758f2fa0f6f59470282cf75150a8f3b` |
|  `latest-dev` | July 4th     | `sha256:1c67b496388008b6c068e31c91ec3494f08663cb43c11e5a347db402ebd26b69` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0` `latest` `0.10.1` `0.10`                 | July 3rd     | `sha256:1e06726ceadca2893db606947922f6480f0e7ed5d6813288951ff32d178db427` |
|  `latest-dev` `0.10-dev` `0-dev` `0.10.1-dev` | July 3rd     | `sha256:705aab3bb0163dbd7639ff945492f01fd15600dfe3ab0cd629e066d8c5acccae` |
|  `0.10.0-dev`                                 | July 3rd     | `sha256:cc8039e9a1fbad2356b2e8e25a863f85d9c647f42a17062ea29afda719ff67e3` |
|  `0.10.0`                                     | July 3rd     | `sha256:a8dcb6a17db05686563a3e94427e2d43d7d9920b62546837ef2393b8f96304b7` |

