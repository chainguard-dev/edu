---
title: "buildkit Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the buildkit Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
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
|  `latest-root`     | July 8th     | `sha256:eb1ed579773ff26117e303f8480fde5f988b7683729ba8f0fed72de88b7f802c` |
|  `latest-root-dev` | July 8th     | `sha256:e7fa7857ad8b016db7b83f9bf2aa022fdfaba7129d3c934e92003ae5350b0da0` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.14-dev` `0-dev` `0.14.1-dev` `latest-dev` | July 8th     | `sha256:d3fe43915f1a1e7be42c7bc09863cc6d9bb39af0f20456a95a3c1ac2416a5fb7` |
|  `0` `0.14.1` `0.14` `latest`                 | July 8th     | `sha256:03c144805b64d9cb5ae83f05d93092a2095e020da627d0ad31775539d2f40dda` |

