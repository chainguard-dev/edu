---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-29 00:47:42
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
|  `latest-root-dev`       | March 28th   | `sha256:8f28a771ee41d3e13883aa27ca58d1fa5c613b52178f2bc9bee221a7ed474d7b` |
|  `latest`                | March 28th   | `sha256:5a1c61e3dfa39881718833fce4c19325478c8350389d2cdb6bd05e07e04125aa` |
|  `latest-dev`            | March 28th   | `sha256:c6def6c8fd958db416994fe8f97f09eccace164afe649e7c74757d813d461549` |
|  `latest-root`           | March 28th   | `sha256:6ce77f45a63cc3646f62fe51c00e9ae57888cc68a8fa21c8a5d8d765eeb6620a` |
|  `latest-glibc-root-dev` | March 28th   | `sha256:88a94041db47a3e75586f510dc8d79a887248d1160d27b411fd899c274c3d593` |
|  `latest-glibc`          | March 28th   | `sha256:c29789ccae98fc407af318578952702ea20761f02935cb71edcca518c568ebca` |
|  `latest-glibc-root`     | March 28th   | `sha256:aac3cb4884b8dc8d7365145be83ecc2cfbbbac9eabb297238c49d3c07a2a327d` |
|  `latest-glibc-dev`      | March 28th   | `sha256:a8f0b830901c1b73c5437fc13da07be9257349b5c7b5d34190383a584294c6e4` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                   | Last Changed | Digest                                                                    |
|-------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `glibc-2.44-dev` `glibc-2.44.0-dev` `latest-glibc-dev` `glibc-2-dev`                     | March 28th   | `sha256:ea5376cff746adc43235bd36f5407b3858eacbc26b26b980adf34307996cb1cc` |
|  `glibc-root-2.44.0` `latest-glibc-root` `glibc-root-2` `glibc-root-2.44`                 | March 28th   | `sha256:74b31e12a0ee7e40189f12894378d2724c0cfd6f9241ee7842d593413b31b294` |
|  `glibc-2.44` `latest-glibc` `glibc-2` `glibc-2.44.0`                                     | March 28th   | `sha256:6c559901e2016a317b7ca1232efd86dbccb59705cc9532fee4d8c9f0f9040e03` |
|  `glibc-root-2.44-dev` `glibc-root-2-dev` `latest-glibc-root-dev` `glibc-root-2.44.0-dev` | March 28th   | `sha256:14e67147b7fc313bb9fbba4452008a8a1617c12c586d43695e19d239f3320a8a` |

