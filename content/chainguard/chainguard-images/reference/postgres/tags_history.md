---
title: "postgres Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the postgres Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-24 00:45:45
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
|  `latest`     | May 23rd     | `sha256:3c2b73d9c533410c5d22ce6a37007694475a929a398abedc68a18ae119d6f27f` |
|  `latest-dev` | May 23rd     | `sha256:489c8d583fa9b922281af5d190a273ee140b7624f42c05b04d3c5756d1885bf2` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `12.19-dev` `12-dev`             | May 23rd     | `sha256:a9ecc1e86bc24dbb1f0dd7b23741477ef76da5e79bfb7a10afba5665d20013ec` |
|  `13.15-dev` `13-dev`             | May 23rd     | `sha256:241c7ce543560dd65a9b2626e02d83ca8f03e26e43052501c503762dd6fa06f8` |
|  `16-dev` `16.3-dev` `latest-dev` | May 23rd     | `sha256:79b601c61114e05e56410d3d9e2e5c8c05f173206b3b9ca445dbc30c3968d7a5` |
|  `14.12-dev` `14-dev`             | May 23rd     | `sha256:13fb5175032411e2fe7baf623cc45f4a7d5d778f2f52eaee12397f4052fec1aa` |
|  `15-dev` `15.7-dev`              | May 23rd     | `sha256:0d997f6ec044841765024ff22f99f924a369c38e9568459be3be5b36c00f6be7` |
|  `14` `14.12`                     | May 23rd     | `sha256:a8a66ccd697f43869a50b8bd1c308a583c510113cba86f87457a58c1d14981de` |
|  `12.19` `12`                     | May 23rd     | `sha256:304f540e61f76b87d5600150846af708f0dda0ea213a0729f76597288626366a` |
|  `13.15` `13`                     | May 23rd     | `sha256:739747ae8269e0f61fc433d768430be2f14a1dadc5297072226b06f65e7d75c3` |
|  `16` `latest` `16.3`             | May 23rd     | `sha256:c6ffe519d36b9e2d19cf9f4e26d7f2753a2154d53604fcccd26a3636fe87528a` |
|  `15.7` `15`                      | May 23rd     | `sha256:98f74b58096fe8192c78c2fd18c101574fac0538baed938f6f0ccb191abeaaf6` |
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

