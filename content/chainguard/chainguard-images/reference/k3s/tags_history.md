---
title: "k3s Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the k3s Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-25 00:53:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/k3s/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/k3s/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/k3s/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/k3s/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | April 24th   | `sha256:4374b77c33e5ade7253d1874395726fd92b7d1025b78a5e775212b99f31d17b0` |
|  `latest-dev` | April 24th   | `sha256:38bed92f520a2376bb0ebd36d65ffb943a7e47a2cdf41274386512e5f0314c05` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `1.29.3` `1` `1.29`                 | April 24th   | `sha256:532b1ce14cea72eecefcdb10c8c979833542b470b1d692e441d9e45b062825b5` |
|  `1.29-dev` `1.29.3-dev` `latest-dev` `1-dev` | April 24th   | `sha256:6e231e1b2ac9015586ea71f7f66992aae16bfe4b3472be29a8ce0f9594eb3a26` |
|  `1.29.2`                                     | March 27th   | `sha256:6802353a8ce9d324acca6bccec57576188d3409c7368ee09dbd7da1dff406b15` |
|  `1.29.2-dev`                                 | March 27th   | `sha256:a32df5dfc4ffa58db6bd3f3b72540e543ed59a476840be94bf033f6448cf7ce4` |

