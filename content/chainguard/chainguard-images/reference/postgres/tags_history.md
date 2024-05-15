---
title: "postgres Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the postgres Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-15 00:39:35
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
|  `latest-dev` | May 14th     | `sha256:650bdc6beca6b41b40d6450c525847d93dc2ae0348a011f8548bbfa5d0d8a4cf` |
|  `latest`     | May 13th     | `sha256:d7f40a6ef9d3833f53e09df8b64eee069420bac4e95420d9be996b1086ad4b0a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `15-dev` `15.7-dev`              | May 14th     | `sha256:f9700f6267d37f383c16c70a89ff7110f9dc8cd2f1c6686382368de519d3d329` |
|  `12.19-dev` `12-dev`             | May 14th     | `sha256:308924f303326e26767a6c833a0d80f8d0f9342a0b4d4fe718104d69b94c42d3` |
|  `14-dev` `14.12-dev`             | May 14th     | `sha256:5a733f73bf09bd0168852610ccf4c658ead78287369db32466ba56374ecd499d` |
|  `13.15-dev` `13-dev`             | May 14th     | `sha256:4041c8d105c9430c81a1e543dff54a40488417f1f81395ac608090eb784bbbdf` |
|  `16-dev` `16.3-dev` `latest-dev` | May 14th     | `sha256:cbf1bcabd06fd9f9625a63bf15b5bd40dc3b5adbd76cadcce59de0cefdf8f7aa` |
|  `15` `15.7`                      | May 13th     | `sha256:43c255a773c8ea07f9be98438f6881da36ac5f3a86c195972bee8ee7e09004fa` |
|  `14.12` `14`                     | May 13th     | `sha256:c1bd8730f6bb1741829c75e36bea206426a54f5d6b68f5a59c731a8822f3ad30` |
|  `13.15` `13`                     | May 13th     | `sha256:047ebcad29113562d96b22cf68ff9e0051683ca4437c0d1e7928ea345ff73b5e` |
|  `16.3` `latest` `16`             | May 13th     | `sha256:ed00b061d3a9591f68e25b12df1cacd2234124bfd54486073ed59856eb2401e6` |
|  `12.19` `12`                     | May 13th     | `sha256:524723b972e6d7fde95f799e4612abd1aa2cb3195317020eb49b7636f0a86f01` |
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

