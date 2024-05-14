---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-14 00:46:23
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jre/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jre/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jre/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jre/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 29th   | `sha256:89a11a1290c3ace002cac429c569f4f170b4208e148de788e7d729cf1dd41581` |
|  `latest`     | April 22nd   | `sha256:74ce09ffa85cb66a0cbaa43cc61277f5abcca7ba4b876b12186cbc03838bd6bf` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-17.0.11` `openjdk-17.0` `openjdk-17`                                     | May 13th     | `sha256:99f4e6f472619761a6e739445db52aceda3dadcff8815e4e36550a69b3a8549b` |
|  `openjdk-17.0.11-dev` `openjdk-17.0-dev` `openjdk-17-dev`                         | May 13th     | `sha256:1c0acb5d0f4f5c9a78fa696f55a96a6d700e5a154f1230491052bb68fa53aa61` |
|  `openjdk-15-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0.10-dev` `openjdk-15.0-dev` | May 13th     | `sha256:3393bdd9ec6c68304fb25fd177a2ecb531b32f4fa2bfdd204b34386f5fa9a3ce` |
|  `openjdk-21-dev` `openjdk-21.0.3-dev` `openjdk-21.0-dev`                          | May 13th     | `sha256:d4dd254085088d294b34f319d4f4f79a6daef3400cf267d747013212a2f932f5` |
|  `openjdk-22.0-dev` `openjdk-22-dev` `openjdk-22.0.1-dev` `latest-dev`             | May 13th     | `sha256:5f1678f257781c9b2e8394f7a001fc0ec68c31aa2f1213f2f9c41c2beeefb1ff` |
|  `openjdk-16.0.2.7-dev` `openjdk-16.0.2-dev` `openjdk-16.0-dev` `openjdk-16-dev`   | May 13th     | `sha256:a068354ce3882f87e73d2d5be2494606b66fbf7b70bf20b9b9176f2cdbbaf91a` |
|  `openjdk-11.0.23-dev` `openjdk-11-dev` `openjdk-11.0-dev`                         | May 13th     | `sha256:13ce9e55f2e9243554f0151820f24f896602f3ff86cd25ba3805b224daf50b87` |
|  `openjdk-8.392.08-dev` `openjdk-8-dev` `openjdk-8.392-dev`                        | May 13th     | `sha256:f87ce6d905a34a30061a4ebb349a1794adcba5c87935902ca394807d258d530e` |
|  `openjdk-14.0.2.12-dev` `openjdk-14.0.2-dev` `openjdk-14-dev` `openjdk-14.0-dev`  | May 13th     | `sha256:6e741185604a4eda93fb45a2f23b54fb72d1e8a6002c71800e1183dca2fe4b34` |
|  `openjdk-11.0` `openjdk-11.0.23` `openjdk-11`                                     | May 11th     | `sha256:8c80f2cadf779faeb08959b0d755a6c92d6528cabe7bb3a1d8d32bd7b74a4602` |
|  `openjdk-14.0.2` `openjdk-14.0` `openjdk-14.0.2.12` `openjdk-14`                  | May 11th     | `sha256:0ae6bee285553e32fb2cc0adc2046c50e82b9dcab0648dc8d8dde0bbd319a479` |
|  `openjdk-21.0` `openjdk-21.0.3` `openjdk-21`                                      | May 11th     | `sha256:b2c2d7498a875c0315b53bc3d9441a8f10fa8c8c61800cd3f6c3be0781c41c32` |
|  `openjdk-8.392` `openjdk-8.392.08` `openjdk-8`                                    | May 10th     | `sha256:c4d78c1f468e52370fb3bfaf03166f14f421c5d2854cf4ee703eb70f97a57b5d` |
|  `openjdk-15.0` `openjdk-15` `openjdk-15.0.10.5` `openjdk-15.0.10`                 | May 10th     | `sha256:a219de1dbb06c53d9d11390dbfc0f3005adb78f259b6f5b4b85bfd4943798f1a` |
|  `openjdk-22.0` `latest` `openjdk-22.0.1` `openjdk-22`                             | May 10th     | `sha256:57400d410ae71aee7a621acdeb024cade196e93fec3df4861e9e6b4f93cd2725` |
|  `openjdk-16.0` `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16`                   | May 10th     | `sha256:7c1461ba6016c745c1d1d652377149c448ee3e3544178b0121ef0de55f7ff16f` |
|  `openjdk17.0.7.5-dev`                                                             | April 21st   | `sha256:d25a9f37fd4ae0a8aa5f0bb7675c9dfaa033e45ac0e4deb4a14e45aee3a4a62b` |
|  `openjdk17.0.7.5`                                                                 | April 21st   | `sha256:eeb678140e97079f4d1e554fa3575831329e78e1382605249ea8ea5558a96d11` |
|  `openjdk11.0.18-dev`                                                              | April 19th   | `sha256:1aa1a3510171eadd787e4a20ae76bef2ff04485d355e01dac1ddef5dbe70a2f2` |
|  `openjdk11.0.18`                                                                  | April 19th   | `sha256:b83713162fda412772e173171870d95621f170ffd46a629f880b44e9bca3a919` |

