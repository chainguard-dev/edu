---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
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
|  `openjdk-15-dev` `openjdk-15.0.10-dev` `openjdk-15.0-dev` `openjdk-15.0.10.5-dev` | May 2nd      | `sha256:270e98c201e9c637bef9e21f17986ea0ee4c8731efb3a9fd57aa7730bd7441f2` |
|  `openjdk-11.0.23` `openjdk-11` `openjdk-11.0`                                     | May 2nd      | `sha256:b25602a5f614f0be0e703482fc1240da750a48a95eb8cbeab474d7d3bd94a8bc` |
|  `openjdk-16.0.2-dev` `openjdk-16.0-dev` `openjdk-16.0.2.7-dev` `openjdk-16-dev`   | May 2nd      | `sha256:8fadf746c9ebfdac5372b2fa145cd555b7d44a43f2f5e06f93ff750f6b8029fd` |
|  `openjdk-15` `openjdk-15.0.10` `openjdk-15.0.10.5` `openjdk-15.0`                 | May 2nd      | `sha256:7f930025597bc9471d56a9cce9117c04c4d3c4188fe0e804fc26fc1f9435ff57` |
|  `openjdk-11.0.23-dev` `openjdk-11.0-dev` `openjdk-11-dev`                         | May 2nd      | `sha256:3ac8d86056173779085b00dcd99f9b49b5fddb6d52720771d2a624c945c833d1` |
|  `latest-dev` `openjdk-22.0-dev` `openjdk-22-dev` `openjdk-22.0.1-dev`             | May 2nd      | `sha256:ade2ab28aaf0e4c9453a5bf453984e631c19ac744ba4f476736ce8a7eedef7ee` |
|  `openjdk-17` `openjdk-17.0.11` `openjdk-17.0`                                     | May 2nd      | `sha256:31057417bf64fbf00a46f66006c072a424ba1c528f5ba78cc03795347066e880` |
|  `openjdk-14.0.2` `openjdk-14.0.2.12` `openjdk-14` `openjdk-14.0`                  | May 2nd      | `sha256:60f7fe41572a09a76b6eb43aacef8ab8f25b7224679fcdac344ec7cae7f9db57` |
|  `openjdk-22` `openjdk-22.0.1` `openjdk-22.0` `latest`                             | May 2nd      | `sha256:72103a256f53446ff2f6db156ede6226409e53e125cafa100e343ffb2aceee20` |
|  `openjdk-8-dev` `openjdk-8.392-dev` `openjdk-8.392.08-dev`                        | May 2nd      | `sha256:d8377378d17fba34ee5616eb3ffe392e574722c8bcbe4e8f6de3ddecf1077bde` |
|  `openjdk-21.0.3` `openjdk-21` `openjdk-21.0`                                      | May 2nd      | `sha256:261c76940094d8e8eac30d912e012f1c88342743aafc18cbba442cd1ffb757f3` |
|  `openjdk-16.0.2` `openjdk-16` `openjdk-16.0.2.7` `openjdk-16.0`                   | May 2nd      | `sha256:59f8ff35d9c58b4984c67af9a9ffb63e062b35cefe64e0a9f1c1db7c89945986` |
|  `openjdk-21.0-dev` `openjdk-21-dev` `openjdk-21.0.3-dev`                          | May 2nd      | `sha256:08f78749c7d5360234f2173363cf2b4cb0916253f0fdc87670be4db1f20af277` |
|  `openjdk-17.0-dev` `openjdk-17.0.11-dev` `openjdk-17-dev`                         | May 2nd      | `sha256:86e2cf657901b57d01b188770d48a0ecaf4a22ed7c7298f6c269ef6938b65f84` |
|  `openjdk-8` `openjdk-8.392.08` `openjdk-8.392`                                    | May 2nd      | `sha256:58108c5701ca7da9ca286448553d883dd6e3c17d1c59bf6c8625627b8312679d` |
|  `openjdk-14.0.2-dev` `openjdk-14.0-dev` `openjdk-14.0.2.12-dev` `openjdk-14-dev`  | May 2nd      | `sha256:0344b7715efed8fc67d869ffc5fc3053549bd6dab98ecbb952cdcc905ad0a808` |
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

