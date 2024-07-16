---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
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
|  `latest`     | July 8th     | `sha256:542b633ad9ec7a4be8d736c32f9d73dcc46d5dd815bda2d89e134f52c3501778` |
|  `latest-dev` | July 8th     | `sha256:a65f91d98f86e572019c5cb1b861d826794865c25a86d02da2ee3b591a3d8757` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-15.0.10-dev` `openjdk-15-dev` `openjdk-15.0-dev` `openjdk-15.0.10.5-dev` | July 8th     | `sha256:f759b3bc93277cda88b9565edf848363da4494d9e93f7a3a5b05ab06127c15b3` |
|  `openjdk-14.0.2-dev` `openjdk-14.0.2.12-dev` `openjdk-14-dev` `openjdk-14.0-dev`  | July 8th     | `sha256:ccf8b1fb11dbbbdae6c02fb14572687e8a655e27df7fc05f2c5bdcbf01809953` |
|  `openjdk-22.0.1` `latest` `openjdk-22` `openjdk-22.0`                             | July 8th     | `sha256:87e2e83f2468df999ff96a12e81f5d5c6fb2ca2c9e3b7da43884c068a1ccddc9` |
|  `openjdk-22-dev` `openjdk-22.0-dev` `openjdk-22.0.1-dev` `latest-dev`             | July 8th     | `sha256:59b9875fcf9089140aa1e1410e4ccd7dc5f03d4458ba19ca7e2097fdc926a429` |
|  `openjdk-11.0.23` `openjdk-11` `openjdk-11.0`                                     | July 8th     | `sha256:176ec134719415ed290ae20e3d49a4b94d10789ee3a7fe08aac035e1d987f505` |
|  `openjdk-14.0.2.12` `openjdk-14` `openjdk-14.0` `openjdk-14.0.2`                  | July 8th     | `sha256:c655729e49daa14ea90c810a48233b406eb574a623a05021d231986c46147311` |
|  `openjdk-21.0.3-dev` `openjdk-21-dev` `openjdk-21.0-dev`                          | July 8th     | `sha256:e28fbdfc59980297f5f9c664ca8a3453e5649a45f7ae7d420ce9c52ee4f7d386` |
|  `openjdk-8-dev` `openjdk-8.412.08-dev` `openjdk-8.412-dev`                        | July 8th     | `sha256:5e20b828541cf558f056146524ca484bdf305b31bc6301893292d4cb6f102355` |
|  `openjdk-16.0.2.7-dev` `openjdk-16.0.2-dev` `openjdk-16.0-dev` `openjdk-16-dev`   | July 8th     | `sha256:0e806867b079bd880495c3a4af640876853dfddd080e106a03809168fd26ea63` |
|  `openjdk-16.0.2` `openjdk-16` `openjdk-16.0.2.7` `openjdk-16.0`                   | July 8th     | `sha256:e9d16ae9e9c2cc841c70eae8a3ce47c7cf7e4d2815df1589691b5d20c059d408` |
|  `openjdk-17` `openjdk-17.0.11` `openjdk-17.0`                                     | July 8th     | `sha256:e128101fadc0570e688acde42e423d715032964bde517b5d5ecffa37c6e40373` |
|  `openjdk-11.0-dev` `openjdk-11.0.23-dev` `openjdk-11-dev`                         | July 8th     | `sha256:0cd6c37959c5fbbfde5fa8d1ebcfe752867d6f7bd98d29d2171400829288a5bb` |
|  `openjdk-17.0-dev` `openjdk-17.0.11-dev` `openjdk-17-dev`                         | July 8th     | `sha256:de3355c7897d3fd81ef553be39e642a78f46f1ef8919b336383b7007abbb199c` |
|  `openjdk-15.0.10.5` `openjdk-15` `openjdk-15.0.10` `openjdk-15.0`                 | July 8th     | `sha256:e08cf2df422a4a990a08f6b9e1a79814e8d75d3b86232ddcf5f9f0ace0f04ea6` |
|  `openjdk-8` `openjdk-8.412` `openjdk-8.412.08`                                    | July 8th     | `sha256:685105f2c3e7582df896aeb589935d0aa20c09ce3e1bde23d46cd7aad5f69f47` |
|  `openjdk-21.0.3` `openjdk-21.0` `openjdk-21`                                      | July 8th     | `sha256:f0876fd3a2dad4cb1c75a77efff67c50ed45fee5e20f653d6d303e7e4b85e127` |

