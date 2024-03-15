---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-15 00:51:40
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
|  `latest-glibc-root-dev` | March 14th   | `sha256:5f886976a89db8062733741350e0814b16e4a91e945f0de172e0d075b6d5d1e8` |
|  `latest-glibc`          | March 14th   | `sha256:fb2c3bc88004aea2020305da7331faccbd1e1dfec91c209271a7552de9032864` |
|  `latest-glibc-root`     | March 14th   | `sha256:d38c14006dca174cb5c04d1eaeea039a3c161033fb33425d1645ad2d512d60e0` |
|  `latest-glibc-dev`      | March 14th   | `sha256:d74bbf9bee07e833c9e74070c5b2ac85db8019d8a0174eba333b13758b55324f` |
|  `latest`                | March 13th   | `sha256:d74dbe0e13009004369e7e48ba80a4d27ec1644d834029a98e0a6ae0c7eb4ca4` |
|  `latest-root-dev`       | March 13th   | `sha256:2949b436956ba4d2673d775872875ff8a9199cc62a541088bf4f11e24056d6f5` |
|  `latest-dev`            | March 13th   | `sha256:c4d0c7f7ccc1fca44583f2c5d9cfa4372050a07102697f8e3475683e6c1cae02` |
|  `latest-root`           | March 13th   | `sha256:39ecb6352f0da46c85c51d6159d0e66375de289b654d203bfe66e2076fbf78a7` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                   | Last Changed  | Digest                                                                    |
|-------------------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `glibc-2.44.0-dev` `glibc-2.44-dev` `latest-glibc-dev` `glibc-2-dev`                     | March 14th    | `sha256:821a0f817b71b41fe71d7cd37025d4906d985c2a61b34546b47485b9ca51ca55` |
|  `glibc-root-2.44` `glibc-root-2.44.0` `glibc-root-2` `latest-glibc-root`                 | March 14th    | `sha256:f96a314ad776227c6b9388232a0cdffb282cf97853d366f9d7daca458e40faa6` |
|  `latest-glibc` `glibc-2.44` `glibc-2` `glibc-2.44.0`                                     | March 14th    | `sha256:f8c661b963adf8ebb342e0fc2c2067636e16d8f9ba6096e7a5d0a78e1b4dea43` |
|  `latest-glibc-root-dev` `glibc-root-2.44-dev` `glibc-root-2.44.0-dev` `glibc-root-2-dev` | March 14th    | `sha256:c252d5afa07af3999e71caec866c0edf2cbf91afa014d50529f221fc6934e358` |
|  `glibc-2.43` `glibc-2.43.2`                                                              | February 22nd | `sha256:d3faa9aada431456a32f757b528c236b155777ff345ce01d15d5f0c424cf43bc` |
|  `glibc-2.43.2-dev` `glibc-2.43-dev`                                                      | February 22nd | `sha256:83620a49e96e024aa0f58042a5cee8bfba67d41c91d73b61c17ae2c0f6ec8392` |
|  `glibc-root-2.43.2` `glibc-root-2.43`                                                    | February 22nd | `sha256:1cf940d7ecc5ec0ac4bf8d000aefc4be4244f0ec8f68a11acab20fe0f5c0c5d7` |
|  `glibc-root-2.43.2-dev` `glibc-root-2.43-dev`                                            | February 22nd | `sha256:14e46233504bdb7d69370eace59e67db5da0bc05e7db079c7f96fbae1c7ec99a` |

