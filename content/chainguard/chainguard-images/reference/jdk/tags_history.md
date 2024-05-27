---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-27 00:43:34
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
|  `latest-dev` | May 24th     | `sha256:d283e8ca2fc03b562456d2018ec314ec81a0b18d8af44c72dcd9e6b3ab6e3362` |
|  `latest`     | May 24th     | `sha256:885937f5e3c0a97df355fe5a798de76df067ef1010bd409cf0e5e75c6e72efee` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-15.0.10` `openjdk-15.0` `openjdk-15.0.10.5` `openjdk-15`                 | May 24th     | `sha256:4c5acd5e105887dda2a8c5654c4d4ac59def1d90f5818e8d00304854f45ce913` |
|  `openjdk-8.392` `openjdk-8` `openjdk-8.392.08`                                    | May 24th     | `sha256:46923fe97a13048c8f32fe8c3eaef247df1e8d595468bffc7715a094766472cd` |
|  `openjdk-16-dev` `openjdk-16.0-dev` `openjdk-16.0.2-dev` `openjdk-16.0.2.7-dev`   | May 24th     | `sha256:272c3b4c9b368bf574fdcef6f07facb4b62326f4c077f667700ae0f04bf6d6c8` |
|  `openjdk-22` `openjdk-22.0` `openjdk-22.0.1` `latest`                             | May 24th     | `sha256:728d6923543428b4a37371999c51de38bafb97b6e6c3fbf95c27d67511363d05` |
|  `openjdk-21.0.3` `openjdk-21.0` `openjdk-21`                                      | May 24th     | `sha256:7c2a182e77aefd9511f0b813403f062a6ee8b5e6ef1b168783b3534b04a7f6fa` |
|  `openjdk-17-dev` `openjdk-17.0-dev` `openjdk-17.0.11-dev`                         | May 24th     | `sha256:0d17a5885a7b9681d8fc3a684b7eb6bd389f03f12e47e57913da15872272f0c9` |
|  `openjdk-22-dev` `latest-dev` `openjdk-22.0-dev` `openjdk-22.0.1-dev`             | May 24th     | `sha256:db4392b3331394a56d85ca9a5d14afd0fa17521ae4360e82dfbfb7cca29d909b` |
|  `openjdk-16.0` `openjdk-16.0.2` `openjdk-16` `openjdk-16.0.2.7`                   | May 24th     | `sha256:dfdbd895fa163eda6af660484074a1027b06342e3d6519470c8e262931ed830c` |
|  `openjdk-17.0` `openjdk-17.0.11` `openjdk-17`                                     | May 24th     | `sha256:83f3ec77eba9d66a3e20198cd344a344ff94240c9365e673658a116c289288a1` |
|  `openjdk-15.0.10.5-dev` `openjdk-15-dev` `openjdk-15.0-dev` `openjdk-15.0.10-dev` | May 24th     | `sha256:2096b82981b29b08f508869f7a9ab5374eeb41a733c3eaf35b3fb1651c309ea9` |
|  `openjdk-11.0-dev` `openjdk-11.0.23-dev` `openjdk-11-dev`                         | May 24th     | `sha256:86fc305bc32907a4946106f33d6a8bcc9aa445ac6554e756a323f83d02fd0217` |
|  `openjdk-8.392.08-dev` `openjdk-8-dev` `openjdk-8.392-dev`                        | May 24th     | `sha256:fbaad341ead88558bba7c9ffc5304d5e8c3c008b1983186039d4cc26cd397adf` |
|  `openjdk-14.0.2-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0-dev` `openjdk-14-dev`  | May 24th     | `sha256:78faf3e461a524c9e422eb9664196f0c60b26bc1319aeb1a092427781e699c29` |
|  `openjdk-11.0.23` `openjdk-11.0` `openjdk-11`                                     | May 24th     | `sha256:6da060cd001984116527f651d53d8d4385f5a74bfd8bc8e12deadcf1f8cc9e9a` |
|  `openjdk-14.0.2` `openjdk-14.0` `openjdk-14` `openjdk-14.0.2.12`                  | May 24th     | `sha256:61686d68b47b32208dd30a721c26e140d5e4b852b0ec22f5f8469d106e2eaa33` |
|  `openjdk-21.0.3-dev` `openjdk-21-dev` `openjdk-21.0-dev`                          | May 24th     | `sha256:da823497f61441cdef05186a653c1140fded77b45dab9c8a6e88417f5185bdff` |
|  `openjdk-17.0.7.7-dev` `openjdk-17.0.7-dev`                                       | May 24th     | `sha256:4371eadda85a33174d3a7bb8084f7e70e862cb0c032b5b4d38bdd6c6fb168756` |
|  `openjdk-17.0.7.7` `openjdk-17.0.7`                                               | May 24th     | `sha256:d69ada7f17ef4b025c353fae0d02620ebebbf2fa20a615fbc1e2c04bc39a59d5` |
|  `openjdk-11.0.19.5-dev` `openjdk-11.0.19-dev`                                     | May 16th     | `sha256:892756bac53e2b57c43cd8b92d1790d223a18535e7186167dd65b41a51bdab7d` |
|  `openjdk-11.0.19.5` `openjdk-11.0.19`                                             | May 16th     | `sha256:4f282df7a3ebd9751b2372d077f7525f93f379e037cdf3b0d9cb3eb081fde668` |

