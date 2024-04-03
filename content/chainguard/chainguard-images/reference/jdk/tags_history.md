---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-03 00:49:16
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jdk/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jdk/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jdk/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jdk/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 2nd    | `sha256:cb09c36793c09a1a278003eba34d8df898af3d241cbe0a8adb26a5dfdb858633` |
|  `latest`     | March 28th   | `sha256:ef8da9daa0d134cf659ec642b4409d344bf483592847abdc8d1edcdaf65bd28e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-8-dev` `openjdk-8.392-dev` `openjdk-8.392.08-dev`                        | April 2nd    | `sha256:4c9655cfaaea5d2c5bb72c5212a1f6c9cc41857514e4decbd7f4b9babb4fae93` |
|  `openjdk-22.0.0-dev` `latest-dev` `openjdk-22.0-dev` `openjdk-22-dev`             | April 2nd    | `sha256:983d843e687023ea35b83d64b59d88002b0aacdf1aa89494f2fe8376a080a2c7` |
|  `openjdk-11-dev` `openjdk-11.0.22-dev` `openjdk-11.0-dev`                         | April 2nd    | `sha256:8145fe615635d3f271473c70b95c34da2716e068c4c2a21c18faa250a91ebb85` |
|  `openjdk-21.0-dev` `openjdk-21.0.2-dev` `openjdk-21-dev`                          | April 2nd    | `sha256:82a728922658440a3c6d24275121b36d2ff3d9d9f22bace5aacfc76905634870` |
|  `openjdk-16.0-dev` `openjdk-16.0.2-dev` `openjdk-16-dev` `openjdk-16.0.2.7-dev`   | April 2nd    | `sha256:aa8fcbfc9842cfb92d4256f017c009a33fa6acef6e016e1d4c9c43f61a124bf1` |
|  `openjdk-17.0.10-dev` `openjdk-17-dev` `openjdk-17.0-dev`                         | April 2nd    | `sha256:1039345c635a05e86ca18d08f7b226b3479006934469b968fdc20d593a4f992d` |
|  `openjdk-15-dev` `openjdk-15.0.10-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0-dev` | April 2nd    | `sha256:84bbf920630315b820b42a4be8b47618ee350d135817b73226e03648d1c3b4bf` |
|  `openjdk-14.0.2.12-dev` `openjdk-14-dev` `openjdk-14.0.2-dev` `openjdk-14.0-dev`  | April 2nd    | `sha256:998dd6dd038cf24d7b4273b1b780e7986ffb4bbee633e40630cf02ff16bc6b47` |
|  `openjdk-22` `latest` `openjdk-22.0.0` `openjdk-22.0`                             | March 28th   | `sha256:5d5a5e7b08afaf5b5fafcc50418354cb268de59fcd8b813b686ea84f8d4244cf` |
|  `openjdk-21.0` `openjdk-21.0.2` `openjdk-21`                                      | March 28th   | `sha256:340596e50e609e40fd72ac3b3d47b13e58d44a242db8163911cab6cf7a2e5570` |
|  `openjdk-11.0` `openjdk-11.0.22` `openjdk-11`                                     | March 28th   | `sha256:5d1bca9f4144fed4e17af29e9ff634a65326bb29a3b4f87d3fd952ba80f577a4` |
|  `openjdk-15` `openjdk-15.0.10.5` `openjdk-15.0.10` `openjdk-15.0`                 | March 28th   | `sha256:f436fbe65269f535938f8677b8d44779429d8a8543a657b8c7f2f25de75be20a` |
|  `openjdk-16.0` `openjdk-16.0.2` `openjdk-16.0.2.7` `openjdk-16`                   | March 28th   | `sha256:74f93f948efbbf5c983da5f404862a4505418ec6403c2cc07668e8d4a3e35883` |
|  `openjdk-8.392` `openjdk-8` `openjdk-8.392.08`                                    | March 28th   | `sha256:49799586a61a71b2858626ec9439eb3491399f0ad18ad26bd5169f6dcd74b538` |
|  `openjdk-17.0.10` `openjdk-17` `openjdk-17.0`                                     | March 28th   | `sha256:683cf4788787618a3876b40cfe5f1d444536548032b4bca62171b0767380da3e` |
|  `openjdk-14.0` `openjdk-14.0.2` `openjdk-14` `openjdk-14.0.2.12`                  | March 28th   | `sha256:7e5a903de62fa9e54086e15b03af0b0103ce538666e2fa57466271f5a066ed7b` |

