---
title: "buildkit Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the buildkit Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-23 00:43:06
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

| Tag (s)            | Last Changed | Digest                                                                    |
|--------------------|--------------|---------------------------------------------------------------------------|
|  `latest-root-dev` | June 22nd    | `sha256:be9f013cecc12e2f9ce62dc41621c2c1f918d9032042d70627c0241e77c36f49` |
|  `latest-root`     | June 20th    | `sha256:17614101afe2bf4255c8d0243e261f7d3bb34a202698398722c3f6f99f6b47ae` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `0.14.1-dev` `0.14-dev` `0-dev` | June 21st    | `sha256:ed41c8e1db032f869b3d8c55555cc9d6a10c0d4c9eb318a00476884ca2a02c9b` |
|  `latest` `0` `0.14.1` `0.14`                 | June 20th    | `sha256:5c7bbc9489a962c6771b239ade8460cd0223541bafa5e742e5bb3e9a4f37544a` |
|  `0.14.0`                                     | June 18th    | `sha256:eed3c150b0952c270106e70e29e140e77393a6491e901586231b687d05059ed9` |
|  `0.14.0-dev`                                 | June 18th    | `sha256:daeaaf11799c18d75c94ccd964948284df5551485d30873828d1ab3d58a7939b` |

