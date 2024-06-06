---
title: "loki Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the loki Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-06 00:48:16
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/loki/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/loki/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/loki/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/loki/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 5th     | `sha256:5027700b11043262bf386b9f689843bae2b0b15492f5d462e5faee6cf0348d1f` |
|  `latest`     | May 31st     | `sha256:52a0823f914f4377ae2dcbc3514ef3696f26996c037138a00bb14bd4d539b46b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.9.8` `2.9` `2`                          | June 5th     | `sha256:8c1d047b260cd632a8a67be7e3dc8d3461069c9c01e31cad99b783295c502d41` |
|  `2.9-dev` `2-dev` `2.9.8-dev`              | June 5th     | `sha256:fe7c4991e112eb388808c3bb95791aa223c5fdf10adb6dfff97aa2f4f006ad5d` |
|  `3.0.0-dev` `3-dev` `3.0-dev` `latest-dev` | June 5th     | `sha256:492d4e1730cb9d14e579103a89ce0e97076af89ddb7cf7c2454317241469e2f1` |
|  `3.0.0` `3.0` `3` `latest`                 | June 5th     | `sha256:962fd18d59b6e5a18fca7151d7eb4fbcab75516326e1be223082265e411f08ac` |

