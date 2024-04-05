---
title: "etcd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the etcd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-05 00:47:12
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
|  `latest-dev` | April 4th    | `sha256:fd62d89ab7421dc73da6ccbdca858b186cc74e01942e554a33e2c7e5eb00a012` |
|  `latest`     | April 4th    | `sha256:20ba940d9f32db32cccb0626c3f3e20462556746a7fe3bcd8f9aaaaa9e2df514` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.5.13-dev` `3-dev` `latest-dev` `3.5-dev` | April 3rd    | `sha256:aea99816ed9875853acb295fbebeffedb9a55effcb9ea5a13c940023934613aa` |
|  `3.5` `3.5.13` `latest` `3`                 | April 3rd    | `sha256:fbb56366bc8173bf48c039f71fdec4dbf96d75e365a0a72c24cc916150605121` |
|  `3.4.31` `3.4`                              | April 3rd    | `sha256:25ed0fe820e28c05ca4100ff5b05269147595308f2a805da6d8825338a80d290` |
|  `3.4-dev` `3.4.31-dev`                      | April 3rd    | `sha256:1e48a5e5daf323d36e7d5c5aba2e5c02a21979a158c32106d936636a7998d0e5` |
|  `3.5.12`                                    | March 28th   | `sha256:72161ffc9e1c4662d0642e9616fd5c61023967fd7216d16531466632d0e93f56` |
|  `3.5.12-dev`                                | March 28th   | `sha256:b284c96d56c2492126e7df9530cdccc2462f39422cd363097f835756965b818a` |
|  `3.4.30`                                    | March 18th   | `sha256:68223c6f890df02b29039f7d4587e116be6c7af1e33f153f22bd26de717f0fc4` |
|  `3.4.30-dev`                                | March 18th   | `sha256:bbdd1cd2be3009846b31f572f447c06b82bdeb2ffb9dce582350904e0cb4947e` |

