---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/fluentd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/fluentd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/fluentd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/fluentd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)              | Last Changed | Digest                                                                    |
|----------------------|--------------|---------------------------------------------------------------------------|
|  `latest-splunk-dev` | May 15th     | `sha256:dec64d9e72543a85578869957f484e3d1555169d10dbff66b6cb3d740460dfdf` |
|  `latest-dev`        | May 15th     | `sha256:2d95fe0cf94fa946eefe3091d8e9ebb5bd80c07465649d15c4ca4d0c519c13a0` |
|  `latest`            | May 15th     | `sha256:92b7c45558a69ae204dacf8c6073c248a83033cabbe49043b927b167965b1d5d` |
|  `latest-splunk`     | May 15th     | `sha256:6d5853c91b23053ca2be7bdf89d6da7fb5d2a537e70f875e655f3573284486c0` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16.5-r0-splunk` `1.16.5-splunk` `1.16-splunk` `1-splunk`                 | May 15th     | `sha256:4776efacc9c6601e28cc97a923d4bb8068fff3f4f7c8266261833c0ecfd52043` |
|  `1.16.5-splunk-dev` `1.16-splunk-dev` `1-splunk-dev` `1.16.5-r0-splunk-dev` | May 15th     | `sha256:97c42a1a04f853f536b9daf92f297065dee7d0ef1a0e98811b0e7bba6f9ffcd8` |
|  `1.16.5` `1` `1.16` `latest`                                                | May 15th     | `sha256:85c0b51b6e07be272c7e0f16a96136b921ad31b60a577bc84cf3a72241b995bf` |
|  `latest-dev` `1.16.5-dev` `1-dev` `1.16-dev`                                | May 15th     | `sha256:ba550d8d2cf7c16bafc61cd8b31f088b0cbae474d5fc4851b61e93ed65b74a62` |

