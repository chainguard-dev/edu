---
title: "yara Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the yara Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/yara/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/yara/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/yara/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/yara/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 3rd     | `sha256:94ba25e01ccd357d36516b6f593958e0f8d8a348f1bef6b86c0d339e2818d681` |
|  `latest`     | June 28th    | `sha256:1e754c84d6aa154f3e2aa6662dcd14e259f3bca943fffad316d3c33244863e48` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `4.5-dev` `4-dev` `4.5.1-dev` `latest-dev` | July 3rd     | `sha256:4a443dad034764e24e58ca974738fc11ce90fe79f9de3b99aa9a2a55227dbc4f` |
|  `4.5.1` `latest` `4.5` `4`                 | June 28th    | `sha256:cee1aeee9a7507d7c997debc571b9c80ee2b35535150430447990e2ee770053f` |

