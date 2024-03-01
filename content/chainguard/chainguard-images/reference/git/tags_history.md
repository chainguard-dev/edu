---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-01 12:14:22
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

| Tag (s)                  | Last Changed  | Digest                                                                    |
|--------------------------|---------------|---------------------------------------------------------------------------|
|  `latest-root`           | February 27th | `sha256:42ee5f8fd3689e6061b7bc13cb7491da8a5bf1a68f554710890b71e6ff700440` |
|  `latest`                | February 27th | `sha256:66f24e75ecdcf96fcb2582ccbc27799626347c6c817e7291373745c1d75c827b` |
|  `latest-root-dev`       | February 27th | `sha256:9e0deaa87e663373bd00a0d0c84cb24526db700d7433d47ae3eeba9b397c2f4d` |
|  `latest-glibc`          | February 27th | `sha256:c173f9f30d438440580adc0738bb5f373b8574218a967796ca609cdbfca12776` |
|  `latest-glibc-root`     | February 27th | `sha256:d3acc4c1ced3ed548ebb9ae38fd83cc279e039a33d695acae272d3ad52823540` |
|  `latest-glibc-dev`      | February 27th | `sha256:0f85990394831b356cb311cc9cbc2f9769be4f191733d5cd3b1e74021a5e3b44` |
|  `latest-glibc-root-dev` | February 27th | `sha256:f24f454d96a2e02acf57cefba020ef6881c3090e2fd650c14bd28e3259b22eda` |
|  `latest-dev`            | February 27th | `sha256:5e36c89abedb1e3f937d63814423219aca1b2b086c12adcf413759df85a0bd3e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                   | Last Changed  | Digest                                                                    |
|-------------------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `latest-glibc-dev` `glibc-2-dev` `glibc-2.44.0-dev` `glibc-2.44-dev`                     | February 26th | `sha256:b07a899014af36b40ec1f2fbe96ac8ab68375cef323a17552dff65ebed7213b7` |
|  `glibc-2.44` `latest-glibc` `glibc-2.44.0` `glibc-2`                                     | February 26th | `sha256:1d263a2d0e7c2bf4fa405e6b71efabdabf7a9b978c4e9a2cb48ce557749eb0fe` |
|  `glibc-root-2` `glibc-root-2.44` `latest-glibc-root` `glibc-root-2.44.0`                 | February 26th | `sha256:5c76658b78a73c10d7ca7808e6ae2cb91c237b2e63f1effa183f7c6218377608` |
|  `glibc-root-2.44-dev` `glibc-root-2.44.0-dev` `glibc-root-2-dev` `latest-glibc-root-dev` | February 26th | `sha256:a9291223d50dd42a0b64a2c79a55b90697b9ef8ccf03eeebb3d5dba3da27bc2a` |
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

