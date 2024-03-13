---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-13 00:52:18
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
|  `latest-dev` | March 12th   | `sha256:afd21428da4e7208445ff7fc860e0d8444a078a14a35c6ea548eb065da772e40` |
|  `latest`     | March 8th    | `sha256:f0e6774dd8d0409453193890b2d9aea91886ecb994051ba20b1f8046e931ec37` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-11.0.22-dev` `openjdk-11-dev` `openjdk-11.0-dev`                         | March 12th   | `sha256:22aadcc00369bf666718c503ade0f52c81442ba1fc86a83eef6905392d5deb61` |
|  `openjdk-17.0.10-dev` `openjdk-17.0-dev` `openjdk-17-dev`                         | March 12th   | `sha256:d5a8908d7111ffa99a925c2da98b06e6cb90d9e71ae42c3bcf6d0496e6ebbb38` |
|  `openjdk-14.0.2-dev` `openjdk-14.0.2.12-dev` `openjdk-14-dev` `openjdk-14.0-dev`  | March 12th   | `sha256:bb1154db274891936e14ed46b87637175481b84fda291aed9da30ff3d6080a8e` |
|  `openjdk-21.0.2-dev` `openjdk-21.0-dev` `latest-dev` `openjdk-21-dev`             | March 12th   | `sha256:32b86201b8f155cc99575f9c2645cfcb81f0d74d6643a75eb07be6af2e9555a7` |
|  `openjdk-15.0.10-dev` `openjdk-15.0.10.5-dev` `openjdk-15-dev` `openjdk-15.0-dev` | March 12th   | `sha256:92884c9813d87d2adfb2da74571d8ddd0fe4a7abf77790a09d8aefe25b2a7414` |
|  `openjdk-16.0.2.7-dev` `openjdk-16.0.2-dev` `openjdk-16.0-dev` `openjdk-16-dev`   | March 12th   | `sha256:94e0058b55cf71a8b0163788f52a25a815377c39542a57b8cb45f07306dd8a7c` |
|  `openjdk-8.392-dev` `openjdk-8-dev` `openjdk-8.392.08-dev`                        | March 12th   | `sha256:b5e068c938c34c77fc2f9c9500b661312955202462cfb48bf3bb1b76ef7b3b0e` |
|  `openjdk-8.392` `openjdk-8` `openjdk-8.392.08`                                    | March 8th    | `sha256:bae886490382480e7c9dc0114c4649e4303c8dd715023f9e4ff11470e181ae92` |
|  `openjdk-15.0.10.5` `openjdk-15` `openjdk-15.0.10` `openjdk-15.0`                 | March 8th    | `sha256:f69188e3fc520e2ac0c552bc8d9f007a76c727b192e9d28eade31bf2336cd7e2` |
|  `openjdk-11` `openjdk-11.0.22` `openjdk-11.0`                                     | March 8th    | `sha256:ff9325703257e5217741f571279d61f0ca63a31c4d0d20dbc9d0fbd49aa61628` |
|  `openjdk-14.0.2` `openjdk-14.0.2.12` `openjdk-14` `openjdk-14.0`                  | March 8th    | `sha256:8390bb4c0f25e4af7f3f6df5d4683ced66e2c9f308623341c0e10901cb8fad9f` |
|  `openjdk-16` `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16.0`                   | March 8th    | `sha256:72889d088d4ec8f77996df3290737c9c0b39ff48a16fdd4aa50a70a91fb64b69` |
|  `openjdk-21` `openjdk-21.0.2` `latest` `openjdk-21.0`                             | March 8th    | `sha256:90fbf09be77cd0ee843aede7e0751c7cf5f4e80fe9752447cf363aa625bab47a` |
|  `openjdk-17.0.10` `openjdk-17` `openjdk-17.0`                                     | March 8th    | `sha256:0ec2447213148e9b670fdad940f0eb858cb995dfc89d4890eb74b2bb7ae837f8` |

