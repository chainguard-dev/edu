---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-26 00:36:54
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
|  `openjdk-8` `openjdk-8.392.08` `openjdk-8.392`                                    | April 25th   | `sha256:d37aaa74097e2c685b2290df11e565429cc44e82f8bed01857412ab0e032d2ee` |
|  `openjdk-8.392-dev` `openjdk-8-dev` `openjdk-8.392.08-dev`                        | April 25th   | `sha256:f5704a9737db6ba91179233cf726d23e5c83d96e1a2bbdc3398b0c6a6c712b7a` |
|  `openjdk-15.0.10-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0-dev` `openjdk-15-dev` | April 24th   | `sha256:53c544ba7bd3db0e32d558bcc403cbe04f6220acf50e5a9b4dc017f5daa33fe1` |
|  `openjdk-22.0.1` `openjdk-22` `openjdk-22.0` `latest`                             | April 24th   | `sha256:1458ecc3f4821eaab2fafe7b04d4f7a030e5e20ee2251cf5a6698b236add7930` |
|  `openjdk-11.0.23` `openjdk-11` `openjdk-11.0`                                     | April 24th   | `sha256:8ec951cb8784171bb8746cf32a14db041bcafd0093f60da1704b2a9de52f3137` |
|  `openjdk-16-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0-dev` `openjdk-16.0.2-dev`   | April 24th   | `sha256:79e62302cffb0ff3c2ac9c7150bb8e3fe5fb641a90c3901d730559e26beb8b0f` |
|  `openjdk-16` `openjdk-16.0.2` `openjdk-16.0.2.7` `openjdk-16.0`                   | April 24th   | `sha256:6f86e40338a85fe7959714878ca2ff67dbea0b3e40afe6ce23ed7ec0fc2f8f8a` |
|  `openjdk-11.0-dev` `openjdk-11.0.23-dev` `openjdk-11-dev`                         | April 24th   | `sha256:21c827f615691d5be63151a912f270adeec258d1819e6ef8cf1e4cd97da760a9` |
|  `openjdk-17-dev` `openjdk-17.0-dev` `openjdk-17.0.11-dev`                         | April 24th   | `sha256:78534eb42f177133d925c093eefff291e22dcafae4937b44be2ef31ccb4539a1` |
|  `openjdk-21-dev` `openjdk-21.0.3-dev` `openjdk-21.0-dev`                          | April 24th   | `sha256:5e90f9057f9c78066d67a3328862d9abcbb4a9d05da596e4fd2c0a35f52af48f` |
|  `latest-dev` `openjdk-22-dev` `openjdk-22.0.1-dev` `openjdk-22.0-dev`             | April 24th   | `sha256:d106f1c56b4999a71b456cdfad6cccf8bb956e912c3da9a0ef008d2cb5b02b5b` |
|  `openjdk-15.0` `openjdk-15` `openjdk-15.0.10` `openjdk-15.0.10.5`                 | April 24th   | `sha256:8a06400999c0ee18abba32aa2e19e5149ea256e1b044e0a3826aac22b1e72eed` |
|  `openjdk-14-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0.2-dev` `openjdk-14.0-dev`  | April 24th   | `sha256:491a7b13c07906056f3c781849f077b873522f64a7b0f75a9f8adbfd6b14a7c0` |
|  `openjdk-14.0` `openjdk-14.0.2.12` `openjdk-14` `openjdk-14.0.2`                  | April 24th   | `sha256:b193ef5c6023d574e69f87307549f6a113a7947e7b178edb4302a5823c6f6cef` |
|  `openjdk-17.0.11` `openjdk-17` `openjdk-17.0`                                     | April 24th   | `sha256:a3947d5d5f056397e7e04711e780829ae55330e6ee8194c5096fef77df8594e5` |
|  `openjdk-21.0` `openjdk-21.0.3` `openjdk-21`                                      | April 24th   | `sha256:789f6724086bb40e4e823ac08a2b5ff6aef7bd85c36f7abddd6f8edacf8baed4` |
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

