---
title: "az Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the az Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/az/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/az/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/az/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/az/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | April 9th    | `sha256:d4f63ec550409b4b68675d745eaad51e5481710150e1edbeec4e1c97d78a91d4` |
|  `latest-dev` | April 9th    | `sha256:3ed55d2a43f1f7318bc1ccd89a4a2d368aeb9ac1d1b57663150989fede6c1225` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2-dev` `2.59.0-dev` `latest-dev` `2.59-dev` | April 9th    | `sha256:90a0e99e72d7a366b3f7581f8f32fe3106a70b42ee546adda0293824c729dcfe` |
|  `latest` `2.59` `2.59.0` `2`                 | April 9th    | `sha256:b7447462df7ff2bd115ef1af2b816783e6ba5171fcb5c807503c30f7b348cf1c` |
|  `2.58.0` `2.58`                              | March 29th   | `sha256:734813223228612022acbdaff720f02863b1d55b8fe5f711edfe5534d9496568` |
|  `2.58.0-dev` `2.58-dev`                      | March 29th   | `sha256:6c09869e1638043d06effba12ef736ade8f6c546f4ceaf794e4a0fd303a02350` |

