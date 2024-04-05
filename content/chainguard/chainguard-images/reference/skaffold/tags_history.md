---
title: "skaffold Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the skaffold Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-05 00:47:12
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
|  `latest-dev` | April 4th    | `sha256:c5191ba04f8b5bae04581093688c81e3096b6f2fae0c99d4447961242cf53ffa` |
|  `latest`     | April 4th    | `sha256:35d7c2e94a4c90eebe1d2ad4ab2687abe2eb31fb34f99320e03a9aaca6ab309b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.11.0` `2` `latest` `2.11`                 | April 4th    | `sha256:3cab031e5917dec8e8725ff43ca5e1b26f44f745aee168f0ec71f9259c0acad8` |
|  `2-dev` `latest-dev` `2.11-dev` `2.11.0-dev` | April 4th    | `sha256:7f352def60b8ca6bf60e14556f231211135993672913fd90807fe503d4bc668e` |
|  `2.10-dev` `2.10.1-dev`                      | April 2nd    | `sha256:3c1c7adb0140d2eac476b6dcca8a5eda5cbfcc36b33f78b51764feb267328438` |
|  `2.10.1` `2.10`                              | April 1st    | `sha256:2dcb9e504cde7b7fa869b45408d14f0ac2c401df49cc5c1829bb076b71c80174` |

