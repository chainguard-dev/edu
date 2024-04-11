---
title: "argocd-repo-server Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the argocd-repo-server Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-11 00:54:43
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/argocd-repo-server/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/argocd-repo-server/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/argocd-repo-server/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/argocd-repo-server/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 5th    | `sha256:a5a0274c9e1820a70f6c222c69ccc90e54e77a23c572465c4e45e77d2fc46cfe` |
|  `latest`     | April 5th    | `sha256:63cc057b5d958d07b15c576eecf33463dd94ceaf159418e9f7522c219652f1e2` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2-dev` `latest-dev` `2.10.6-dev` `2.10-dev` | April 10th   | `sha256:927b66fb87c2dbb992a17f54ebc89f1c079a8950c751f3fe5f7350a69b364186` |
|  `2.9-dev` `2.9.11-dev`                       | April 10th   | `sha256:83efc9b32b7de4c76ba37fd117f0188c39d55f176bb6b5f1483403d1b3abc8da` |
|  `2.10` `latest` `2.10.6` `2`                 | April 10th   | `sha256:d9159f0ae418d68a893e3fa2345cd89f9f28c28be6dcd6b2f7c4795e131097b4` |
|  `2.9.11` `2.9`                               | April 10th   | `sha256:0fc427cdb5865da85d8acf8e087884568573f999b3d92f2199ef462b38137bd4` |
|  `2.8.15` `2.8`                               | April 10th   | `sha256:1665cb40b6eeb0158de17668138df454c03fea9753ca0b9dbe1104c6d1fc0a46` |
|  `2.8.15-dev` `2.8-dev`                       | April 10th   | `sha256:b30ee73cbc58eeed27081865398826903f50184ba61325e2c3d3cb23fe56d96e` |
|  `2.9.10-dev`                                 | April 4th    | `sha256:6a87015c45e17feed12bb20a39524bc0eff310c0eede86c43f33f869c0a8ef01` |
|  `2.8.14`                                     | April 4th    | `sha256:27efe278cb5036ebef2eb0e48a03f10bbd268364a017939e12a2d9005b581049` |
|  `2.9.10`                                     | April 4th    | `sha256:f4538cd436980c3941410e0c34413af2039f0ab59ae2670077f6e64e2675c49d` |
|  `2.10.5`                                     | April 4th    | `sha256:74a615b2642cf385c7db30a75ebf685350cfb02f82771798e1bac42d32cd2479` |
|  `2.8.14-dev`                                 | April 4th    | `sha256:156996488e5dfc57c9679db08119e678d1eab59625c5af1777cc98a4139bb7ba` |
|  `2.10.5-dev`                                 | April 4th    | `sha256:60d82fbbce5c9c92d7270a0bad45e9b3fef772d0bcd1dca98c19ba410e736e37` |
|  `2.9.9-dev`                                  | April 2nd    | `sha256:1577222250740d0da7a8bdfe213378a4ec58d5131285bb49ff8f270a58f0b451` |
|  `2.9.9`                                      | April 2nd    | `sha256:b67042b57b515ad90c89a9a0eab64cc17cb4740d273eb9b43ed5186c43e87b5e` |
|  `2.10.4`                                     | March 28th   | `sha256:90dbc3dc5d9ce25118b106cc59e5fef981f5610b350f11c552d81d482678bbf8` |
|  `2.10.4-dev`                                 | March 28th   | `sha256:e43224c420ea1105878bd374f079a600e2450120f2c70c1547c8e7e504fcb507` |
|  `2.8.13`                                     | March 28th   | `sha256:79562ad1de2193debc7f65ebc1e3392aecf7bddc2e5b7a255b939ae0e8d88605` |
|  `2.8.13-dev`                                 | March 28th   | `sha256:4b821f3cff591ceb010ed96072293c888dcf32327f4b43cf813390a91381ddc7` |
|  `2.7.17` `2.7`                               | March 20th   | `sha256:4a56fdff0ef5cdc5c02eb597eb0e965e5beffe529b088da1228c50399f384329` |
|  `2.7-dev` `2.7.17-dev`                       | March 20th   | `sha256:4f20d7a6abdf9512f6b167b260e9295490b132e04235ac5c8ae8a11a7c01a7b3` |

