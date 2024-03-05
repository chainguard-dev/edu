---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-05 17:06:05
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
|  `latest`                | March 4th    | `sha256:4550b52c7733d002a11e63ca6724defe75285099b883c35dc0bffd2f9f5776f3` |
|  `latest-root-dev`       | March 4th    | `sha256:ff76c8ea49b5cee19a3b6f787e2c1629e4ab46ec62df616412e7042e3c51c7fe` |
|  `latest-dev`            | March 4th    | `sha256:1ca940b298e3dadc073092530531ac3c947da0d46dbbcaf55be2b733b49aba00` |
|  `latest-root`           | March 4th    | `sha256:db0fd121db483f4dfad230333b1532cdfe8831211a6953bf5ba3024ecc121b04` |
|  `latest-glibc-root-dev` | March 1st    | `sha256:bacbbaad4d625e675e61b20b07e1f26259652887c77741012d30412aab21d291` |
|  `latest-glibc`          | March 1st    | `sha256:cadfde158808913db68ecb30032f20c1c0edc8c7cf766cb247953bebe91d1f7a` |
|  `latest-glibc-dev`      | March 1st    | `sha256:c4c0d1bad0da6a4a4a9744d34c8643e2172eb2c53b19a09df99b389cd390d918` |
|  `latest-glibc-root`     | March 1st    | `sha256:958be459e44d579aaa6615de5969eee1852077c1a9d3a75b40eae90dc0ff3fcb` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                   | Last Changed  | Digest                                                                    |
|-------------------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `glibc-2.44.0` `glibc-2` `latest-glibc` `glibc-2.44`                                     | March 2nd     | `sha256:9d29fba3e029a82471619697bba55a1e98c1bd662490353a5c884d72c80ec8ed` |
|  `glibc-root-2-dev` `latest-glibc-root-dev` `glibc-root-2.44-dev` `glibc-root-2.44.0-dev` | March 2nd     | `sha256:ea577934ca6bb5af6461f3f408be550d3a9a62b19c3b8a8af86de80652458faf` |
|  `glibc-root-2.44` `glibc-root-2` `latest-glibc-root` `glibc-root-2.44.0`                 | March 2nd     | `sha256:f4d2ea2c481813bf79a8ba17257a90750788772e8bc9d01b9fcb764f95bf5947` |
|  `glibc-2-dev` `latest-glibc-dev` `glibc-2.44-dev` `glibc-2.44.0-dev`                     | March 2nd     | `sha256:b6dc26de32b157f10e7df42dac3e93391e96a777416102aeac4e9afc9d5284d1` |
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
|  `glibc-2.43.0`                                                                           | February 6th  | `sha256:6a0dfe4f6cdd26a87c77864cdf66ed645ba2821eb27aaa996e4fca9967e93c2b` |
|  `glibc-root-2.43.0`                                                                      | February 6th  | `sha256:5cd775f84ffa365cc029de6354545dea008f76a11f062a635348f09b152985cb` |

