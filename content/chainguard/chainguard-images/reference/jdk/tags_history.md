---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
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
|  `latest-dev` | April 29th   | `sha256:edd009c0ff17ed9b589ede796cc1bd19149fb3b3f275e0357ab684f9685ac10e` |
|  `latest`     | April 22nd   | `sha256:6a733cdd53c73b6c6c0b58bf322ac7480c38e9271d277bb141debaa9f4ec066d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-16` `openjdk-16.0.2.7` `openjdk-16.0` `openjdk-16.0.2`                   | May 1st      | `sha256:b7804e088fc802d1bd5de380c3841efff66fd83ba679fa492e87a246eac48177` |
|  `openjdk-17.0` `openjdk-17.0.11` `openjdk-17`                                     | May 1st      | `sha256:6a351a6c3c00164260ab487e58b402dece296443562b208f661115c294d8f9a0` |
|  `openjdk-22.0.1-dev` `openjdk-22.0-dev` `latest-dev` `openjdk-22-dev`             | May 1st      | `sha256:79ac47c8d3b922ce206c634c7a0862a27fc3ab0d7d056dbecb80599a420287ea` |
|  `openjdk-8.392.08` `openjdk-8` `openjdk-8.392`                                    | May 1st      | `sha256:520d43df012a08f0fd8afd8a8131ae48d05eabc5ca545fdeffe3057c303caf8e` |
|  `openjdk-16-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0.2-dev` `openjdk-16.0-dev`   | May 1st      | `sha256:3806b66cfdaeb820917469777a0e9651c31ff510003daa05f54dc4a297648cf9` |
|  `openjdk-21.0-dev` `openjdk-21-dev` `openjdk-21.0.3-dev`                          | May 1st      | `sha256:a345e0d460056df5668004b256cb8da5bb5a5d9f6b09f8211e8da60d2c6b59a0` |
|  `openjdk-14.0.2.12` `openjdk-14` `openjdk-14.0` `openjdk-14.0.2`                  | May 1st      | `sha256:9a049c43f288c091ace200f536fa6c9d14572be5241b2e287189c670658112a5` |
|  `openjdk-21.0.3` `openjdk-21.0` `openjdk-21`                                      | May 1st      | `sha256:f598fb82e3cfd0e593926a3db658e67e7435c72da4f7dfdabbf0d1a593a795ab` |
|  `openjdk-15.0.10.5` `openjdk-15.0.10` `openjdk-15.0` `openjdk-15`                 | May 1st      | `sha256:dae480a4e52b997b6ad7f98aec195f9467a88c759f42b87411f21abc048d770d` |
|  `openjdk-17-dev` `openjdk-17.0.11-dev` `openjdk-17.0-dev`                         | May 1st      | `sha256:e1ecfa13e578d80c9e806badd7f8fb5ebb4fd4caa2f871e01a07f35a7dfdf152` |
|  `openjdk-15.0.10-dev` `openjdk-15.0-dev` `openjdk-15.0.10.5-dev` `openjdk-15-dev` | May 1st      | `sha256:8fd3624e9203badde7fc6a563f7926f4d3af33f4c25453e2bc21fc0ea046f831` |
|  `openjdk-8-dev` `openjdk-8.392-dev` `openjdk-8.392.08-dev`                        | May 1st      | `sha256:0d89243b1fce58dac5c24b0a210f83ef721950447a3271f1894fa9958ea06124` |
|  `openjdk-14-dev` `openjdk-14.0-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0.2-dev`  | May 1st      | `sha256:13b91c4487b66feb61755475076ed073863b16158a76f4dc67e83bb2ad6199f4` |
|  `openjdk-22.0` `latest` `openjdk-22.0.1` `openjdk-22`                             | May 1st      | `sha256:ee32a70432da32915305ecbe5a815fa7abc57e6616a658abf9738a2930d18211` |
|  `openjdk-11` `openjdk-11.0.23` `openjdk-11.0`                                     | May 1st      | `sha256:c407c375573d9c6f887b745b443a09c3a988317e648f4bfdc726b27db3d0bc4e` |
|  `openjdk-11.0.23-dev` `openjdk-11.0-dev` `openjdk-11-dev`                         | May 1st      | `sha256:5fb85325e234e3acf26f425230bc145eec93d5f14edc42b8b69ca0b29d51ddfc` |
|  `openjdk-22.0.0`                                                                  | April 11th   | `sha256:7c0389db518bad161ca24bf21cb3ac79f7e724168847035994cc3a49c518a31a` |
|  `openjdk-21.0.2-dev`                                                              | April 11th   | `sha256:0fa62e4be3aaa872aae70cd282e4b3f3bbfba68b9c746c472c68fccdcb403a03` |
|  `openjdk-17.0.10-dev`                                                             | April 11th   | `sha256:55ea5ef998c15dcfb1ffb82780d17e89f68f8f0c65b1a96ff71ce71220589926` |
|  `openjdk-11.0.22`                                                                 | April 11th   | `sha256:e0f2667d98d019f260105976d2ddad5eeebda2cdd66299bd43212707062354d8` |
|  `openjdk-21.0.2`                                                                  | April 11th   | `sha256:4ece5af768c27dffcffb16780206dfdcd4b45c7edc682250d1b498cb2267d30c` |
|  `openjdk-22.0.0-dev`                                                              | April 11th   | `sha256:580fc13a5ebd248e02273ec8dd432a490813ce8eb45005e0fde8dd05f6ae38d6` |
|  `openjdk-17.0.10`                                                                 | April 11th   | `sha256:b34966b9212d2ce857f154b42bc4d242e0f46a68fb175a4b24d0dbdaafc6bf8b` |
|  `openjdk-11.0.22-dev`                                                             | April 11th   | `sha256:1f6d7112bea7d3ecce9b904977e9d7b9c771a1456313b49baf7d180de6d6c7b9` |
|  `openjdk-17.0.7.5`                                                                | April 21st   | `sha256:42f156acccda6a812a7792a6201b040080865c08d8d88602c9ef7a03c1fb291d` |
|  `openjdk-17.0.7.5-dev`                                                            | April 21st   | `sha256:e2436f9e5d2e780ea5809773e14715030fe90c677badba52a4d134e649beb8c3` |
|  `openjdk-11.0.18`                                                                 | April 19th   | `sha256:616a92ccf6b7da35d0bb32536342dbe71d44aec2a8056f3eba8835d3259806e5` |
|  `openjdk-11.0.18-dev`                                                             | April 19th   | `sha256:45d4fb375ddc407a53ef2fb5ad02c22dfb49e7ce11f1dc9f265552f29c8fc467` |
|  `openjdk-17.0.6-dev`                                                              | April 17th   | `sha256:8af23710b78109323329b8195092c9185f81ed7b002f363fbd85a95ad35bf40c` |
|  `openjdk-17.0.6`                                                                  | April 17th   | `sha256:429deb189bb4d575511a91844b2bdb45e3be956b748b2756408e3be517210541` |

