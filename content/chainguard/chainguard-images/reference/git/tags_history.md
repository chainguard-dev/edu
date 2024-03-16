---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-16 00:33:13
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
|  `latest-root-dev`       | March 15th   | `sha256:6cb080479d7dbb878762e4a158690c381e8956e3ce53221d28fb924d2e8b9413` |
|  `latest-root`           | March 15th   | `sha256:5349718e288564eccbacb90da8bfd37d26057303401676db86bee2155cb2ee87` |
|  `latest`                | March 15th   | `sha256:30d910bcc53bcfb32c7f26364ef3f2d2ba9c627369d6537da4c0583f5da69567` |
|  `latest-dev`            | March 15th   | `sha256:99606173586c226abf86aac0ee1b598cc2da9f40d0e7f6e868498854237b4789` |
|  `latest-glibc-root-dev` | March 15th   | `sha256:5033a38ee2a929b338e538eeae4b899912174c0470fbf3494581d80123c5ebb4` |
|  `latest-glibc-dev`      | March 15th   | `sha256:74ec0ed61efbfe6ad7d40784b46434e626e8a760be6ed92bf32d9073811db7c1` |
|  `latest-glibc`          | March 15th   | `sha256:d868e229077c3de9b552e63f2833b9e36d3bbff395f5b7d9aaceada0f155439e` |
|  `latest-glibc-root`     | March 15th   | `sha256:0f35034f2a3a4e03bbf4ff452c07af99b5e011f1728606e6fbfdb1fc724f125f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                   | Last Changed  | Digest                                                                    |
|-------------------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `glibc-2.44.0-dev` `glibc-2-dev` `latest-glibc-dev` `glibc-2.44-dev`                     | March 15th    | `sha256:b77fe7814de7465249651ee4ee7e64128afbb7e7b9487d8235c13f1d980af078` |
|  `latest-glibc-root` `glibc-root-2` `glibc-root-2.44.0` `glibc-root-2.44`                 | March 15th    | `sha256:f9aadf4742180794890c6777e4486e9d56336211dc39e8391b8fea0b8a850fbc` |
|  `glibc-2.44.0` `glibc-2.44` `glibc-2` `latest-glibc`                                     | March 15th    | `sha256:f25f4e3f8fcaa44d6fcd8f54798188835795a00e29621b522fa0e5e291ddc919` |
|  `latest-glibc-root-dev` `glibc-root-2-dev` `glibc-root-2.44-dev` `glibc-root-2.44.0-dev` | March 15th    | `sha256:d5e86aacff8ec973252aba414efa860a091e747665ab195f307d37041b3847e2` |
|  `glibc-2.43` `glibc-2.43.2`                                                              | February 22nd | `sha256:d3faa9aada431456a32f757b528c236b155777ff345ce01d15d5f0c424cf43bc` |
|  `glibc-2.43.2-dev` `glibc-2.43-dev`                                                      | February 22nd | `sha256:83620a49e96e024aa0f58042a5cee8bfba67d41c91d73b61c17ae2c0f6ec8392` |
|  `glibc-root-2.43.2` `glibc-root-2.43`                                                    | February 22nd | `sha256:1cf940d7ecc5ec0ac4bf8d000aefc4be4244f0ec8f68a11acab20fe0f5c0c5d7` |
|  `glibc-root-2.43.2-dev` `glibc-root-2.43-dev`                                            | February 22nd | `sha256:14e46233504bdb7d69370eace59e67db5da0bc05e7db079c7f96fbae1c7ec99a` |

