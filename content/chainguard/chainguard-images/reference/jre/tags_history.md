---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
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
|  `openjdk-14-dev` `openjdk-14.0.2-dev` `openjdk-14.0-dev` `openjdk-14.0.2.12-dev`  | May 1st      | `sha256:02e95997edefd986362c23777cb28a019daff8a7828496d106e496deaf457178` |
|  `openjdk-15` `openjdk-15.0.10.5` `openjdk-15.0.10` `openjdk-15.0`                 | May 1st      | `sha256:6b4d04b838b2f87ad929d5e545dbc6d12d16c1aaaea5cb9fde7b7776fa9db750` |
|  `openjdk-16` `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16.0`                   | May 1st      | `sha256:7f9513c326f0fc6a522de0c50cc2681d9330750ab53185b86c6b5296b3893e80` |
|  `openjdk-11.0.23` `openjdk-11` `openjdk-11.0`                                     | May 1st      | `sha256:7500c41ad210a94a7ac601fe0cee48acb4946ca47071074946878d804bc095c2` |
|  `openjdk-8.392.08-dev` `openjdk-8-dev` `openjdk-8.392-dev`                        | May 1st      | `sha256:718b77f83d1a041d2d12ab15949d67258854191376fb82c0ffff5f9d128226b2` |
|  `openjdk-17.0-dev` `openjdk-17.0.11-dev` `openjdk-17-dev`                         | May 1st      | `sha256:b963cd471e247834822eede8e1a417fe162d3ed01a8122cf5bf912dea11071bb` |
|  `openjdk-8.392.08` `openjdk-8.392` `openjdk-8`                                    | May 1st      | `sha256:8a5cc15c0898b5a6a0de94a80e5470e5eb3cead61b67196475869b0b4000a6fa` |
|  `openjdk-16.0-dev` `openjdk-16.0.2-dev` `openjdk-16-dev` `openjdk-16.0.2.7-dev`   | May 1st      | `sha256:013f0ae9f570c9f7bc75608ebd248912b7397af3c211ca0c280d6942439197f5` |
|  `openjdk-11.0-dev` `openjdk-11-dev` `openjdk-11.0.23-dev`                         | May 1st      | `sha256:a860a652eacda92817797a9cc1fcd03fb2b4dbf7421f8a38e27e196885b066ae` |
|  `openjdk-22` `latest` `openjdk-22.0.1` `openjdk-22.0`                             | May 1st      | `sha256:abd087a5f5250e3a5ce2e25785a0d345f711d171d1ab4cc990b5d84266779e8b` |
|  `openjdk-22.0-dev` `openjdk-22-dev` `latest-dev` `openjdk-22.0.1-dev`             | May 1st      | `sha256:14721f5f305484634faf61fa8cdda10472cb147fd92b58992ed690d9d018fa03` |
|  `openjdk-15-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0-dev` `openjdk-15.0.10-dev` | May 1st      | `sha256:eeeb0206da4eda8b6de88b4d1c1ed1590387c44e9be803b6711e162fe05dd82c` |
|  `openjdk-21.0.3` `openjdk-21.0` `openjdk-21`                                      | May 1st      | `sha256:aa27d043295f1390544a8a1f0c5bda1931d9a466c3b1db2c3778bc7b34bbc2ad` |
|  `openjdk-14.0` `openjdk-14.0.2.12` `openjdk-14.0.2` `openjdk-14`                  | May 1st      | `sha256:cfd3eedf9722b15eb06b3612d70eb9375e3ce249b2e7c85e6930aa4f1002b63f` |
|  `openjdk-21.0-dev` `openjdk-21-dev` `openjdk-21.0.3-dev`                          | May 1st      | `sha256:3e119da8a501e31a1d10f269c00de3771e3312858ae7b99a523538367176c83d` |
|  `openjdk-17.0` `openjdk-17.0.11` `openjdk-17`                                     | May 1st      | `sha256:0c29fd7df6deb815b9de9a4b5ddb2c82fb88d6b244feb0a0af448b6f4d59737e` |
|  `openjdk-17.0.10`                                                                 | April 12th   | `sha256:4b16b3e9b03d8a91bb0435f67001754f82ff1fc65ab8d67b0114188a91acbb25` |
|  `openjdk-17.0.10-dev`                                                             | April 12th   | `sha256:84ec1db02e835ed53aba81513bc4e36d63f24fd728f2a68d4d830f6cd826fde6` |
|  `openjdk-22.0.0`                                                                  | April 12th   | `sha256:bc6824cd3807473ed4722d4519036f83b474ba332800daded94cefd178778850` |
|  `openjdk-11.0.22-dev`                                                             | April 12th   | `sha256:38736b2878c0068dab1451acfd6b7a79e4f471840f07066f7630a2c530847027` |
|  `openjdk-11.0.22`                                                                 | April 12th   | `sha256:15a3894105a0a488f6fd0bf7f877b62cbc8048606ef27cdb2a25468d3f10fa66` |
|  `openjdk-21.0.2-dev`                                                              | April 12th   | `sha256:3d2aaabb17c620a1d469a9a500d3095370bd43c95537cbc4875a642ad0d5ae2f` |
|  `openjdk-21.0.2`                                                                  | April 12th   | `sha256:ba10d0b63a7035b2291dd9051856e50be3517731ce6672cebc1f6daaba9d5ab8` |
|  `openjdk-22.0.0-dev`                                                              | April 12th   | `sha256:2e5ed6339e6ba8bbbf73203586d51b4a02549f75e9034b6a8f44930525d69162` |
|  `openjdk17.0.7.5-dev`                                                             | April 21st   | `sha256:d25a9f37fd4ae0a8aa5f0bb7675c9dfaa033e45ac0e4deb4a14e45aee3a4a62b` |
|  `openjdk17.0.7.5`                                                                 | April 21st   | `sha256:eeb678140e97079f4d1e554fa3575831329e78e1382605249ea8ea5558a96d11` |
|  `openjdk11.0.18-dev`                                                              | April 19th   | `sha256:1aa1a3510171eadd787e4a20ae76bef2ff04485d355e01dac1ddef5dbe70a2f2` |
|  `openjdk11.0.18`                                                                  | April 19th   | `sha256:b83713162fda412772e173171870d95621f170ffd46a629f880b44e9bca3a919` |

