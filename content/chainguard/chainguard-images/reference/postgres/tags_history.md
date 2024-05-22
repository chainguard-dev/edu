---
title: "postgres Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the postgres Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-22 00:47:17
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
|  `latest-dev` | May 21st     | `sha256:7ea795b8bd80782dc19d2fe6d74c204c89074c22f9df0c0985dfad7ea655e74e` |
|  `latest`     | May 21st     | `sha256:a8331a152fed2cfdfaa52581cfc1bdd168ad357ec9a5810eafc4ad6313bca80f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `15` `15.7`                      | May 21st     | `sha256:4f85f3bd44568998de5f6d426a19d9abba6eb27ece01a4ebc82be0193aef964d` |
|  `16.3-dev` `16-dev` `latest-dev` | May 21st     | `sha256:294c6b2e6ea804e9fd2d453fcd1311ae3c54f10fed6214c503bdc6c6097891b5` |
|  `13.15-dev` `13-dev`             | May 21st     | `sha256:6728d51cd1cd0bfb59e959cd7b095ae7006c62a8df0f5d2c10f3eaee13084645` |
|  `15-dev` `15.7-dev`              | May 21st     | `sha256:41209b0ce9b15d111175bba440e259fabe77b9ee2efc14f8b0d711cdfd2a5746` |
|  `13.15` `13`                     | May 21st     | `sha256:c8a919a755ae6f38bdeeb4f42d22b4db4382038257bc3093bcf94a7a743fbd74` |
|  `14-dev` `14.12-dev`             | May 21st     | `sha256:671d1bbc9aeca4a576cc3f2f6d28cb73f99e4d5b49188608429bdc7d6fbfe535` |
|  `16.3` `16` `latest`             | May 21st     | `sha256:d46ed8a2feeff196f1ecc3212131add5b2e21ef4aa20789cc2a337131653e8c8` |
|  `12-dev` `12.19-dev`             | May 21st     | `sha256:0aca8ac5c5e84fbd2345ca089a3c85accd69169908572b4e2a32cb335ee16c7f` |
|  `12` `12.19`                     | May 21st     | `sha256:ecbdab167ff03bc21fbe688af84c3a9894cc201e2966ef9d1679ba31777d40d3` |
|  `14` `14.12`                     | May 21st     | `sha256:25c88a8d4b8b2eabf71a09a7735140e300aaf41dff505ab51af598fa7d1c6a00` |
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

