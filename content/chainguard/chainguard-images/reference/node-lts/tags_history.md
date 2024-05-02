---
title: "node-lts Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node-lts Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/node-lts/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/node-lts/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/node-lts/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/node-lts/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                  | Last Changed | Digest                                                                    |
|--------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `next-dev` | May 1st      | `sha256:3847fdc589f1385defecf86a73294bf4ff92e0616bef00851631e6979bc1c226` |
|  `next`                  | May 1st      | `sha256:b032dd93aab1dfabdc2a40feee7049e83bb2d51fe7a7d2fff73a822ff733f0f1` |
|  `latest`                | May 1st      | `sha256:564a1aa42bafd79289cb6e9b11f6111c5d1d6361d7c8e8814d229ee91623df03` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                     | Last Changed | Digest                                                                    |
|-------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `next-dev` `20-dev` `20.12.2-dev` `20.12-dev` `latest-dev` | May 1st      | `sha256:a24271dc8d0fd4ccd739da448bd0a71af2251d70c76c4bf0b42bb91ae33651d4` |
|  `latest` `20` `20.12.2` `20.12`                            | May 1st      | `sha256:7a5c3ac307923ff503e651e4632b765e963a3f97b1107e7a63c81586281c3636` |
|  `next`                                                     | May 1st      | `sha256:8e6348bcc46fdaf77cf212472512ce8c9b722db8f4e396ffb911d6038dd18c6a` |
|  `20.12.1-dev`                                              | April 9th    | `sha256:d289a7c7a304ddbed4b56ad9d455d5927e43fdb587c451e75bd652ee876feed2` |
|  `20.12.1`                                                  | April 9th    | `sha256:7d95ea2daa4623b270d640e2a7e9f7aeb353993313b277bd44f29a67bce1655f` |
|  `20.12.0-dev`                                              | April 3rd    | `sha256:83afbbb59e0c66fe10e503df0da53673df4724b013dcf10bdc996d6898a8608c` |
|  `20.12.0`                                                  | April 3rd    | `sha256:0f9217ed827198cbb8c09503e28fb93acbe24a2f1af31c45e5cdcb31fe0f5347` |

