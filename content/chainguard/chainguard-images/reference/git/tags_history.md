---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-01 00:36:20
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
|  `latest-root`           | June 30th    | `sha256:86896961b6049d834913780b8c8fef780f0db67b60010ad06bf06f90207d58b7` |
|  `latest-root-dev`       | June 30th    | `sha256:3f4264d49e56b723af56ec35dfea31c56404a00756e9d03fc51afec9274eb70d` |
|  `latest-dev`            | June 30th    | `sha256:88181f421a9db0388c0be4186d5db575eabffbaa1b84a782db5aada93e5f328b` |
|  `latest`                | June 30th    | `sha256:08af28f81fffaf3546514b38ff144adcca17c49690169284788bbdb0ac644ea6` |
|  `latest-glibc`          | June 29th    | `sha256:d8ad128dd74efaf13bbf02272547f33dacbacfea7c9283a075d1d5ef07cee203` |
|  `latest-glibc-dev`      | June 29th    | `sha256:dc1b1bb719c7119b595d4d99a4e7fc93c3cf835a334abb5827d459208f9f0c87` |
|  `latest-glibc-root-dev` | June 29th    | `sha256:a0a6f138aaddb318d940598c0833f8d16931a634e1e9609ba8ebbffa52cccbbb` |
|  `latest-glibc-root`     | June 29th    | `sha256:e906348a58cfffdbb2b35e698120d6c73d8f0ac2715b1f3d7424e49389a3c305` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                                                                                    | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `glibc-root-2.45` `latest-glibc-root` `root-2.45.2` `glibc-root-2.45.2` `glibc-root-2` `root-2` `root-2.45` `latest-root`                                 | June 28th    | `sha256:4cb32d7deb17b1fb86799efbfd29d4896c8c8c58f218994c7898d85a50683a57` |
|  `root-2.45.2-dev` `root-2-dev` `latest-glibc-root-dev` `latest-root-dev` `root-2.45-dev` `glibc-root-2-dev` `glibc-root-2.45-dev` `glibc-root-2.45.2-dev` | June 28th    | `sha256:ebb42cea93ee3e384c2b89eefb790bb7707da0e11ad989fef8e4976efb29e2fb` |
|  `latest-glibc-dev` `2.45.2-dev` `glibc-2.45.2-dev` `2.45-dev` `2-dev` `latest-dev` `glibc-2-dev` `glibc-2.45-dev`                                         | June 28th    | `sha256:6b6d308284a6192703e6903a7e04afc5b51717cf7264c25f09a552e1b32bac85` |
|  `glibc-2.45` `glibc-2.45.2` `2` `latest-glibc` `glibc-2` `2.45.2` `2.45` `latest`                                                                         | June 28th    | `sha256:5b63902e98620a66140284d5a29dd3441877f93421e587c99c59ea20f83c49f1` |

