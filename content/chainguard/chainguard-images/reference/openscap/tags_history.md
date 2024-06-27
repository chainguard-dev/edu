---
title: "openscap Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the openscap Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-27 00:41:27
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/openscap/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/openscap/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/openscap/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/openscap/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 26th    | `sha256:7f26813e78ead83100f6245178334463d1e00c5f71198634a7edc0b0a742f834` |
|  `latest`     | June 26th    | `sha256:f4ac271aabd2daaa50d463b1cd36c0ecc0b1d78c21ee357a1ee3d2228e0ec325` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `1-dev` `1.3.10-dev` `1.3-dev` | June 26th    | `sha256:4e0d17b0c44fe14255bcdfec0bc065768362d4246c8dc295d8438af1c5898ee5` |
|  `1` `1.3.10` `1.3` `latest`                 | June 26th    | `sha256:53adc4332849c1b72c505232231b1fdeffdbf26a2b7c41a3e0cff2483a848ad4` |

