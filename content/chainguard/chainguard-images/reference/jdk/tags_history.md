---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-23 00:42:59
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
|  `latest`     | April 22nd   | `sha256:6a733cdd53c73b6c6c0b58bf322ac7480c38e9271d277bb141debaa9f4ec066d` |
|  `latest-dev` | April 22nd   | `sha256:fbe5d22d13f89b6cf4664892b73659e73f149fe270c76482bffd798447176755` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-11.0.23-dev` `openjdk-11.0-dev` `openjdk-11-dev`                         | April 20th   | `sha256:ded6991d2abe52dbf82370d9f1332e6024c6dfd58e47806dafd3eb34f418128a` |
|  `openjdk-8.392.08-dev` `openjdk-8-dev` `openjdk-8.392-dev`                        | April 20th   | `sha256:e8f87980b65adda814489cc36437a1f16cd4db7758cc33fc63724315967c204b` |
|  `openjdk-14.0.2-dev` `openjdk-14.0-dev` `openjdk-14.0.2.12-dev` `openjdk-14-dev`  | April 20th   | `sha256:68b819b3e63c2a2e093f3e12d69b3899fdd7daec1b9d27810213914b86d1f13c` |
|  `openjdk-16-dev` `openjdk-16.0-dev` `openjdk-16.0.2-dev` `openjdk-16.0.2.7-dev`   | April 20th   | `sha256:f88b43e78401dc3feabe2c0363592c19d0d34e7fd6a16152d3861c653bdf7e1e` |
|  `openjdk-17.0-dev` `openjdk-17-dev` `openjdk-17.0.11-dev`                         | April 20th   | `sha256:597492e6fbeea82a5b580915bfbc00ac578c08ec2b18647dca592f3c00554085` |
|  `openjdk-21.0-dev` `openjdk-21-dev` `openjdk-21.0.3-dev`                          | April 20th   | `sha256:3117a7700619fa736bf3dc0e04573071a0f3274b16c44828ca6806fe48d224ee` |
|  `openjdk-15.0-dev` `openjdk-15-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0.10-dev` | April 20th   | `sha256:33fe0a4b8452545d1168ca1e02043eb0cbde415a12c53ec039311ab6423ab9cf` |
|  `openjdk-22-dev` `latest-dev` `openjdk-22.0-dev` `openjdk-22.0.1-dev`             | April 20th   | `sha256:8b0ed5fa75c4cff54df3f950405cc9ec3f5c3b7d4abd2c93b7f9517c7fde1acb` |
|  `openjdk-22.0` `openjdk-22` `latest` `openjdk-22.0.1`                             | April 19th   | `sha256:a74eae2bde2a3cde3c983f8e12431884220e1f1f82a3e260d0d46dba770f8464` |
|  `openjdk-21.0.3` `openjdk-21` `openjdk-21.0`                                      | April 17th   | `sha256:c792a36f99406c8cf2f494255bf11acedc166536a22983ee9fb00ae555f55305` |
|  `openjdk-11` `openjdk-11.0.23` `openjdk-11.0`                                     | April 17th   | `sha256:b5f1ccd4e5a4da5ed74560003cc6f205a3d681dca74fc179bb35bb942c2f6dfb` |
|  `openjdk-17` `openjdk-17.0.11` `openjdk-17.0`                                     | April 17th   | `sha256:101a6a8a06482561299c83dfe9e17603909a36ae94de97c974fea9126895a6e7` |
|  `openjdk-8.392` `openjdk-8.392.08` `openjdk-8`                                    | April 16th   | `sha256:c09f514498438d5971cc0667e9cf8798a16a6b21634337d248ff5905ada10568` |
|  `openjdk-22.0.0`                                                                  | April 11th   | `sha256:7c0389db518bad161ca24bf21cb3ac79f7e724168847035994cc3a49c518a31a` |
|  `openjdk-21.0.2-dev`                                                              | April 11th   | `sha256:0fa62e4be3aaa872aae70cd282e4b3f3bbfba68b9c746c472c68fccdcb403a03` |
|  `openjdk-14` `openjdk-14.0.2` `openjdk-14.0.2.12` `openjdk-14.0`                  | April 11th   | `sha256:57f22a576651c565d892fafe1f33f49fee25ed612f977b59d5695363a2954f32` |
|  `openjdk-17.0.10-dev`                                                             | April 11th   | `sha256:55ea5ef998c15dcfb1ffb82780d17e89f68f8f0c65b1a96ff71ce71220589926` |
|  `openjdk-16.0.2` `openjdk-16.0` `openjdk-16.0.2.7` `openjdk-16`                   | April 11th   | `sha256:27a6c5802f783ad81b76c40e9df6fc82afa1640878555eae1628f8db3e3b1913` |
|  `openjdk-15.0.10.5` `openjdk-15.0.10` `openjdk-15` `openjdk-15.0`                 | April 11th   | `sha256:9f89d9c31d4d89a1fd16b40267378e1cdca79442666aeb99afffb4da06de5af1` |
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

