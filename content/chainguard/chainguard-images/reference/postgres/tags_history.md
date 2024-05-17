---
title: "postgres Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the postgres Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-17 00:44:46
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
|  `latest-dev` | May 16th     | `sha256:f64fdf42662b7d325eb2f8e5a95f04030c051a73c912cebd2b52e864b77dbac8` |
|  `latest`     | May 16th     | `sha256:c2e7368c2b232f7451001b90cb2baca9f9b94bdec1cc16ae0ee8ebbbd4dfbe5b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `16.3` `latest` `16`             | May 16th     | `sha256:4ea5965835da410693caa720c9d29703d07b7f5736897eb5a25bf790c9e5d26b` |
|  `15.7` `15`                      | May 16th     | `sha256:08c485c3546399f6ec60b4a4dec261167e146e5c0d6f63439a93047bc28990f5` |
|  `latest-dev` `16-dev` `16.3-dev` | May 16th     | `sha256:48eae08bcc596d7517da9df7ea1a9499ad92bc4aec00a49da2654893a2509b9b` |
|  `13` `13.15`                     | May 16th     | `sha256:d3c1362265de9cae8b1d7b9a2d9fbd399da156a0113a045e617afc204022bb60` |
|  `14.12-dev` `14-dev`             | May 16th     | `sha256:3770ce8db53467f314268ad4f06d81ec32b4ff52f54d782e2bb04f386fdbc628` |
|  `15.7-dev` `15-dev`              | May 16th     | `sha256:7757be9da45cc1a8caccf3287ad0b079c962e3e6b5376e9d545c23de7693ae5c` |
|  `14` `14.12`                     | May 16th     | `sha256:dd15dd224ddc7af0efa9f70fb61804aec3ff8e3e6002cb88a5a0f4fc5544ed9d` |
|  `12-dev` `12.19-dev`             | May 16th     | `sha256:23a6a0cb8c2f5ced36f81f2b93dfea41c3686b75d53ca2933304b2a4fb31908f` |
|  `13.15-dev` `13-dev`             | May 16th     | `sha256:0d50044a5f10d1c74ce44400b348376bdd511ee27d192c49e5511858887fe42c` |
|  `12` `12.19`                     | May 16th     | `sha256:26b61f6d95a300df533ceb4c7194e45bb9b713842283ae8a2e1eb226175dad0a` |
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

