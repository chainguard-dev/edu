---
title: "az Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the az Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-26 00:36:54
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
|  `latest-dev` | April 25th   | `sha256:64d5a19cb4dd186334e2d299cb7e6282037d73c511b2d141ac4c1d6ac0f62dc6` |
|  `latest`     | April 25th   | `sha256:baa875e7d763480574cf9557b3b51a0d9b2f7ff445c143c4b961e00a7835d44b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.59.0` `2.59` `latest` `2`                 | April 25th   | `sha256:3940fcf63420f9c47bb62f711da794643fe351ec83de9e84d5be4f55f4b20ede` |
|  `2-dev` `latest-dev` `2.59.0-dev` `2.59-dev` | April 25th   | `sha256:17ed79d531e59667175dfb6facfadd99db5c284413b1c5eb9552307d5458d307` |
|  `2.58.0` `2.58`                              | March 29th   | `sha256:734813223228612022acbdaff720f02863b1d55b8fe5f711edfe5534d9496568` |
|  `2.58.0-dev` `2.58-dev`                      | March 29th   | `sha256:6c09869e1638043d06effba12ef736ade8f6c546f4ceaf794e4a0fd303a02350` |

