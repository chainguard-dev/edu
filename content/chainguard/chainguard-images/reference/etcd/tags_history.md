---
title: "etcd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the etcd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-23 00:43:06
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
|  `latest-dev` | June 22nd    | `sha256:6247e56f764ab1ef3824703713c64c57bb0b24a85c7f2d4dad03f1e339d65771` |
|  `latest`     | June 20th    | `sha256:271c4f299e7821de28ed533451795fb4dc07146def24928c4b463608f0280ed9` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.4.33-dev` `3.4-dev`                      | June 21st    | `sha256:ae96d6ca9d2369bc563205f3749ab848ffe224a81498a400a0a81b2f7dbe3e0f` |
|  `latest-dev` `3-dev` `3.5.14-dev` `3.5-dev` | June 21st    | `sha256:27b843472c245a348623992902f5b2c9d431c08ebd4e48e5f5c594b6498adf66` |
|  `3` `latest` `3.5` `3.5.14`                 | June 20th    | `sha256:c9a0078e178d3c7f7618317e7163706cc353bba77347db7c89f2815b0fb8aeaf` |
|  `3.4.33` `3.4`                              | June 20th    | `sha256:cebbe61e873d0365ac55ab8a3b2f8200f9dae275b64d4310ae11f10943a66ff3` |

