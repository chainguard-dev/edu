---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-12 00:55:01
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
|  `latest-dev` | March 11th   | `sha256:fd6d94b3a0d2492d22844e0a57b612151cd7cc25cff5bdd9245bdb34a59730d9` |
|  `latest`     | March 8th    | `sha256:f0e6774dd8d0409453193890b2d9aea91886ecb994051ba20b1f8046e931ec37` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-21-dev` `openjdk-21.0.2-dev` `latest-dev` `openjdk-21.0-dev`             | March 10th   | `sha256:d7d8c6c6cb02514c5e1fbe432088e1081cf074563667f71571b073e9b53816d9` |
|  `openjdk-17.0-dev` `openjdk-17.0.10-dev` `openjdk-17-dev`                         | March 10th   | `sha256:60a3c08c06fa2eb2d19b190858ed033ad6190885399339be4d940d56cc31a4ad` |
|  `openjdk-16.0.2-dev` `openjdk-16-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0-dev`   | March 10th   | `sha256:9487a823bed14970640ed8e73113119cb5a6b1d4b98ab45d083681ad3011991f` |
|  `openjdk-14.0.2.12-dev` `openjdk-14.0.2-dev` `openjdk-14-dev` `openjdk-14.0-dev`  | March 10th   | `sha256:0dded8e830defb41c451edc2af4127612399b8d5e358274d689c69c1002719f5` |
|  `openjdk-11.0.22-dev` `openjdk-11.0-dev` `openjdk-11-dev`                         | March 10th   | `sha256:d8ce997b62f64335db0c57d903c9d0c212290fb4063037f4f23137cceb244576` |
|  `openjdk-8.392-dev` `openjdk-8-dev` `openjdk-8.392.08-dev`                        | March 10th   | `sha256:59ccf115c737e3283cdedef02b9665bad451893b59261ffc39cfe07bd5298c98` |
|  `openjdk-15-dev` `openjdk-15.0-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0.10-dev` | March 10th   | `sha256:6a08c29d5d5cb78e5011e2ffc3bd59137758ab239302b2ad66d7d8a994022e14` |
|  `openjdk-8.392` `openjdk-8` `openjdk-8.392.08`                                    | March 8th    | `sha256:bae886490382480e7c9dc0114c4649e4303c8dd715023f9e4ff11470e181ae92` |
|  `openjdk-15.0.10.5` `openjdk-15` `openjdk-15.0.10` `openjdk-15.0`                 | March 8th    | `sha256:f69188e3fc520e2ac0c552bc8d9f007a76c727b192e9d28eade31bf2336cd7e2` |
|  `openjdk-11` `openjdk-11.0.22` `openjdk-11.0`                                     | March 8th    | `sha256:ff9325703257e5217741f571279d61f0ca63a31c4d0d20dbc9d0fbd49aa61628` |
|  `openjdk-14.0.2` `openjdk-14.0.2.12` `openjdk-14` `openjdk-14.0`                  | March 8th    | `sha256:8390bb4c0f25e4af7f3f6df5d4683ced66e2c9f308623341c0e10901cb8fad9f` |
|  `openjdk-16` `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16.0`                   | March 8th    | `sha256:72889d088d4ec8f77996df3290737c9c0b39ff48a16fdd4aa50a70a91fb64b69` |
|  `openjdk-21` `openjdk-21.0.2` `latest` `openjdk-21.0`                             | March 8th    | `sha256:90fbf09be77cd0ee843aede7e0751c7cf5f4e80fe9752447cf363aa625bab47a` |
|  `openjdk-17.0.10` `openjdk-17` `openjdk-17.0`                                     | March 8th    | `sha256:0ec2447213148e9b670fdad940f0eb858cb995dfc89d4890eb74b2bb7ae837f8` |

