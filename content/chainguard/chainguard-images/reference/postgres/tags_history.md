---
title: "postgres Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the postgres Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-13 00:45:28
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
|  `latest-dev` | May 9th      | `sha256:9cba2e8decebdd011b4492e4399848d0aed78158c38781402451f5ba0a42b153` |
|  `latest`     | May 9th      | `sha256:368a963066e2c7e2d7643818d3f2e6bc70a332ad739713aa3bab05652c78bff9` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `13-dev` `13.15-dev`             | May 11th     | `sha256:17cb8ace62cb3b577d1c7a4647937a79d3a64cb9613065cd220717dcd481cbc5` |
|  `13` `13.15`                     | May 11th     | `sha256:b7b28ee79715b6d9e8d65d6350c3075688c454fb459813685b0a08e92ef457d8` |
|  `15.7-dev` `15-dev`              | May 11th     | `sha256:fac9ade8c688eb378a8fd3b6dcdf910e551c34bf70c79f1cc303139d1a22992e` |
|  `12` `12.19`                     | May 11th     | `sha256:ff7a6b3974fd101ae004bbc7785c0aa877432d343a8925015b7ea49f0b0f2a29` |
|  `15.7` `15`                      | May 11th     | `sha256:4abc4369d6ab1434908fdbcca10a4a2583d247b7907335d47e3d9666fdc9939f` |
|  `14` `14.12`                     | May 11th     | `sha256:6f7c5d1d9de6d5981b07ed49a8a86f78eaca44940faed1b18b908a2bb30ea076` |
|  `12-dev` `12.19-dev`             | May 11th     | `sha256:140b54cb2e26dbfc3e9e22699a57d63090f705a836185487889c3c74d82aa7e6` |
|  `14-dev` `14.12-dev`             | May 11th     | `sha256:5dca4be3a371057545e3ac42a7d41c7c48e07d676bd6ec4a1f9b965c29340180` |
|  `16` `latest` `16.3`             | May 9th      | `sha256:70633a56e1713be814ffb698855c7375a1010cbbf4bca852c5592b692cd8ebcf` |
|  `16.3-dev` `16-dev` `latest-dev` | May 9th      | `sha256:90b9ec9af0b91fb3c27e2859246718b2937bf72d2c54e0c4aa06d7da2b31f8e8` |
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
|  `14.7`                           | May 13th     | `sha256:d9065435b98504de355decd1d2106e293eab368b170aabf3368950db105d07d6` |
|  `12.14`                          | May 13th     | `sha256:4ee5fcc3d4a5da3f93cb9470280e40ae740fa9248094f7bc32ed6f5af5ea2b42` |
|  `11.19`                          | May 13th     | `sha256:5e105e0a390be47a0f3212b230a9b783a2c4b65dee3f8c9b28440a7e635c9917` |
|  `13.10`                          | May 13th     | `sha256:d8de570577877963d5166d2f9cb85e0c626e6b70e188d63f75fd38be6ac0138c` |

