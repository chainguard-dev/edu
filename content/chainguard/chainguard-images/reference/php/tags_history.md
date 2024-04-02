---
title: "php Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the php Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-02 00:36:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/php/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/php/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/php/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/php/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)               | Last Changed | Digest                                                                    |
|-----------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev`         | April 1st    | `sha256:bdff07291db848cc5a1c2b2af27afd0f6f270383077083028b85914f1d5643bd` |
|  `latest-fpm-dev`     | April 1st    | `sha256:3bda648297bcca2b6ded77bc141af0997ff2a322b6159fbf3b2d2c820d0e51c4` |
|  `latest-laravel-dev` | April 1st    | `sha256:3d39f41a410b814ab4c32241e651174003f2cd7c8312db01d979d05906818f47` |
|  `latest-laravel`     | March 29th   | `sha256:e16c7d195b744b2e9136c1ece0e0b1668269dc7763a70d49a95a4f984e100bc0` |
|  `latest-fpm`         | March 29th   | `sha256:ae8331feb04566e5c26ac9837d12b02dca8ebf6e0d1cff4a9a50d39a13fed191` |
|  `latest`             | March 29th   | `sha256:334a09f076e3a55a6ed5c351f6d636b6b694643a2c0a024d0b487fcd0dc0cfef` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                          | Last Changed | Digest                                                                    |
|----------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `8-fpm-dev` `8.2-fpm-dev` `8.2.17-r0-fpm-dev` `latest-fpm-dev` `8.2.17-fpm-dev` | April 1st    | `sha256:5e56ef505a519e4288ae1c38cdf62a4366811ca4b9e25186ac5d4f0b9ce888e6` |
|  `8.2-dev` `8-dev` `latest-dev` `8.2.17-dev`                                     | April 1st    | `sha256:6355915223575a32cf5e5744b40239350d90aef3e2f19b6c59ed5bc542d4087f` |
|  `8.2` `8.2.17` `latest` `8`                                                     | March 29th   | `sha256:035ff4453226c9198382c32266c3b2f66ed2a1b6b3ee40de42846c2f353dc13c` |
|  `latest-fpm` `8-fpm` `8.2.17-r0-fpm` `8.2-fpm` `8.2.17-fpm`                     | March 29th   | `sha256:5c269cf540cc3b764497ae5fda2b055b5bf716a0a2676ad559d877a301d456f0` |
|  `8.2.16-fpm-dev` `8.2.16-r2-fpm-dev`                                            | March 12th   | `sha256:97f58bfd708efb00b13ae23147578742f71b69418cf63ac57f84207f3712264c` |
|  `8.2.16-dev`                                                                    | March 12th   | `sha256:e00efa792d0cabce50f11a8aca51fe58801754f3900d1f1a748169b15186b84a` |
|  `8.2.16-r2-fpm` `8.2.16-fpm`                                                    | March 9th    | `sha256:4bd1cd3d6bf2a801bdf5f948742ab0133ffdb50bc787e2be65f16ed2feeb191c` |
|  `8.2.16`                                                                        | March 9th    | `sha256:dae5dfc98fcc7664617d89c77a0a728b68b3558a5281a58c6f1d9d7aee3e98c4` |
|  `8.2.16-r1-fpm`                                                                 | March 6th    | `sha256:13308e1d491d7a0f89a548b3b250b3b9de5973ecb5146a32f0a0771469d9dbcc` |
|  `8.2.16-r1-fpm-dev`                                                             | March 6th    | `sha256:9bad5615e1841275f5b05866500efffdea969487f1143c1bf446a552a72b43ef` |

