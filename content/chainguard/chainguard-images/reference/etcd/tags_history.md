---
title: "etcd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the etcd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
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
|  `latest-dev` | April 9th    | `sha256:50a73295880368f06b876c84ca25a44f473fd135ff809b08a2df722a191b79c4` |
|  `latest`     | April 4th    | `sha256:20ba940d9f32db32cccb0626c3f3e20462556746a7fe3bcd8f9aaaaa9e2df514` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.5.13-dev` `3-dev` `latest-dev` `3.5-dev` | April 9th    | `sha256:db585c67f58c390a60e86cf88ffab280b0f4fe92e73581daae08ba26d61eb217` |
|  `3.4.31-dev` `3.4-dev`                      | April 9th    | `sha256:a52500cb8fff9de3959d2e891bb7f844a9077e15247d24e9bf88861753f9384a` |
|  `3.5` `3.5.13` `latest` `3`                 | April 3rd    | `sha256:fbb56366bc8173bf48c039f71fdec4dbf96d75e365a0a72c24cc916150605121` |
|  `3.4.31` `3.4`                              | April 3rd    | `sha256:25ed0fe820e28c05ca4100ff5b05269147595308f2a805da6d8825338a80d290` |
|  `3.5.12`                                    | March 28th   | `sha256:72161ffc9e1c4662d0642e9616fd5c61023967fd7216d16531466632d0e93f56` |
|  `3.5.12-dev`                                | March 28th   | `sha256:b284c96d56c2492126e7df9530cdccc2462f39422cd363097f835756965b818a` |
|  `3.4.30`                                    | March 18th   | `sha256:68223c6f890df02b29039f7d4587e116be6c7af1e33f153f22bd26de717f0fc4` |
|  `3.4.30-dev`                                | March 18th   | `sha256:bbdd1cd2be3009846b31f572f447c06b82bdeb2ffb9dce582350904e0cb4947e` |

