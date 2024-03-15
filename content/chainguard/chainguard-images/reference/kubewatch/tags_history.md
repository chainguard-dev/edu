---
title: "kubewatch Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubewatch Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-15 00:51:40
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubewatch/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubewatch/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/kubewatch/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubewatch/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | March 14th   | `sha256:2f53ab1bd916c2cc02eb6d4a6b14ddf757e71bb647b76cf5ba77daff72ce4d5c` |
|  `latest-dev` | March 14th   | `sha256:c1830aa5d3f61ef3b3dc7f2d497fa81f2db3106651fb0df5b50a3d00804c3a58` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2-dev` `latest-dev` `2.5.0-dev` `2.5-dev` | March 14th   | `sha256:7357046b56918df01591d0cb6e0be5c86da6a1e548fb04cd37b2a3376a7bba96` |
|  `2` `2.5` `latest` `2.5.0`                 | March 14th   | `sha256:ca53f36983ad6b9d0957808885cf1a6f4607c52052397af4ae1b6d1bf228e36a` |

