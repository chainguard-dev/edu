---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-05 00:36:13
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
|  `latest-dev` | June 1st     | `sha256:f23b8abcc273d6ae280689cd3e06539e1aac0540281f0a0cfbf648945f3e0633` |
|  `latest`     | May 30th     | `sha256:73e0de721af78beb9f059f12d34083192610f23bcba953a836b7581ad396a5ab` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-17.0.11-dev` `openjdk-17-dev` `openjdk-17.0-dev`                         | June 1st     | `sha256:1b6cb0ba15f1be28b774a629256f9d76157da6e259ec895118b7f8fed7bfad65` |
|  `openjdk-15.0-dev` `openjdk-15-dev` `openjdk-15.0.10-dev` `openjdk-15.0.10.5-dev` | June 1st     | `sha256:1cfc431a4fa691cd667b6faa8063b1bda0292ddeed691c2d26a884ce64140912` |
|  `openjdk-16.0.2.7-dev` `openjdk-16-dev` `openjdk-16.0.2-dev` `openjdk-16.0-dev`   | June 1st     | `sha256:455b1abba90f5f42fd5d11f6a332839a6da14e4fb2e2d812910eb04de7e2710c` |
|  `openjdk-14.0.2-dev` `openjdk-14.0.2.12-dev` `openjdk-14-dev` `openjdk-14.0-dev`  | June 1st     | `sha256:af11d13c3b2773736f128f2f1cf52609297a21ea89b7c4078663d7af29900c18` |
|  `openjdk-22.0-dev` `openjdk-22-dev` `latest-dev` `openjdk-22.0.1-dev`             | June 1st     | `sha256:64f41be37eae7432628a2634e5eac5e9ca445949c2a7ed48c6bd2beb9df5ddba` |
|  `openjdk-11.0-dev` `openjdk-11.0.23-dev` `openjdk-11-dev`                         | June 1st     | `sha256:08be9f2f5c22e632cab2d3e6a3fc56c61eab7c753c271d5a6b376b642f9a176f` |
|  `openjdk-8.412.08-dev` `openjdk-8.412-dev` `openjdk-8-dev`                        | June 1st     | `sha256:dddde9c1586002525cf157dc8c72ed876270c39c71c06c732be2ab9e705830a4` |
|  `openjdk-21.0.3-dev` `openjdk-21.0-dev` `openjdk-21-dev`                          | June 1st     | `sha256:c7cd60c131e8b8d845e97ae21374d5462cf70f05d4cef688580cf863af8a3b2f` |
|  `openjdk-8` `openjdk-8.412` `openjdk-8.412.08`                                    | May 30th     | `sha256:5566e209c1f461bd308cfdaaf5a19fa9a0e539c72cd7f053896c3f5d9ef829ba` |
|  `openjdk-21.0` `openjdk-21.0.3` `openjdk-21`                                      | May 30th     | `sha256:93342b6a77952e18d974c2c26bf0ee57e29dea020429a94f1888b88bdd8758eb` |
|  `openjdk-15.0.10.5` `openjdk-15.0` `openjdk-15.0.10` `openjdk-15`                 | May 30th     | `sha256:70880f23067dfa3a97bd7e68f5cd99eba18e551ff605e1bcf65cdc4e373d6cf2` |
|  `openjdk-17.0` `openjdk-17` `openjdk-17.0.11`                                     | May 30th     | `sha256:523f4faffa753f57f83ceca057a745e7209a04bbe5b1afe966ae163c25cd2ffc` |
|  `openjdk-22` `openjdk-22.0.1` `latest` `openjdk-22.0`                             | May 30th     | `sha256:eacad718e5f49d3f568d2975f94bae2b20badd075c9bc728c6fd7ff01fc561e1` |
|  `openjdk-11.0.23` `openjdk-11` `openjdk-11.0`                                     | May 30th     | `sha256:4cb2b13c5f6c45c34d6af0235ccabd401154d76a07721a7f7258d9ae44804964` |
|  `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16.0` `openjdk-16`                   | May 30th     | `sha256:21e1661940d507fb0c93fbc78a5623aad923f6195562fca4de388156ce84693c` |
|  `openjdk-14.0.2` `openjdk-14` `openjdk-14.0` `openjdk-14.0.2.12`                  | May 30th     | `sha256:dc9f34a481df0aaf485d6c6ffe48b887009aad2274042616540eb730847b2001` |

