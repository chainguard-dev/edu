---
title: "postgres Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the postgres Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/postgres/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/postgres/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/postgres/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/postgres/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 15th     | `sha256:1f1fbd61a9a0a2118285384269461d380d01196d2eacaed1258d3c4bc3d80c97` |
|  `latest`     | May 15th     | `sha256:bda4235f88d74a07a66957157dfa08ec6e1dd93bfed167e139ee8dbcba2c260a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `14.12-dev` `14-dev`             | May 15th     | `sha256:fdd859899755f442151fb10f4b6e499e3f8b78686d1bd279787aa6b54b78ad20` |
|  `latest-dev` `16-dev` `16.3-dev` | May 15th     | `sha256:d3e246be2f2cb92f14f34664e511407e7ed9dcdd371d9ba7892a781dbe85af6e` |
|  `12` `12.19`                     | May 15th     | `sha256:2036239db21edff0b74c8086dd845050a0ca45ff1c94e9baab01711e62d1154e` |
|  `16` `16.3` `latest`             | May 15th     | `sha256:7e6494c109bcfa999db3eb57c66b41a498cbb5797ff86cf93f6d117654d01f18` |
|  `15.7-dev` `15-dev`              | May 15th     | `sha256:9f4c479fd1139ad749f2341e0037d328ba0009f60bcee31db9a2a1222a759712` |
|  `12-dev` `12.19-dev`             | May 15th     | `sha256:48fc22f01a1b69d92e567972e5284eadb6dbb7b92e999dce0188529bc5f94b34` |
|  `15.7` `15`                      | May 15th     | `sha256:bc034527fa334d0d29ee2b6f5a7ced6cde06d8abf67a4898dc2c3b78229aa9b8` |
|  `14` `14.12`                     | May 15th     | `sha256:911ef8f57a575fde5f312db523aa6e4d90d66130c88c6bd8f03291dfc03eb63d` |
|  `13-dev` `13.15-dev`             | May 15th     | `sha256:24cb8ee106e761cfadb8073a29b8c7c145d5db16cd64a1c0f860cdee044f0526` |
|  `13.15` `13`                     | May 15th     | `sha256:a6b7dc47cc7add2f676997a56cf6107dd1cefed7bf5a21a4baa32083d9d3b65c` |
|  `16.2-dev`                       | May 9th      | `sha256:e6df17d553a0e6e85cd0673f383814360fd64ce3f079e272b25b3a61dd9a5a51` |
|  `16.2`                           | May 9th      | `sha256:4063177a3addc5a285a0d0ccb1c695b19892a65a4ac67fc2303720beaa5cad7b` |
|  `13.14-dev`                      | May 6th      | `sha256:8668ca6d658fa902a7e1a08d2a223a706caf315dd243663a754e2fbed5dbaccd` |
|  `14.11`                          | May 6th      | `sha256:a2646e751d83bbc6a98aa1efb90c3da8180cc5a27b921f8bf382ae595721ba77` |
|  `15.6`                           | May 6th      | `sha256:36aa8da71af31de4ae5d6876e1c6dd02e74a9438a5d5867f7b1067173d1bf0f8` |
|  `12.18-dev`                      | May 6th      | `sha256:6be6fa8abd5305b72c639dec0930882614493c3a4b3042a2e7ce7a3bc99890bc` |
|  `13.14`                          | May 6th      | `sha256:fde2688caf5b7269fec75f7204938459c7eaa3b0c4bf3ec68e6f9aa35079e464` |
|  `12.18`                          | May 6th      | `sha256:09671cc440c5046a857d63a4988f74cd070bebc89ed765113d514001f9fc1ad2` |
|  `14.11-dev`                      | May 6th      | `sha256:3b31be9393d356b5813c70b345a086e229ff8e1c432c07f6405d6903caee3922` |
|  `15.6-dev`                       | May 6th      | `sha256:dc213d703c03cb46dae0cb5ede7879c7d335d75c09e4a9120e5e8c83d3138eed` |
|  `15.2`                           | May 13th     | `sha256:9795b38cef6aff459626d2539760a28d82b40e3d54a51616486e9c1ba18594d7` |
|  `14.7`                           | May 13th     | `sha256:d9065435b98504de355decd1d2106e293eab368b170aabf3368950db105d07d6` |
|  `12.14`                          | May 13th     | `sha256:4ee5fcc3d4a5da3f93cb9470280e40ae740fa9248094f7bc32ed6f5af5ea2b42` |
|  `11.19`                          | May 13th     | `sha256:5e105e0a390be47a0f3212b230a9b783a2c4b65dee3f8c9b28440a7e635c9917` |
|  `13.10`                          | May 13th     | `sha256:d8de570577877963d5166d2f9cb85e0c626e6b70e188d63f75fd38be6ac0138c` |

