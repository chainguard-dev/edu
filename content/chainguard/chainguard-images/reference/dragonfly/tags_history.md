---
title: "dragonfly Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the dragonfly Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/dragonfly/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/dragonfly/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/dragonfly/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/dragonfly/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 1st      | `sha256:b9e390b94a68d1fb10f9b332f3605183f1400c69ef80f0b20596aab27cda6222` |
|  `latest`     | May 1st      | `sha256:84f4ca08b338350d270f49924b7eb7ddcc74076f83056940ec94f20e46d830b8` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `1.17` `1.17.1` `1`                 | May 1st      | `sha256:e17ac174994291abd75e7120def430bb25bfe7f3e31ec1e9f29183ba5a185316` |
|  `1-dev` `1.17.1-dev` `latest-dev` `1.17-dev` | May 1st      | `sha256:600f347e7818c513d0fc4197ba4d85fccb06fa06883dedcc84799bd28961c1b2` |
|  `1.15.1-dev` `1.15-dev`                      | April 30th   | `sha256:73085a96dac9b4eecf03b4cda6cdd035a2946bd7bf296d3ef922b8982ad10431` |
|  `1.15` `1.15.1`                              | April 30th   | `sha256:c13eaa4e42c9658886271ab0127ef4e41002aad7c3da491912769c58bb2d992f` |

