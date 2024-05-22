---
title: "az Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the az Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-22 00:47:17
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
|  `latest-dev` | May 21st     | `sha256:59487a7e979db7b134dd3b4a038210b2ca7d5b98661a0df3a8bd016a914894c3` |
|  `latest`     | May 21st     | `sha256:1225f87ee8a5a38f6e822a8e3d0637dba279f4fb4d9c99c4ed4e6f1c12abca47` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `2` `2.61` `2.61.0`                 | May 21st     | `sha256:85a045e8d646225921c62b689d5aff1fb61d5cc7a5733633492f3029dcb4d163` |
|  `2.61-dev` `2.61.0-dev` `2-dev` `latest-dev` | May 21st     | `sha256:9dde58ea3207314b6d4dabecf03305294c65d1efdaa7b6f616d0db6b21bee9ab` |
|  `2.60.0-dev` `2.60-dev`                      | May 19th     | `sha256:ebf4af5e8c9618e08a9d8d17cfcc446250833fd4b0fb8593179302879a9fd2b9` |
|  `2.60.0` `2.60`                              | May 17th     | `sha256:15ef99e92cea2e3acfa4c18d8cfea77d74684109d3c2a41ef1899924a800ff2a` |
|  `2.59-dev` `2.59.0-dev`                      | April 29th   | `sha256:2dae57e4903bb057f1152588ee958d5d9c4f06ca45a96a69942c18b79fce858a` |
|  `2.59.0` `2.59`                              | April 25th   | `sha256:3940fcf63420f9c47bb62f711da794643fe351ec83de9e84d5be4f55f4b20ede` |

