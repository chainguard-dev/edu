---
title: "etcd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the etcd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-10 00:50:47
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/etcd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/etcd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/etcd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/etcd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 9th     | `sha256:1497002d1bf4725fdfe612116af5a0479d9a17c4c9aead8bebdd402ee0bd0794` |
|  `latest`     | June 5th     | `sha256:4fdb9aa42c627105c95220b9b684e7c48119ae3c277ad57769bdc444417dfb3d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `3.5-dev` `3.5.14-dev` `3-dev` | June 8th     | `sha256:ee6e262a68fea6f4473bc8ba96fd6d0fc5fdffc8fa2a6a745ceefd9c84b429a4` |
|  `3.4.32-dev` `3.4-dev`                      | June 8th     | `sha256:95bed440406c8d9978ea9cfae50704270b9f2f76ba118003aae92ffacdeb05f1` |
|  `3.4` `3.4.32`                              | June 5th     | `sha256:a26aa0f531889f81d4d37dec83f6577629bcb35992818a2abcf523d942ca5fde` |
|  `latest` `3.5` `3.5.14` `3`                 | June 5th     | `sha256:77855d3ad07f3e0418dc32fe0bca1bbfc7603f2f9f9d591c120c1e87ac078b5a` |

