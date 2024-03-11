---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-11 00:52:51
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
|  `latest-glibc-root`     | March 8th    | `sha256:71c0b48a016a86079670f71f3aa852aee0c559c9255403c1318473327c8ad94f` |
|  `latest-glibc-dev`      | March 8th    | `sha256:31e6619e147b6ee760cfd86eeaedf45598144ab9bfd47f0c4545538200e583dd` |
|  `latest-glibc-root-dev` | March 8th    | `sha256:c960940d8a0e02e0e20b9a3f85508547a5177795545876074bcca02923c31303` |
|  `latest-glibc`          | March 8th    | `sha256:110121630cf73870ab6f2b7577a3d9d31dfc849755682084d275a330359233d9` |
|  `latest`                | March 4th    | `sha256:4550b52c7733d002a11e63ca6724defe75285099b883c35dc0bffd2f9f5776f3` |
|  `latest-root-dev`       | March 4th    | `sha256:ff76c8ea49b5cee19a3b6f787e2c1629e4ab46ec62df616412e7042e3c51c7fe` |
|  `latest-dev`            | March 4th    | `sha256:1ca940b298e3dadc073092530531ac3c947da0d46dbbcaf55be2b733b49aba00` |
|  `latest-root`           | March 4th    | `sha256:db0fd121db483f4dfad230333b1532cdfe8831211a6953bf5ba3024ecc121b04` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                   | Last Changed  | Digest                                                                    |
|-------------------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `glibc-root-2-dev` `latest-glibc-root-dev` `glibc-root-2.44.0-dev` `glibc-root-2.44-dev` | March 10th    | `sha256:54e4b0e4924c1bee38f24ba4ba8e43a4061163bd4826ad516a28cda04701eb81` |
|  `latest-glibc-dev` `glibc-2.44-dev` `glibc-2.44.0-dev` `glibc-2-dev`                     | March 10th    | `sha256:0ce90cd2beaaa7770e36d3cabd75a81bba5ff5ac1534dd540b67ce8e8efe530a` |
|  `glibc-2` `glibc-2.44` `latest-glibc` `glibc-2.44.0`                                     | March 8th     | `sha256:c3852310b5545b3ea403a681f5129bf968334d4668ad7948fe067edb24c55539` |
|  `glibc-root-2` `glibc-root-2.44` `glibc-root-2.44.0` `latest-glibc-root`                 | March 8th     | `sha256:50ef405a175baaa14ead1cf0a6b4a547311f1b3358b2c0eb9de3218b83bb06df` |
|  `glibc-2.43` `glibc-2.43.2`                                                              | February 22nd | `sha256:d3faa9aada431456a32f757b528c236b155777ff345ce01d15d5f0c424cf43bc` |
|  `glibc-2.43.2-dev` `glibc-2.43-dev`                                                      | February 22nd | `sha256:83620a49e96e024aa0f58042a5cee8bfba67d41c91d73b61c17ae2c0f6ec8392` |
|  `glibc-root-2.43.2` `glibc-root-2.43`                                                    | February 22nd | `sha256:1cf940d7ecc5ec0ac4bf8d000aefc4be4244f0ec8f68a11acab20fe0f5c0c5d7` |
|  `glibc-root-2.43.2-dev` `glibc-root-2.43-dev`                                            | February 22nd | `sha256:14e46233504bdb7d69370eace59e67db5da0bc05e7db079c7f96fbae1c7ec99a` |
|  `glibc-root-2.43.1`                                                                      | February 13th | `sha256:616d39550a72b688faab97f15b50cd872ba97df9837697b27d82990c3bceae40` |
|  `glibc-2.43.1`                                                                           | February 13th | `sha256:c92fde81357abd19dba374d686cd5c8b56428874e586f5ab9fd8e3ce2f183fad` |
|  `glibc-2.43.1-dev`                                                                       | February 13th | `sha256:a504b308e6f6a949b9f40eb907a9c5e376c0d397c2ea26d94791adff9924982e` |
|  `glibc-root-2.43.1-dev`                                                                  | February 13th | `sha256:d0b1ff22ad38649eab38818d0008092aa8cbb14c2ce0d4874445ba3636282651` |

