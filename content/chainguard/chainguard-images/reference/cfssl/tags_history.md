---
title: "cfssl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cfssl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cfssl/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cfssl/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cfssl/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cfssl/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 1st      | `sha256:2a902cd9b27b100a2ff8d4f76bd7acfc4b65860e132bd94ac3a748d1bde98869` |
|  `latest`     | May 1st      | `sha256:26ac78428edafdd7008e80ac52dec097da97b649bd55dc2686ec2afc917bcbed` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1-dev` `1.6.5-dev` `latest-dev` `1.6-dev` | May 1st      | `sha256:44769f75b3c5ecca453a591c77d5b8565a3ca26a13adc8447d52a10c6eae9d45` |
|  `1` `1.6.5` `1.6` `latest`                 | May 1st      | `sha256:b5a4b45b7a34d9850f6077b8943ddbc0a22458dcba8e412675f6a251cdc4e8e3` |

