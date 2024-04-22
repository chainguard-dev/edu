---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-22 00:45:38
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
|  `latest-dev` | April 21st   | `sha256:d52548cbd026297d54e2d9bed5c595446b98b4917c0325adf27addd3859d0a46` |
|  `latest`     | April 19th   | `sha256:a6e0fefad0294fe59705df76097ce196f42554840f396a7395fc549bcdea97a5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-11.0.23-dev` `openjdk-11.0-dev` `openjdk-11-dev`                         | April 20th   | `sha256:2acf1e81e0ffafa16a20503c9cd6d684ea70f784e460c114d377264626bb06ab` |
|  `openjdk-8.392.08-dev` `openjdk-8.392-dev` `openjdk-8-dev`                        | April 20th   | `sha256:3af30654a5cab19b269402ce8f58f4d967743e088f718843061301e958520263` |
|  `openjdk-14.0.2-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0-dev` `openjdk-14-dev`  | April 20th   | `sha256:1af6cf076ca912be183aae08d5a4c1101c0dc5087a2a152a910f74ff59596831` |
|  `openjdk-15.0.10.5-dev` `openjdk-15-dev` `openjdk-15.0-dev` `openjdk-15.0.10-dev` | April 20th   | `sha256:e72f3fc950fc3b43eda2c087a11218746e58c4690f778b4ab6842f206771ce2b` |
|  `openjdk-22.0-dev` `openjdk-22-dev` `openjdk-22.0.1-dev` `latest-dev`             | April 20th   | `sha256:f65df3b41f68efba67704a91c421d361e748590dd0840a57415e8537f5eca3f6` |
|  `openjdk-16-dev` `openjdk-16.0.2-dev` `openjdk-16.0-dev` `openjdk-16.0.2.7-dev`   | April 20th   | `sha256:d076977895e76800954bce579599cee2a9c426b98f16ca9e50370a7202ef1cd7` |
|  `openjdk-17-dev` `openjdk-17.0-dev` `openjdk-17.0.11-dev`                         | April 20th   | `sha256:96010af853dceb9b21b07f8649d5a064608909de8d12baeecd8903d419886f48` |
|  `openjdk-21.0-dev` `openjdk-21.0.3-dev` `openjdk-21-dev`                          | April 20th   | `sha256:966983b2852a8d364e4d884ca32829cb288317ac58e9e21f84858e2e47ce2d5a` |
|  `latest` `openjdk-22.0.1` `openjdk-22.0` `openjdk-22`                             | April 19th   | `sha256:968971f271ed327bf5059fe1bf045e731aef8d484bc62a5d4fd1f62ba6ec385d` |
|  `openjdk-21` `openjdk-21.0.3` `openjdk-21.0`                                      | April 17th   | `sha256:effd544d47f7b1221b4885a788a70489f09c52b3257d3fbd002d230044c52404` |
|  `openjdk-11` `openjdk-11.0.23` `openjdk-11.0`                                     | April 17th   | `sha256:317c4ab96c6de41f688103dac5761c5436eef41e3a591faf261b9a909daae0a7` |
|  `openjdk-17` `openjdk-17.0` `openjdk-17.0.11`                                     | April 17th   | `sha256:d32d3e40b29f08e22ef633ef03851d71c1d67f58c67ca70c17d42cf5dd59dab5` |
|  `openjdk-8.392.08` `openjdk-8.392` `openjdk-8`                                    | April 16th   | `sha256:e49fdbffedd9c1a44f8e36dc2c1d3c40ab0701034a5327ed1fba2bfdf1828c78` |
|  `openjdk-17.0.10`                                                                 | April 12th   | `sha256:4b16b3e9b03d8a91bb0435f67001754f82ff1fc65ab8d67b0114188a91acbb25` |
|  `openjdk-17.0.10-dev`                                                             | April 12th   | `sha256:84ec1db02e835ed53aba81513bc4e36d63f24fd728f2a68d4d830f6cd826fde6` |
|  `openjdk-16.0` `openjdk-16.0.2.7` `openjdk-16` `openjdk-16.0.2`                   | April 12th   | `sha256:e4bcbb11e53587315fd039c60924b064bbd6951c7a5f2d8d683a0f3d5922500f` |
|  `openjdk-22.0.0`                                                                  | April 12th   | `sha256:bc6824cd3807473ed4722d4519036f83b474ba332800daded94cefd178778850` |
|  `openjdk-11.0.22-dev`                                                             | April 12th   | `sha256:38736b2878c0068dab1451acfd6b7a79e4f471840f07066f7630a2c530847027` |
|  `openjdk-14.0.2` `openjdk-14` `openjdk-14.0` `openjdk-14.0.2.12`                  | April 12th   | `sha256:435712667300dc498f9e58999619e7b319316e7b5d184fe61a27db814555165e` |
|  `openjdk-15.0.10.5` `openjdk-15.0` `openjdk-15.0.10` `openjdk-15`                 | April 12th   | `sha256:baa5ddb14ba98494f781a30d7446152d2d74ee52f6911e90a63c09d217132bda` |
|  `openjdk-11.0.22`                                                                 | April 12th   | `sha256:15a3894105a0a488f6fd0bf7f877b62cbc8048606ef27cdb2a25468d3f10fa66` |
|  `openjdk-21.0.2-dev`                                                              | April 12th   | `sha256:3d2aaabb17c620a1d469a9a500d3095370bd43c95537cbc4875a642ad0d5ae2f` |
|  `openjdk-21.0.2`                                                                  | April 12th   | `sha256:ba10d0b63a7035b2291dd9051856e50be3517731ce6672cebc1f6daaba9d5ab8` |
|  `openjdk-22.0.0-dev`                                                              | April 12th   | `sha256:2e5ed6339e6ba8bbbf73203586d51b4a02549f75e9034b6a8f44930525d69162` |
|  `openjdk17.0.7.5-dev`                                                             | April 21st   | `sha256:d25a9f37fd4ae0a8aa5f0bb7675c9dfaa033e45ac0e4deb4a14e45aee3a4a62b` |
|  `openjdk17.0.7.5`                                                                 | April 21st   | `sha256:eeb678140e97079f4d1e554fa3575831329e78e1382605249ea8ea5558a96d11` |
|  `openjdk11.0.18-dev`                                                              | April 19th   | `sha256:1aa1a3510171eadd787e4a20ae76bef2ff04485d355e01dac1ddef5dbe70a2f2` |
|  `openjdk11.0.18`                                                                  | April 19th   | `sha256:b83713162fda412772e173171870d95621f170ffd46a629f880b44e9bca3a919` |

