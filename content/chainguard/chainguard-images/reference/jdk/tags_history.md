---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-01 00:50:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jdk/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jdk/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jdk/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jdk/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 31st     | `sha256:0152c8a3b1d5a25c842925abe8d2f4f7cab3c32e4be0521c9bb7333555953d82` |
|  `latest`     | May 30th     | `sha256:73e0de721af78beb9f059f12d34083192610f23bcba953a836b7581ad396a5ab` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-11-dev` `openjdk-11.0-dev` `openjdk-11.0.23-dev`                         | May 30th     | `sha256:e71811712922ff77ba465b8034de250d8abe0ed52661573803035ded2c9d5561` |
|  `openjdk-16-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0.2-dev` `openjdk-16.0-dev`   | May 30th     | `sha256:24c7d164cba95a2111071e195fae2adf727de63f96446863f2ba08bc420b4d7b` |
|  `openjdk-8` `openjdk-8.412` `openjdk-8.412.08`                                    | May 30th     | `sha256:5566e209c1f461bd308cfdaaf5a19fa9a0e539c72cd7f053896c3f5d9ef829ba` |
|  `openjdk-21.0` `openjdk-21.0.3` `openjdk-21`                                      | May 30th     | `sha256:93342b6a77952e18d974c2c26bf0ee57e29dea020429a94f1888b88bdd8758eb` |
|  `openjdk-21-dev` `openjdk-21.0.3-dev` `openjdk-21.0-dev`                          | May 30th     | `sha256:0ba0efd4fff0f0ba0bcb4a654b03fe4c9735dc79c9f4e3f654ebb7d53a7e3ff2` |
|  `openjdk-15.0.10.5` `openjdk-15.0` `openjdk-15.0.10` `openjdk-15`                 | May 30th     | `sha256:70880f23067dfa3a97bd7e68f5cd99eba18e551ff605e1bcf65cdc4e373d6cf2` |
|  `openjdk-14.0-dev` `openjdk-14-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0.2-dev`  | May 30th     | `sha256:762c47b1d1501a154481a58b5496f9781b03efd487a15db9964d6e80e63ad6a0` |
|  `openjdk-17.0.11-dev` `openjdk-17.0-dev` `openjdk-17-dev`                         | May 30th     | `sha256:c57a86f5d3a3249e4ca942c8f856d81b0234a51982390e770c36d8229ec46757` |
|  `openjdk-22-dev` `openjdk-22.0.1-dev` `openjdk-22.0-dev` `latest-dev`             | May 30th     | `sha256:f0fc0dc3a87a9515b546612f1f3bab39a2d544a88765469553ab3f1ce68626c6` |
|  `openjdk-17.0` `openjdk-17` `openjdk-17.0.11`                                     | May 30th     | `sha256:523f4faffa753f57f83ceca057a745e7209a04bbe5b1afe966ae163c25cd2ffc` |
|  `openjdk-22` `openjdk-22.0.1` `latest` `openjdk-22.0`                             | May 30th     | `sha256:eacad718e5f49d3f568d2975f94bae2b20badd075c9bc728c6fd7ff01fc561e1` |
|  `openjdk-11.0.23` `openjdk-11` `openjdk-11.0`                                     | May 30th     | `sha256:4cb2b13c5f6c45c34d6af0235ccabd401154d76a07721a7f7258d9ae44804964` |
|  `openjdk-8.412-dev` `openjdk-8-dev` `openjdk-8.412.08-dev`                        | May 30th     | `sha256:bc4754818a91f4f1608989715f7f709669e6ce8e190d63670cf724c7eae43ade` |
|  `openjdk-15-dev` `openjdk-15.0.10-dev` `openjdk-15.0-dev` `openjdk-15.0.10.5-dev` | May 30th     | `sha256:ab4f7ab6dfe3c4d52bf86849b0541f69991dcc50454d924cf5044ecc7192c368` |
|  `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16.0` `openjdk-16`                   | May 30th     | `sha256:21e1661940d507fb0c93fbc78a5623aad923f6195562fca4de388156ce84693c` |
|  `openjdk-14.0.2` `openjdk-14` `openjdk-14.0` `openjdk-14.0.2.12`                  | May 30th     | `sha256:dc9f34a481df0aaf485d6c6ffe48b887009aad2274042616540eb730847b2001` |
|  `openjdk-8.392` `openjdk-8.392.08`                                                | May 24th     | `sha256:46923fe97a13048c8f32fe8c3eaef247df1e8d595468bffc7715a094766472cd` |
|  `openjdk-8.392.08-dev` `openjdk-8.392-dev`                                        | May 24th     | `sha256:fbaad341ead88558bba7c9ffc5304d5e8c3c008b1983186039d4cc26cd397adf` |
|  `openjdk-17.0.7.7-dev` `openjdk-17.0.7-dev`                                       | May 24th     | `sha256:4371eadda85a33174d3a7bb8084f7e70e862cb0c032b5b4d38bdd6c6fb168756` |
|  `openjdk-17.0.7.7` `openjdk-17.0.7`                                               | May 24th     | `sha256:d69ada7f17ef4b025c353fae0d02620ebebbf2fa20a615fbc1e2c04bc39a59d5` |
|  `openjdk-11.0.19.5-dev` `openjdk-11.0.19-dev`                                     | May 16th     | `sha256:892756bac53e2b57c43cd8b92d1790d223a18535e7186167dd65b41a51bdab7d` |
|  `openjdk-11.0.19.5` `openjdk-11.0.19`                                             | May 16th     | `sha256:4f282df7a3ebd9751b2372d077f7525f93f379e037cdf3b0d9cb3eb081fde668` |

