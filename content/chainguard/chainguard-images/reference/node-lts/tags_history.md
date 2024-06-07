---
title: "node-lts Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node-lts Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-07 00:46:50
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
|  `latest-dev` `next-dev` | June 6th     | `sha256:83c35cff7d42c49795bc1cc13e7023accc59fded05da5ccb09e367ff0f9c8bc2` |
|  `latest`                | June 6th     | `sha256:5bcab869041e81dbd3864046ad7a0c230fb3cc505bd8a960f2c288534e40a14f` |
|  `next`                  | June 6th     | `sha256:f9e599068dd2d009269433eabbdcdf21dcf530aea8140f01ce46cc29c3675d23` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                     | Last Changed | Digest                                                                    |
|-------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `20.14` `20` `20.14.0` `latest`                            | June 6th     | `sha256:4b1416dd8702326c552904d217a13741b7c29f19da5154285dbfe2a9b54c12be` |
|  `next-dev` `20.14.0-dev` `20-dev` `latest-dev` `20.14-dev` | June 6th     | `sha256:a8aa6dff820ffb0d75b73d20b05e50743bad15b9810b08b91e2cbc0d4de0ad06` |
|  `next`                                                     | June 6th     | `sha256:cd152bee975f95a9404013be8084a361b65c2320b8950e2e06e8d91265acd69d` |

