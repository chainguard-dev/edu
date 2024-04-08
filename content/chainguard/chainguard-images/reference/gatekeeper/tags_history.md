---
title: "gatekeeper Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gatekeeper Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-08 00:38:35
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gatekeeper/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gatekeeper/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/gatekeeper/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gatekeeper/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 5th    | `sha256:aaf13d380febaf7b4490070475966562f4553042a9e652650f10405395cafaeb` |
|  `latest`     | April 4th    | `sha256:51fccfc02c52eaaebd5d983ff53fa822777c715fe3874487bfa86222d29a8127` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.14.1-dev` `latest-dev` `3.14-dev` `3-dev` | April 5th    | `sha256:4ed8ef107592d08380a75e0727bdc3e49a0c1c4a2ad5106579a0d4eaeefbc94d` |
|  `3.13.4-dev` `3.13-dev`                      | April 5th    | `sha256:ed36f09d17a4994fd021bfe68375e887e0c6050942c21221f2f230c5856a3663` |
|  `3.12.0-dev` `3.12-dev`                      | April 5th    | `sha256:7d9071e7f38d274420db68c03d18ca8c03838c041fa9d10cc1b6728cc481aefe` |
|  `latest` `3.14` `3` `3.14.1`                 | April 4th    | `sha256:cf4f06161ae528be2620a6477d118bd11652caedb06a6851d7b721be693cc028` |
|  `3.13.4` `3.13`                              | April 4th    | `sha256:e172ee396c6d9321b455d8664ff88c1d9ce7c017072e63e4758b2dad6f3bc04f` |
|  `3.12.0` `3.12`                              | April 4th    | `sha256:a948c59cccced4c98b267d3ca567805cdf2252728a40fe63440dfad43607868c` |
|  `3.14.0-dev`                                 | March 12th   | `sha256:b4b3ef5c89c9f443b9f12a2199c3c4dffb1260770cb5c30f8d0f8dd33eca2eb1` |

