---
title: "postgres Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the postgres Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-21 00:38:36
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
|  `latest-dev` | May 20th     | `sha256:d2907aa52c9cdef167e4c73a49467d606e5d31135e7eedd4f191d07003483de6` |
|  `latest`     | May 17th     | `sha256:0636be0b1d05d0895db7f3b9e5005d26929de52f9457ba4b59eb8184f78fcd2b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `14-dev` `14.12-dev`             | May 19th     | `sha256:7d6ca487819219850993379c4247f81c6deab822bf88e4077b611f2958e6461f` |
|  `13.15-dev` `13-dev`             | May 19th     | `sha256:836a9a69ff900152b6f117b86c75d4d3a3408b735e512dd6d84228600d2de5b5` |
|  `latest-dev` `16.3-dev` `16-dev` | May 19th     | `sha256:1c170c4368b75beabe1c8ac80e59678da8b6b88ba0c1b407b52d6f55fafd850b` |
|  `12.19-dev` `12-dev`             | May 19th     | `sha256:9fb188551f36ad3dddb0d73f3a4cd2d17e6febff3cbfbd8d9d435b690d0108a5` |
|  `15.7-dev` `15-dev`              | May 19th     | `sha256:5ccc8d301ba208a1912bff2a7b68466fd33cc2a1b56d5f18599216ac54109234` |
|  `latest` `16.3` `16`             | May 17th     | `sha256:1b8df8d0d0b5e71933c6626cb8b3aef982274aa438b40b02148d45edc51489c8` |
|  `15` `15.7`                      | May 17th     | `sha256:50313ec21aed53f638e3d9bfab25591d0090ab214cb0b4700270b50606d9885f` |
|  `13.15` `13`                     | May 17th     | `sha256:caf6fd95afe47095e2b748e70e94ecc22470971bf8a8363bf46204053985f7e4` |
|  `14` `14.12`                     | May 17th     | `sha256:1d6b3bde5fb281fa0e5276dc5b9b8ee7fee78da63a10b7f1189ccd6274bd4765` |
|  `12.19` `12`                     | May 17th     | `sha256:5d8f0b23f1505fe7505ffb80b2d994e3576c67c4f54b986d9f7f2997fb92dce2` |
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

