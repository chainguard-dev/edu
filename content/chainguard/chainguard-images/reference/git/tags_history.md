---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-14 00:37:02
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
|  `latest-glibc-root-dev` | March 13th   | `sha256:2db3742eca08e7e6fd0214a8f238014f52249f9f9c9da1db1acca7d093a08114` |
|  `latest-glibc`          | March 13th   | `sha256:da3e03fa45e57c7c3e023fa5b9600ca929f82c7db03f7e32b28e3474ddc1cb0e` |
|  `latest-glibc-dev`      | March 13th   | `sha256:ae9397fed8f1be69beb36a134fb21f8eff8f7de24e956693b083fead954636e9` |
|  `latest-glibc-root`     | March 13th   | `sha256:0ee73fe87419e940db4aad9c47344204e5fc76b13c7964ad48da7ee88f6db193` |
|  `latest`                | March 13th   | `sha256:d74dbe0e13009004369e7e48ba80a4d27ec1644d834029a98e0a6ae0c7eb4ca4` |
|  `latest-root-dev`       | March 13th   | `sha256:2949b436956ba4d2673d775872875ff8a9199cc62a541088bf4f11e24056d6f5` |
|  `latest-dev`            | March 13th   | `sha256:c4d0c7f7ccc1fca44583f2c5d9cfa4372050a07102697f8e3475683e6c1cae02` |
|  `latest-root`           | March 13th   | `sha256:39ecb6352f0da46c85c51d6159d0e66375de289b654d203bfe66e2076fbf78a7` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                   | Last Changed  | Digest                                                                    |
|-------------------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `glibc-root-2.44.0-dev` `glibc-root-2-dev` `latest-glibc-root-dev` `glibc-root-2.44-dev` | March 13th    | `sha256:e5f5f60aa64ea485f46b95d14b03a6687357e7c75334e31c466c5ca9b697cbf4` |
|  `latest-glibc-dev` `glibc-2.44-dev` `glibc-2-dev` `glibc-2.44.0-dev`                     | March 13th    | `sha256:a5fae7853da57f26a53680bcfef25bd2a0eb6e128b123be42d3a28698236543e` |
|  `latest-glibc-root` `glibc-root-2.44.0` `glibc-root-2` `glibc-root-2.44`                 | March 13th    | `sha256:c22719f960e706d4935c51568adbf969adadc295cc0d1bffe1cdd9d4c618ae88` |
|  `glibc-2` `glibc-2.44` `latest-glibc` `glibc-2.44.0`                                     | March 13th    | `sha256:d37e7026b2d35fecb5eb270907ae946a1b8f6297babeba12843ecc7fec36ff30` |
|  `glibc-2.43` `glibc-2.43.2`                                                              | February 22nd | `sha256:d3faa9aada431456a32f757b528c236b155777ff345ce01d15d5f0c424cf43bc` |
|  `glibc-2.43.2-dev` `glibc-2.43-dev`                                                      | February 22nd | `sha256:83620a49e96e024aa0f58042a5cee8bfba67d41c91d73b61c17ae2c0f6ec8392` |
|  `glibc-root-2.43.2` `glibc-root-2.43`                                                    | February 22nd | `sha256:1cf940d7ecc5ec0ac4bf8d000aefc4be4244f0ec8f68a11acab20fe0f5c0c5d7` |
|  `glibc-root-2.43.2-dev` `glibc-root-2.43-dev`                                            | February 22nd | `sha256:14e46233504bdb7d69370eace59e67db5da0bc05e7db079c7f96fbae1c7ec99a` |

