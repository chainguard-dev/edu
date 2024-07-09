---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/git/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/git/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/git/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/git/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                  | Last Changed | Digest                                                                    |
|--------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-root-dev`       | July 8th     | `sha256:d7b02c997340347eebdd4b924b0cdbd604cf1d44a4d72a8fc14e22733003efc9` |
|  `latest-glibc`          | July 8th     | `sha256:1eb8ab655bc4d63e0bb7baabc82d756570f38b81d010567798fea31747682324` |
|  `latest`                | July 8th     | `sha256:34de649e402f6d8299847649085d26a1b2699e570db31b00d7df3be58fca4e7b` |
|  `latest-glibc-root`     | July 8th     | `sha256:99fd90fc5890c63137a497b04eb61e5dfdd30776be9d85625736dd718cd83506` |
|  `latest-root`           | July 8th     | `sha256:c4077f5b3c6eccb0b528fc0c0d3076bc3d25eca75452935263faa39de179169c` |
|  `latest-glibc-root-dev` | July 8th     | `sha256:ad7056fedd631f80af5fb468e1ddee29f1bf1691123348ab6915f34c5bcad663` |
|  `latest-dev`            | July 8th     | `sha256:4630f7e0ee21e898b353f2cead0fc2faec548cccbfa2677bd88dfd73823d5ae9` |
|  `latest-glibc-dev`      | July 8th     | `sha256:5fbaed4d49eea190c55da35c3a648260ad9c3316aa35b93d854162e7fb3b86c5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                                                                                    | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-glibc` `glibc-2` `2.45.2` `latest` `2.45` `2` `glibc-2.45.2` `glibc-2.45`                                                                         | July 8th     | `sha256:be367a88ad147a7d9e5c5f0cf4a853b3e0a5297fc3c53b6173b78fc9fa9bf07b` |
|  `root-2.45` `latest-root` `glibc-root-2` `glibc-root-2.45.2` `glibc-root-2.45` `root-2` `root-2.45.2` `latest-glibc-root`                                 | July 8th     | `sha256:26d4d5189fb0872b79270e5862d164b8cbc8796f201f53cf15adcf9c96cc28c4` |
|  `glibc-2-dev` `2-dev` `glibc-2.45.2-dev` `latest-dev` `latest-glibc-dev` `glibc-2.45-dev` `2.45-dev` `2.45.2-dev`                                         | July 8th     | `sha256:4a480fb3719f5d593910413599a6a083fb06b48d195edcee82b12e579cf7956c` |
|  `latest-root-dev` `glibc-root-2.45-dev` `root-2.45-dev` `root-2.45.2-dev` `glibc-root-2.45.2-dev` `latest-glibc-root-dev` `glibc-root-2-dev` `root-2-dev` | July 8th     | `sha256:680500d52dda989efb2ca51f8e61ce968807c108f85a1bf3e0ddefece0e9899e` |

