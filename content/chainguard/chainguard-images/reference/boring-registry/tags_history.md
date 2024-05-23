---
title: "boring-registry Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the boring-registry Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-23 00:45:07
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
|  `latest-dev` | May 22nd     | `sha256:d6e701eed85a0edc4d3b3f097323af6a69c92e94eafb61b0fc30bb816150670d` |
|  `latest`     | May 21st     | `sha256:f18728bddd6785babf59b5057ddd14f3e62053ffe8a013745fe965e5f7f9e3b3` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.14.0-dev` `latest-dev` `0.14-dev` `0-dev` | May 22nd     | `sha256:6d0ff5b235fd22fce5b90724193d45f4ad9f3db59fc2e3fc203333b5bf5224c2` |
|  `0` `latest` `0.14` `0.14.0`                 | May 21st     | `sha256:70d1e5f1b46e5877dd9304bca8606b61cb55916c7c106d84b83cec94a470465e` |

