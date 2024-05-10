---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-10 00:43:45
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
|  `openjdk-11` `openjdk-11.0` `openjdk-11.0.23`                                     | May 9th      | `sha256:a774de5f4ffee19bfdb4c5210f5727499fb478b113991a68fa25354df77d02c9` |
|  `openjdk-11.0.23-dev` `openjdk-11-dev` `openjdk-11.0-dev`                         | May 9th      | `sha256:5c42b7bc4b7ca206114876c346302fc6f5aecf685a480bc44316685c23542694` |
|  `latest` `openjdk-22` `openjdk-22.0` `openjdk-22.0.1`                             | May 9th      | `sha256:213fe9c14a30ecc3de5b0ef33d4612cec13885f1fa66b28fdee8d96e47da1e1b` |
|  `openjdk-22.0-dev` `latest-dev` `openjdk-22-dev` `openjdk-22.0.1-dev`             | May 9th      | `sha256:3efa8e4c036270fb2ecd3bf5e1c982183f67bdd510a1761a70b163bc8dfa7229` |
|  `openjdk-21.0-dev` `openjdk-21.0.3-dev` `openjdk-21-dev`                          | May 9th      | `sha256:3b64fcf603fe508fe36c753c5826f6c0005bbe7ca81bfc5cb16b0cd66c307a09` |
|  `openjdk-21` `openjdk-21.0.3` `openjdk-21.0`                                      | May 9th      | `sha256:a67feaad8c078169b35b8dda0d452471b957636fb45854560e343444c15c8839` |
|  `openjdk-8` `openjdk-8.392.08` `openjdk-8.392`                                    | May 8th      | `sha256:adc31e9fc3a3e02e5dae9d01564807e278f2f7bd3f80e0588ca78f01f201ca10` |
|  `openjdk-8.392.08-dev` `openjdk-8-dev` `openjdk-8.392-dev`                        | May 8th      | `sha256:273b0de379345e9490f78f06456befc65c205f86c28fae93f46e43bc91b334d3` |
|  `openjdk-17.0.11-dev` `openjdk-17.0-dev` `openjdk-17-dev`                         | May 4th      | `sha256:14ab740215ab608727c5948371a3895ea780d55e3974d432e9f65ec40884fcf9` |
|  `openjdk-15.0.10-dev` `openjdk-15.0-dev` `openjdk-15-dev` `openjdk-15.0.10.5-dev` | May 4th      | `sha256:996f281e0eb00f91a6425bf7017a01786c6ab7c61be3937bba295832390773c6` |
|  `openjdk-16.0.2.7-dev` `openjdk-16.0-dev` `openjdk-16-dev` `openjdk-16.0.2-dev`   | May 4th      | `sha256:9e78ce1724440889475907e7847a2a75291bdd5aa69344cb848b225cfcf29dd9` |
|  `openjdk-14.0.2-dev` `openjdk-14.0-dev` `openjdk-14-dev` `openjdk-14.0.2.12-dev`  | May 4th      | `sha256:173e108c3ab8f5adcb337cdac5c91c29561ac5fdccda9d6cba485bee0580e702` |
|  `openjdk-14` `openjdk-14.0.2.12` `openjdk-14.0` `openjdk-14.0.2`                  | May 2nd      | `sha256:562e1a1b4a029f4ef41532e9399f8b7a2439806d39c1502cf573c9672481a99a` |
|  `openjdk-15` `openjdk-15.0` `openjdk-15.0.10` `openjdk-15.0.10.5`                 | May 2nd      | `sha256:2a2319de4d39d38d9e6336d6eda1e07776f8e2cae7de828cc258096935937442` |
|  `openjdk-17.0.11` `openjdk-17.0` `openjdk-17`                                     | May 2nd      | `sha256:1540667cfa15b4634681e7cb12e06c071cde623926101c8379373435da81dc31` |
|  `openjdk-16.0` `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16`                   | May 2nd      | `sha256:c549503946c9180ef899a58e96cbdb2c5db31c7ff4d01b3db803a0dc68bc77c8` |
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

