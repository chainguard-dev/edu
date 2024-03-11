---
title: "cfssl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cfssl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-11 00:52:51
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
|  `latest-dev` | March 8th    | `sha256:be539ef47230f659afa48a42402c75f487a968a2bfb74e8c388a7f620dd0836e` |
|  `latest`     | March 8th    | `sha256:142101b63f64b1cac2fb22c93f63c9a7a300739a10c03e6b5a497ed54d6328e2` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `1.6-dev` `1.6.5-dev` `1-dev` | March 10th   | `sha256:3db7f53a1f44f2f7ad04a3cfa668a121a1c7e31ad986ece5977cc780c86c6db2` |
|  `latest` `1.6` `1.6.5` `1`                 | March 8th    | `sha256:afeccc4f4b38124196f333ecd050c5ce600aedccd9932afe8dc2a5210d1c705a` |
|  `1.6.4-dev`                                | March 2nd    | `sha256:6bb1365ee7004869afbf8c48665e97c7106fcf69cafa58a6c65b2bcfc1523d66` |
|  `1.6.4`                                    | March 1st    | `sha256:0f22b930283055b703dae5fa37506924b8b083ee11e6012964f184072692f9c5` |

