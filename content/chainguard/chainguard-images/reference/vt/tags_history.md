---
title: "vt Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vt Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-23 00:45:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/vt/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/vt/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/vt/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/vt/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 22nd     | `sha256:784ba5e20575a4c8aca57a8199eb9d46597b69d54f3766dda6205c4cbf3ad98b` |
|  `latest`     | May 21st     | `sha256:ddce8558799ea0abe40ff40cad5fa0e7565587b24c8c5d9f20cb5f053a30985f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1-dev` `latest-dev` `1.0.0-dev` `1.0-dev` | May 22nd     | `sha256:1445302fa5a29f6743481c3e70fdfcf5191a5fae6baf9c5bd27027a02a2a7033` |
|  `1.0.0` `latest` `1` `1.0`                 | May 21st     | `sha256:77e3a647d114b6365c451a8f2fd362a7199b6ae2a77cc93e799b39ed4c8c4819` |

