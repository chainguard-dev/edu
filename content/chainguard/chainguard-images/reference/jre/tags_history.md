---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-26 00:36:54
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
|  `latest`     | April 22nd   | `sha256:74ce09ffa85cb66a0cbaa43cc61277f5abcca7ba4b876b12186cbc03838bd6bf` |
|  `latest-dev` | April 22nd   | `sha256:b0259b5c889298dfe043d255b89b4638517813f0d2a99f94f351cc54b9faebfb` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-8.392` `openjdk-8` `openjdk-8.392.08`                                    | April 25th   | `sha256:7f5f4d65450eb915cffad3949f7d4d50ef7ea41b3794c68ccad887d368c6932a` |
|  `openjdk-8.392-dev` `openjdk-8-dev` `openjdk-8.392.08-dev`                        | April 25th   | `sha256:9952e5f2109576c61ac958f5fac64c9951c0ed3c55e309e8f4d1d1d1bbf205d3` |
|  `openjdk-11` `openjdk-11.0` `openjdk-11.0.23`                                     | April 24th   | `sha256:a82de8e9c3a8ac304c005d39ea5005460c464d253cf5614f58f4aaaa7ede4374` |
|  `openjdk-14.0.2.12` `openjdk-14.0` `openjdk-14.0.2` `openjdk-14`                  | April 24th   | `sha256:59b517101421cdfa3256293f98c1a3189125822df05d06ed671d248a85a80d37` |
|  `openjdk-14.0.2.12-dev` `openjdk-14.0.2-dev` `openjdk-14-dev` `openjdk-14.0-dev`  | April 24th   | `sha256:519b9a90fc23409f81d9aaa3d218b079a653a9f385cac2485ddba08458ca58be` |
|  `openjdk-17.0-dev` `openjdk-17.0.11-dev` `openjdk-17-dev`                         | April 24th   | `sha256:a73c3a7e9fd93463c9d94e9aba180993732568eb31edc3128bc0834a4e4f51a9` |
|  `openjdk-16.0.2.7-dev` `openjdk-16-dev` `openjdk-16.0-dev` `openjdk-16.0.2-dev`   | April 24th   | `sha256:c27f98c59a1da96fafa8af452472f17ac6c9373a0209c0f0938c342ed5c82566` |
|  `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16.0` `openjdk-16`                   | April 24th   | `sha256:be372cee9c9f1350edb4f7e2c0fc91d9a9bf7bff3ffcd1220b31bbc5e5416867` |
|  `openjdk-15` `openjdk-15.0.10` `openjdk-15.0.10.5` `openjdk-15.0`                 | April 24th   | `sha256:2cef14fd08c888eed9d301a88ecd0e944c94a2dbe7dc597b58ea038255cd494e` |
|  `openjdk-22` `latest` `openjdk-22.0.1` `openjdk-22.0`                             | April 24th   | `sha256:74a49a48b7aa110d07e6b070417c3c23a917d6b81cd515b686c72c59bf766734` |
|  `openjdk-22.0.1-dev` `latest-dev` `openjdk-22-dev` `openjdk-22.0-dev`             | April 24th   | `sha256:43adfd19feb32d869abfd57a82ce3adc5fee606ed0793d21d979790c102e62cb` |
|  `openjdk-21.0` `openjdk-21` `openjdk-21.0.3`                                      | April 24th   | `sha256:76c09d2ca52bfb9b8e39d3f2a6ad49ca7cf5cde400f3605f3b26fd01f3cea427` |
|  `openjdk-21-dev` `openjdk-21.0.3-dev` `openjdk-21.0-dev`                          | April 24th   | `sha256:cd375b59c543dc2e60764c2ab2238a30ae89e41a7d899420e8d1fba7e9e1f759` |
|  `openjdk-11.0.23-dev` `openjdk-11.0-dev` `openjdk-11-dev`                         | April 24th   | `sha256:ced6032719c3dbe1772e3e1fd2cd8d502f866e272364e608fd1f8820018a70e5` |
|  `openjdk-15.0.10.5-dev` `openjdk-15.0-dev` `openjdk-15-dev` `openjdk-15.0.10-dev` | April 24th   | `sha256:7ec657505ad5370051a145c74f232344fc14bdd2d179e43c5ed91e4de1e81a27` |
|  `openjdk-17.0.11` `openjdk-17` `openjdk-17.0`                                     | April 24th   | `sha256:a552ed2f0e0197e6cbed2070ee2be2a12ad83b138b17865b6de12e8b8c2f6a45` |
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

