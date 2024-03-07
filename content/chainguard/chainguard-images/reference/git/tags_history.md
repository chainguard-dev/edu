---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-07 00:51:54
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
|  `latest-glibc`          | March 6th    | `sha256:2afd3dbce6cd47140b86adec9a6320d41f2b6d429f2a4389f6c0268f23e61b5f` |
|  `latest-glibc-root-dev` | March 6th    | `sha256:ec804385b87b2f354ed4910effcc5557be32ff289b9c908a1796f7938e6e4893` |
|  `latest-glibc-dev`      | March 6th    | `sha256:5ac783d641e4219b34c5dbfbfd248b8d4eecadce0fc27a1d22df41669f0bf703` |
|  `latest-glibc-root`     | March 6th    | `sha256:aae55f4922082991f68c5facd61edb367e375f24890c0874fcc02564d4f1a72b` |
|  `latest`                | March 4th    | `sha256:4550b52c7733d002a11e63ca6724defe75285099b883c35dc0bffd2f9f5776f3` |
|  `latest-root-dev`       | March 4th    | `sha256:ff76c8ea49b5cee19a3b6f787e2c1629e4ab46ec62df616412e7042e3c51c7fe` |
|  `latest-dev`            | March 4th    | `sha256:1ca940b298e3dadc073092530531ac3c947da0d46dbbcaf55be2b733b49aba00` |
|  `latest-root`           | March 4th    | `sha256:db0fd121db483f4dfad230333b1532cdfe8831211a6953bf5ba3024ecc121b04` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                   | Last Changed  | Digest                                                                    |
|-------------------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `glibc-root-2.44.0` `glibc-root-2.44` `glibc-root-2` `latest-glibc-root`                 | March 6th     | `sha256:1c017c50a35202046790a43423f223341626dab9981730ff1e071b7def56e068` |
|  `glibc-2-dev` `latest-glibc-dev` `glibc-2.44-dev` `glibc-2.44.0-dev`                     | March 6th     | `sha256:8b5c64bc04026dfd958fe61c1f86b597e2388fd3f9d19e92611d7090d24406bd` |
|  `glibc-2` `glibc-2.44.0` `glibc-2.44` `latest-glibc`                                     | March 6th     | `sha256:b3dfdd5ee32993e53aa4c28013f2a497e810a7537a80cec2ad4945abb78c582f` |
|  `glibc-root-2-dev` `latest-glibc-root-dev` `glibc-root-2.44-dev` `glibc-root-2.44.0-dev` | March 6th     | `sha256:ed77eb1b3d8dbb9ba5814a084ab0ec8dcaa7ccf44945c0cff3e140ea9bdcda15` |
|  `glibc-2.43` `glibc-2.43.2`                                                              | February 22nd | `sha256:d3faa9aada431456a32f757b528c236b155777ff345ce01d15d5f0c424cf43bc` |
|  `glibc-2.43.2-dev` `glibc-2.43-dev`                                                      | February 22nd | `sha256:83620a49e96e024aa0f58042a5cee8bfba67d41c91d73b61c17ae2c0f6ec8392` |
|  `glibc-root-2.43.2` `glibc-root-2.43`                                                    | February 22nd | `sha256:1cf940d7ecc5ec0ac4bf8d000aefc4be4244f0ec8f68a11acab20fe0f5c0c5d7` |
|  `glibc-root-2.43.2-dev` `glibc-root-2.43-dev`                                            | February 22nd | `sha256:14e46233504bdb7d69370eace59e67db5da0bc05e7db079c7f96fbae1c7ec99a` |
|  `glibc-root-2.43.1`                                                                      | February 13th | `sha256:616d39550a72b688faab97f15b50cd872ba97df9837697b27d82990c3bceae40` |
|  `glibc-2.43.1`                                                                           | February 13th | `sha256:c92fde81357abd19dba374d686cd5c8b56428874e586f5ab9fd8e3ce2f183fad` |
|  `glibc-2.43.1-dev`                                                                       | February 13th | `sha256:a504b308e6f6a949b9f40eb907a9c5e376c0d397c2ea26d94791adff9924982e` |
|  `glibc-root-2.43.1-dev`                                                                  | February 13th | `sha256:d0b1ff22ad38649eab38818d0008092aa8cbb14c2ce0d4874445ba3636282651` |
|  `latest`                                                                                 | February 10th | `sha256:fccc781c14433640703748db6655f440587dc4a72dcdc2ae5084879c6e7f2692` |
|  `latest-root-dev`                                                                        | February 10th | `sha256:6d1f62e9c2ddc6c2755c6f8a04a6a9027995c500d9e9746c9b9b03e7c18cd04a` |
|  `latest-dev`                                                                             | February 10th | `sha256:0003913f40bcaf0e049ab42bfb631caffd2fb9c0dab4f9dfb87635aa8c903dce` |
|  `latest-root`                                                                            | February 10th | `sha256:9903bfe9fd2ca4a263c321184c9120e4d524f0c9cfc76ab37fafc4f444ebbf6b` |
|  `glibc-2.43.0-dev`                                                                       | February 8th  | `sha256:771e3197f012f883fe6488341075d541b280a6ecdf38814e2010938927aab3b4` |
|  `glibc-root-2.43.0-dev`                                                                  | February 8th  | `sha256:b00a5d7cabaa09f0208e2a350462ec7359603d3f887d5c76bb110b53dc8eac36` |

