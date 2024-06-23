---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-23 00:43:06
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
|  `latest` `openjdk-21`         | June 22nd    | `sha256:73d0a2fd316c85d306833049454e89f9f0afd806499fa138f821e51ec68de94f` |
|  `openjdk-21-dev` `latest-dev` | June 22nd    | `sha256:68d8ffcf3c76b12e9ed7adb3f1d6ee371e9f6a2229ad534e3a46139494051ad0` |
|  `openjdk-11`                  | June 22nd    | `sha256:50e91c69de72a0f6407844922f06dd706f8bb05eb128e300866f5070533ff1d6` |
|  `openjdk-17`                  | June 22nd    | `sha256:8e302e62fd72f0df207bc70af98c80de20c9039434ef5b19c51e964cf6cb595b` |
|  `openjdk-11-dev`              | June 22nd    | `sha256:1c769ae46925803ca5b1415b6e1d56c8322ab9a76eacc9351480b10fd3039504` |
|  `openjdk-17-dev`              | June 22nd    | `sha256:1e3d5eff8dc119d4730ba31f65c9234e90b4daeb94403d9f03dca0ff1bee0ed5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-21-dev` `openjdk-21-3.9-dev` `latest-dev` `openjdk-21-3-dev` `openjdk-21-3.9.8-dev` | June 21st    | `sha256:58556ff02e4dfc60b3be001a38c47248e4d478fe473470a5c0a86bda587cb014` |
|  `openjdk-17-3.9.8-dev` `openjdk-17-3.9-dev` `openjdk-17-dev` `openjdk-17-3-dev`              | June 21st    | `sha256:27741bb82ee925a4d62793c9757b70a4b35f6e0350dca4681fd6470ac1b69a04` |
|  `openjdk-11` `openjdk-11-3.9.8` `openjdk-11-3.9` `openjdk-11-3`                              | June 21st    | `sha256:79d295d2a7affdf1701a37d8c12c995829d3fa810b1eba4a7b3ea3beca572267` |
|  `openjdk-11-3.9.8-dev` `openjdk-11-3.9-dev` `openjdk-11-3-dev` `openjdk-11-dev`              | June 21st    | `sha256:8bbf0b8e923a9e8a9a5a63c8db7cb618177c886cab7decc773920deffcfc0ed8` |
|  `openjdk-17-3` `openjdk-17-3.9` `openjdk-17-3.9.8` `openjdk-17`                              | June 21st    | `sha256:9c7610f43ec41863b70a50532dfb783eb2daa1aca60681103af04e184c03f452` |
|  `openjdk-21-3` `openjdk-21-3.9.8` `openjdk-21` `latest` `openjdk-21-3.9`                     | June 21st    | `sha256:ba80a2804a97b482364157d8121de860a958958a11677b56140591602fd126fd` |
|  `openjdk-17-3.9.7-dev`                                                                       | June 19th    | `sha256:c86bd652ab8b3e9efda89777be6457c36986cfea43c21718fb53e2b17827a5d3` |
|  `openjdk-21-3.9.7`                                                                           | June 19th    | `sha256:c2cc4396cf8f464e2ef5de78319b123dd085c6bd573d169f0fd7bcf138b60e76` |
|  `openjdk-11-3.9.7-dev`                                                                       | June 19th    | `sha256:cab436034442b1ff594d13731c695c219a24729630ece1e3f3bb329dcfcfd978` |
|  `openjdk-11-3.9.7`                                                                           | June 19th    | `sha256:854fe0bedc5af844af46773de0404f73dadf3c965476007632e0a81ad7e1e518` |
|  `openjdk-21-3.9.7-dev`                                                                       | June 19th    | `sha256:c4c6a08acd2875f491b90a5b81e0a1e75f88513efae495a1ba43995090dd23ec` |
|  `openjdk-17-3.9.7`                                                                           | June 19th    | `sha256:80e4945ef0bd8f06284f345bd9ed40e62c37813808e518854b84ddb77f7e48d6` |

