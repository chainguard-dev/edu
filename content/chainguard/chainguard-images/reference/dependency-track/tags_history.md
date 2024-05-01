---
title: "dependency-track Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the dependency-track Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-01 00:46:56
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/dependency-track/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/dependency-track/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/dependency-track/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/dependency-track/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 30th   | `sha256:fb88e18a001f99c5960c0e5f81651e356e66aafb01406e0e5555b1b7c9edb02d` |
|  `latest`     | April 30th   | `sha256:cdfe3ea5df89d1174eefc4e0cb99c2380a6a4715cc074ef7db9d47c87b6f4cea` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `4.10-dev` `4-dev` `4.10.1-dev` `latest-dev` | April 30th   | `sha256:13539cd71382e51d2e1fe9e3e5ad944c9fcbdad3595b1c3d6be53ba89f2722c8` |
|  `4` `latest` `4.10.1` `4.10`                 | April 30th   | `sha256:c1cf8ae5f5b883ac252fe2a8291ca0ceb4535ac34e21432c9c065a096ef797f6` |

