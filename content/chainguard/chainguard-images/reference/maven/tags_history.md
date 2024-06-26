---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-26 00:35:03
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/maven/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/maven/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/maven/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/maven/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                        | Last Changed | Digest                                                                    |
|--------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `openjdk-21`         | June 25th    | `sha256:813a1a7b7468a7f5561ef6ee657d60d3969e4928b5bc60d63c7c285b95ef2145` |
|  `latest-dev` `openjdk-21-dev` | June 25th    | `sha256:f274d21630bd4cf0f9828196e1c8f0cf635ea8c07e2834daecde13423149c71f` |
|  `openjdk-11-dev`              | June 24th    | `sha256:9f917ef71d3a8e1ca57bb9a0299663a5ee553b1ffea8867191e9a9991f37a629` |
|  `openjdk-17-dev`              | June 24th    | `sha256:886b1ab0922f95cfe69ea34da94dd56be9b66fdb70c03d58801be12e9d1914a4` |
|  `openjdk-11`                  | June 22nd    | `sha256:50e91c69de72a0f6407844922f06dd706f8bb05eb128e300866f5070533ff1d6` |
|  `openjdk-17`                  | June 22nd    | `sha256:8e302e62fd72f0df207bc70af98c80de20c9039434ef5b19c51e964cf6cb595b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-11-3-dev` `openjdk-11-dev` `openjdk-11-3.9.8-dev` `openjdk-11-3.9-dev`              | June 25th    | `sha256:56d461eb7356836a111ca76cb3f81afb1f50150151eeadbea48a66f5f2ca8925` |
|  `openjdk-21-dev` `openjdk-21-3-dev` `latest-dev` `openjdk-21-3.9.8-dev` `openjdk-21-3.9-dev` | June 25th    | `sha256:bf68c60c3326ba30c40bf19145bf9ba386ccde8e02edd37003f2ab4273e8e453` |
|  `openjdk-17-dev` `openjdk-17-3.9.8-dev` `openjdk-17-3-dev` `openjdk-17-3.9-dev`              | June 25th    | `sha256:97f51f6c147521699f12b9d121d3b6bc4a1a0d94ee74c946dd55d0a512ba3ed3` |
|  `openjdk-21-3.9.8` `latest` `openjdk-21-3` `openjdk-21` `openjdk-21-3.9`                     | June 24th    | `sha256:0362d61d6bd0485a1e7b8ab4605372632bfa6f63198d3d985b7002065fcc590f` |
|  `openjdk-11` `openjdk-11-3.9.8` `openjdk-11-3.9` `openjdk-11-3`                              | June 21st    | `sha256:79d295d2a7affdf1701a37d8c12c995829d3fa810b1eba4a7b3ea3beca572267` |
|  `openjdk-17-3` `openjdk-17-3.9` `openjdk-17-3.9.8` `openjdk-17`                              | June 21st    | `sha256:9c7610f43ec41863b70a50532dfb783eb2daa1aca60681103af04e184c03f452` |
|  `openjdk-17-3.9.7-dev`                                                                       | June 19th    | `sha256:c86bd652ab8b3e9efda89777be6457c36986cfea43c21718fb53e2b17827a5d3` |
|  `openjdk-21-3.9.7`                                                                           | June 19th    | `sha256:c2cc4396cf8f464e2ef5de78319b123dd085c6bd573d169f0fd7bcf138b60e76` |
|  `openjdk-11-3.9.7-dev`                                                                       | June 19th    | `sha256:cab436034442b1ff594d13731c695c219a24729630ece1e3f3bb329dcfcfd978` |
|  `openjdk-11-3.9.7`                                                                           | June 19th    | `sha256:854fe0bedc5af844af46773de0404f73dadf3c965476007632e0a81ad7e1e518` |
|  `openjdk-21-3.9.7-dev`                                                                       | June 19th    | `sha256:c4c6a08acd2875f491b90a5b81e0a1e75f88513efae495a1ba43995090dd23ec` |
|  `openjdk-17-3.9.7`                                                                           | June 19th    | `sha256:80e4945ef0bd8f06284f345bd9ed40e62c37813808e518854b84ddb77f7e48d6` |

