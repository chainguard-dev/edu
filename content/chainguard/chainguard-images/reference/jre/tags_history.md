---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-20 00:48:18
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
|  `latest-dev` | May 17th     | `sha256:9c6b9bbe1c4f6601e694525dad9c3296c14bdef96646833fc26365cbb7976c80` |
|  `latest`     | May 17th     | `sha256:219e35fb84fba3d3bbd155027c4253ce2ed6b330cec077b3a2367869d737c8f1` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-16.0.2.7-dev` `openjdk-16.0.2-dev` `openjdk-16-dev` `openjdk-16.0-dev`   | May 19th     | `sha256:e259b1c9d697aca60ee20b513c79d6f967e3f9a983fa6114734f9bc9393eb289` |
|  `openjdk-22-dev` `openjdk-22.0-dev` `openjdk-22.0.1-dev` `latest-dev`             | May 19th     | `sha256:bdbde298dfe11c4adcad35eb106e0ed1c5cc7a8f7937818209b7990cdb3afd40` |
|  `openjdk-17-dev` `openjdk-17.0.11-dev` `openjdk-17.0-dev`                         | May 19th     | `sha256:9efdd8c2256418302278a114454d50f57e5aa58618c3304f3baeda25efae2857` |
|  `openjdk-15.0.10.5-dev` `openjdk-15.0.10-dev` `openjdk-15-dev` `openjdk-15.0-dev` | May 19th     | `sha256:2d39b0239292c19703d4f73948773ac8b03277f2bfa0e2a3b9144f44b09cc0be` |
|  `openjdk-14.0-dev` `openjdk-14.0.2-dev` `openjdk-14-dev` `openjdk-14.0.2.12-dev`  | May 19th     | `sha256:980f339cfcf98dbc3ebce668bb4cbad113906e4d00bbe02b25167bf1d1813996` |
|  `openjdk-11.0-dev` `openjdk-11-dev` `openjdk-11.0.23-dev`                         | May 19th     | `sha256:84382627371a30327293a0c091212e38e63f49a366e239c0b86d527d456fe501` |
|  `openjdk-8.392.08-dev` `openjdk-8.392-dev` `openjdk-8-dev`                        | May 19th     | `sha256:db8ad6c5c19387921253bc5b2602da63047a7d9b7ea3d15e71b1dad09a26ea37` |
|  `openjdk-21.0-dev` `openjdk-21-dev` `openjdk-21.0.3-dev`                          | May 19th     | `sha256:a287dee1df4c149071850e9af5088730b3a1e63d94cfcb6841906b8003b2a8d5` |
|  `openjdk-21.0.3` `openjdk-21.0` `openjdk-21`                                      | May 17th     | `sha256:072d56b8c3a4b041e75e604d0c82043c45839c162e530ed9d69b73f18e6f6b3d` |
|  `openjdk-16.0` `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16`                   | May 17th     | `sha256:282f3385eed3927689614256354bb6d896bcd283e063a48caa16ec3e47e8ba27` |
|  `openjdk-15` `openjdk-15.0` `openjdk-15.0.10.5` `openjdk-15.0.10`                 | May 17th     | `sha256:600bf73eb2602c54f786c45155349c22dd7e0cd39ed703d6d5196602707bda80` |
|  `openjdk-14` `openjdk-14.0.2` `openjdk-14.0` `openjdk-14.0.2.12`                  | May 17th     | `sha256:958212a2afab2311da851e92f2557a7e9b9f781be6badd8ee4ed77dbeae9df55` |
|  `openjdk-22.0` `latest` `openjdk-22.0.1` `openjdk-22`                             | May 17th     | `sha256:bd96e03b29fe0315f48e4b1b97908922fed591da9e0733e2db4e777706f1d5da` |
|  `openjdk-17.0.11` `openjdk-17` `openjdk-17.0`                                     | May 17th     | `sha256:4b1e401edb0d40de2b884ced59f948a2045c1c68deefd08f11434f9a437460a9` |
|  `openjdk-11.0.23` `openjdk-11.0` `openjdk-11`                                     | May 17th     | `sha256:ddf8fa00079280b1f16ddba3ab1b309d73f076cf0502075797cc69f1b9412f4f` |
|  `openjdk-8` `openjdk-8.392.08` `openjdk-8.392`                                    | May 17th     | `sha256:be2dfaf7976800325bd4e5a94884a67400201d38885fa47d8c80b1d93fd0ffa9` |
|  `openjdk11.0.19.5` `openjdk11.0.19`                                               | May 16th     | `sha256:677dee78db811af812e1bb2bd33c1f247a5a4e0418169c194d965fc618768bba` |
|  `openjdk11.0.19.5-dev` `openjdk11.0.19-dev`                                       | May 16th     | `sha256:30327ab04c691b2d4f2bfa4391531384ea89b4e204cc65b90eee78a5cbc83156` |
|  `openjdk17.0.7.5-dev`                                                             | April 21st   | `sha256:d25a9f37fd4ae0a8aa5f0bb7675c9dfaa033e45ac0e4deb4a14e45aee3a4a62b` |
|  `openjdk17.0.7.5`                                                                 | April 21st   | `sha256:eeb678140e97079f4d1e554fa3575831329e78e1382605249ea8ea5558a96d11` |

