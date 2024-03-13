---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-13 00:52:18
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
|  `latest-dev`            | March 12th   | `sha256:ed73d783d7a9b73366bc8aa3c51658d8777c6cab6effd0449db08db1710fc099` |
|  `latest`                | March 12th   | `sha256:cc77e3b25dd5f3a89038fa4df0c4ca1a9078de97a3e52454c165cec71d7d3851` |
|  `latest-root-dev`       | March 12th   | `sha256:1d03320c253316618eb5e1e81da0a23b64ea457484add4f596b75b1d2859da93` |
|  `latest-root`           | March 12th   | `sha256:0ede305c49c0cd0ded1885bdac0a1645d5ee5990fc210a8258009e9f19585c6e` |
|  `latest-glibc-dev`      | March 12th   | `sha256:3ebc1e6885b48259648c80bbf2759db39e29dcbf73063c99375305947366bfa2` |
|  `latest-glibc-root-dev` | March 12th   | `sha256:81561c1ebd4a52c18f3becfb7cb57db1facfbe0dbfb923a0563afbb5f2a76e2d` |
|  `latest-glibc-root`     | March 8th    | `sha256:71c0b48a016a86079670f71f3aa852aee0c559c9255403c1318473327c8ad94f` |
|  `latest-glibc`          | March 8th    | `sha256:110121630cf73870ab6f2b7577a3d9d31dfc849755682084d275a330359233d9` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                   | Last Changed  | Digest                                                                    |
|-------------------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `glibc-root-2.44-dev` `glibc-root-2.44.0-dev` `latest-glibc-root-dev` `glibc-root-2-dev` | March 12th    | `sha256:f219f5aa5a6fd16243f596da90efa2714a8b1d2234d0724000d1824a7d1f4850` |
|  `glibc-2.44.0-dev` `latest-glibc-dev` `glibc-2-dev` `glibc-2.44-dev`                     | March 12th    | `sha256:90d5f4436524c4b188f53185c66710d0dd98c7544060a1c7112478472a7d9b48` |
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

