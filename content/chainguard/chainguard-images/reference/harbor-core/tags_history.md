---
title: "harbor-core Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the harbor-core Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-19 00:39:27
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/harbor-core/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/harbor-core/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/harbor-core/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/harbor-core/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 11th   | `sha256:d5733428a7c613be0c06c705cf99d74a1ce424b8b691cfe1788be452de3748dd` |
|  `latest`     | April 10th   | `sha256:ad1393182c78b5f9284687b77b33f734820e18aa69316ef108e8066243336ba5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.9` `2.9.4`                                | April 18th   | `sha256:a56bcc18505ebc1ba64bc5cbb6e6267c2a926e53ad7aa8049798812ef5ec99c2` |
|  `2.10.2` `2.10` `2` `latest`                 | April 18th   | `sha256:e42dda9466fca9e76ed1499a2dedf15132ab64492dfd5ea2858cce4837175b41` |
|  `2.10-dev` `2.10.2-dev` `2-dev` `latest-dev` | April 18th   | `sha256:0aa81f29eb34fa8935b0380c3328ede453254d4837f3d247442ac627d89fea3a` |
|  `2.9-dev` `2.9.4-dev`                        | April 18th   | `sha256:667ad7c97e0e8decabe48303852efe86880f5a4a9f9d874dcb70f50f09f920c4` |
|  `2.8.5-dev` `2.8-dev`                        | April 18th   | `sha256:91efd85cf3507b005d9e761ee0a727aad8ecbce182263928afd6778f71b2ae58` |
|  `2.8` `2.8.5`                                | April 18th   | `sha256:68d454500f2db9faae0a102e86447cb2951f7ffa757c49bac9c9a143ff2dddc7` |

