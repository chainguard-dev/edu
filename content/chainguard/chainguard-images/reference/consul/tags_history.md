---
title: "consul Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the consul Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-23 00:43:06
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/consul/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/consul/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/consul/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/consul/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | June 22nd    | `sha256:bd94fcfdfc47df15c182242005dcdd61c8bcdaf5fb1a1427b4588db5fae7986b` |
|  `latest-dev` | June 22nd    | `sha256:6688cf0451a96cb9132fa8bd9746d2492dcc01e23454c9848205de93c1cc3749` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.17.4` `1.17` `latest` `1`                 | June 21st    | `sha256:998fc95a0661edcba0980fdce5b628efd81e2e67533f69dca6a8b3a433db4a21` |
|  `1.15` `1.15.11`                             | June 21st    | `sha256:60b3883f632b5a9adefc632ce119b8e7f4e9b57cafcb0c419c7e5efe17159264` |
|  `1.17-dev` `1.17.4-dev` `1-dev` `latest-dev` | June 21st    | `sha256:f590c1b685b511f34cbd2059ec94650ecbad944a799f8576d736ea2f5f95d81a` |
|  `1.15.11-dev` `1.15-dev`                     | June 21st    | `sha256:e30b42bedd1ad378863ff61b7cebc7620a526487a9fd076063abd2c45897562e` |
|  `1.16-dev` `1.16.7-dev`                      | June 21st    | `sha256:d5b6c274d71c1722ad8118a33c45a590af98be26c3c98d7bf0f5811820845631` |
|  `1.16` `1.16.7`                              | June 21st    | `sha256:94bc6a879442919a10651ab1f1459c337b7130aa6f542aa9aa2eabc53889c01d` |

