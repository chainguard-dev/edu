---
title: "chromium Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the chromium Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-28 00:31:38
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/chromium/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/chromium/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/chromium/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/chromium/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 27th    | `sha256:14b6a8ca2c967fbd86ed2d7335a890e0fc7e44a92b66c3d0b29b5e000c3982e4` |
|  `latest`     | June 27th    | `sha256:92d59e4723b08ed87a1586e9e5566a76f2a3e2c9638fa4adac9511e8d993b980` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                   | Last Changed | Digest                                                                    |
|---------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `126.0-dev` `126.0.6478-dev` `126-dev` `126.0.6478.126-dev` `latest-dev` | June 27th    | `sha256:345712bea6d51b7747659ce22d0e03cbb9b0a9c2543d3dda5d960b1366757bcd` |
|  `126` `latest` `126.0.6478.126` `126.0.6478` `126.0`                     | June 27th    | `sha256:adcd9a9e3c2f40777857b205a0dfa19c5f604f48ef9a090d0a4ccb48c3e57fe5` |
|  `126.0.6478.114-dev`                                                     | June 25th    | `sha256:44797b2395588e067f3e3abf5bf0584c647775cac28f13091ef520f974c107bb` |
|  `126.0.6478.114`                                                         | June 24th    | `sha256:06220b773650d116efe99472959357cdbb6740200ed82b16db91091429c4156f` |

