---
title: "az Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the az Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
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
|  `latest-dev` | May 2nd      | `sha256:35efa339181970e875724c5cb8dd1dc6a1651388fddf24267764904c6ce8aa06` |
|  `latest`     | May 2nd      | `sha256:bc0547e8ea953f29fa26b7143781862c5248610b48d848fdd82be00c8c30da8c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `2` `2.60` `2.60.0`                 | May 2nd      | `sha256:65ebb6ed111ec05e0b2411f244e772fce7a0af7f387d2b8e5c2c6b305d47cf43` |
|  `2.60.0-dev` `latest-dev` `2-dev` `2.60-dev` | May 2nd      | `sha256:900a417663f417787628c006e7e058f3173bb14dfa1d9a9fc7a7e9a32b66b7ba` |
|  `2.59-dev` `2.59.0-dev`                      | April 29th   | `sha256:2dae57e4903bb057f1152588ee958d5d9c4f06ca45a96a69942c18b79fce858a` |
|  `2.59.0` `2.59`                              | April 25th   | `sha256:3940fcf63420f9c47bb62f711da794643fe351ec83de9e84d5be4f55f4b20ede` |

