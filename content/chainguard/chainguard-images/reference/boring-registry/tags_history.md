---
title: "boring-registry Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the boring-registry Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-19 00:54:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/boring-registry/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/boring-registry/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/boring-registry/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/boring-registry/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | March 18th   | `sha256:d120255c88a177d96aba9e562a202e641b9107410fa47d75d189416a4d9a8f06` |
|  `latest-dev` | March 18th   | `sha256:a0a80a3691c4338870e274a162d5f455ee5918621c780a6b7b6e157af82748da` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `0-dev` `0.13-dev` `0.13.2-dev` | March 18th   | `sha256:4e4707c3ded5e9c8083e3340fd08433d90816e126af60ca01b9604737c3ef1e8` |
|  `latest` `0` `0.13` `0.13.2`                 | March 18th   | `sha256:66b1936abfcce27654828558f759f215c9af24296ca1377002583e204db9e313` |

