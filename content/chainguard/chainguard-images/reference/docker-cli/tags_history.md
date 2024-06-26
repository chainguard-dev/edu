---
title: "docker-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the docker-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-26 00:35:03
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/docker-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/docker-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/docker-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/docker-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | June 25th    | `sha256:cc13e94b8802460b35ffa72d5e9ee0a0930744fb5cc719bedf4a86452a46a6be` |
|  `latest-dev` | June 25th    | `sha256:2f56a96b7cdeb842d03a40e5d93e5758a6b4ee47e03de670a1982d2257e35826` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `27-dev` `27.0-dev` `latest-dev` `27.0.1-dev` | June 25th    | `sha256:f0a3855c8c2d589159964ae806b065d193c5c1ec3ca29c8ffa6870d75af4d2eb` |
|  `27.0.1` `27` `27.0` `latest`                 | June 25th    | `sha256:3922ea4ac68bad09f3a67bc5a3b12d7815f2c97a3e12f7a1c408fc1634638cde` |
|  `26.1.4-dev` `26-dev` `26.1-dev`              | June 23rd    | `sha256:f39d7efaa93d2b319364b1c96346e111a46e03cc1bebd335a9e8116ef0da1d44` |
|  `26.1.4` `26.1` `26`                          | June 20th    | `sha256:967fb9c9044f6d38615384688163e896525511cad05d0b49f70cd3230ee6e44f` |

