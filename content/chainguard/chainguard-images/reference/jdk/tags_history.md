---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
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
|  `latest-dev` `openjdk-22.0-dev` `openjdk-22.0.1-dev` `openjdk-22-dev`             | May 2nd      | `sha256:b25cba643ba7bdff9183665727d274890c21215defc5effee319e3ab2e554b76` |
|  `openjdk-21.0.3-dev` `openjdk-21-dev` `openjdk-21.0-dev`                          | May 2nd      | `sha256:e6e2f96e6de6e7ee7199d7ff8e32daaf7a71f49bc09194b91cb18ed924f954db` |
|  `openjdk-14` `openjdk-14.0.2.12` `openjdk-14.0` `openjdk-14.0.2`                  | May 2nd      | `sha256:562e1a1b4a029f4ef41532e9399f8b7a2439806d39c1502cf573c9672481a99a` |
|  `openjdk-15` `openjdk-15.0` `openjdk-15.0.10` `openjdk-15.0.10.5`                 | May 2nd      | `sha256:2a2319de4d39d38d9e6336d6eda1e07776f8e2cae7de828cc258096935937442` |
|  `openjdk-16.0.2.7-dev` `openjdk-16-dev` `openjdk-16.0-dev` `openjdk-16.0.2-dev`   | May 2nd      | `sha256:f7dfcf7cf8c6d45e4ff6e30e2721aedddc35aa634b6ef5b4caf87a54072fd7e9` |
|  `openjdk-15.0-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0.10-dev` `openjdk-15-dev` | May 2nd      | `sha256:8a26f995cd6d2bfca77aed78a39005fe539f0675c1d80fec55aeb96f77d850b1` |
|  `openjdk-17.0.11` `openjdk-17.0` `openjdk-17`                                     | May 2nd      | `sha256:1540667cfa15b4634681e7cb12e06c071cde623926101c8379373435da81dc31` |
|  `openjdk-16.0` `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16`                   | May 2nd      | `sha256:c549503946c9180ef899a58e96cbdb2c5db31c7ff4d01b3db803a0dc68bc77c8` |
|  `openjdk-11.0.23-dev` `openjdk-11-dev` `openjdk-11.0-dev`                         | May 2nd      | `sha256:b9b31bffc5c29862e6779bb03069655d8af824d242c5b6c57ee93af07f08af92` |
|  `openjdk-11.0` `openjdk-11.0.23` `openjdk-11`                                     | May 2nd      | `sha256:1175692b7914c28831151d68c09ebc71f333b1dd71f71d8178c4ee05e3fd4867` |
|  `openjdk-8.392` `openjdk-8` `openjdk-8.392.08`                                    | May 2nd      | `sha256:c0c7421e908467b1f5b65121d254d90e16177f6b5b3afdbcf8a3a289dae36eb4` |
|  `openjdk-22` `openjdk-22.0` `latest` `openjdk-22.0.1`                             | May 2nd      | `sha256:127eb9e90d75d43a589716715f1913fbadc2cef16eb350855fbb8b780381c498` |
|  `openjdk-17-dev` `openjdk-17.0-dev` `openjdk-17.0.11-dev`                         | May 2nd      | `sha256:ba49620fa4a4249083733c0c38740b4b6b8a1d3c596bb46570e5dcd4b0360a23` |
|  `openjdk-21.0` `openjdk-21` `openjdk-21.0.3`                                      | May 2nd      | `sha256:089d4cc5acfb3404290443fa5c289c026bccdcf6dcf4097ca8923e70f2776a4d` |
|  `openjdk-8-dev` `openjdk-8.392-dev` `openjdk-8.392.08-dev`                        | May 2nd      | `sha256:7c55339dcb6f12deca531f602bf358e1b548aa57cf5ccc16748391ab2eae5123` |
|  `openjdk-14.0.2.12-dev` `openjdk-14-dev` `openjdk-14.0.2-dev` `openjdk-14.0-dev`  | May 2nd      | `sha256:137f490c181ccef9b8582757ca29858b4cd932233bc70dcbe64095efa7977ef0` |
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

