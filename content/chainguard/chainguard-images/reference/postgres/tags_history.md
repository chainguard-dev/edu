---
title: "postgres Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the postgres Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-31 00:48:45
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
|  `latest`     | May 30th     | `sha256:f359eed58238db0c9dc24b791e11b197e997e799eb42455f31099fc1492617e7` |
|  `latest-dev` | May 24th     | `sha256:a2771acf2b1ba976ef488dc8dd642195030d36a9a87272d967dc8927922807d9` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `12-dev` `12.19-dev`             | May 30th     | `sha256:af5f3d306e9ea4f912258655051311a95abeeef556ad59de023748a028f1a49d` |
|  `12.19` `12`                     | May 30th     | `sha256:05ff4933a194712d40b544c56d2ddb9f2038c2f60bfd8a6be4bf4bc2922146a1` |
|  `13.15-dev` `13-dev`             | May 30th     | `sha256:aabb48a58b3d14ef253a4f91119646664850ca48969cbd805b28d6160cd9c2bd` |
|  `14.12` `14`                     | May 30th     | `sha256:d438e39d8310017460fb088c46303fd23e1eec9c62b0a4676c8a774a4414fecb` |
|  `15.7` `15`                      | May 30th     | `sha256:c0130f531d2892a1a1cdbb57d52cb119acb01d737083780df25a9242464e3fe2` |
|  `latest` `16.3` `16`             | May 30th     | `sha256:301cb508dcbaa3f6d36b9da3bd132a91af1e82be0d58a3823f74863d70645f9b` |
|  `13` `13.15`                     | May 30th     | `sha256:44c955b2dd056bcc1d94e8178527cad010d71a23451a93cdd2cc0f28b7a78534` |
|  `14-dev` `14.12-dev`             | May 30th     | `sha256:e528ad869552616be7ad8008c68b0f6eec42843137cd34777de9e7fdb2302044` |
|  `16-dev` `16.3-dev` `latest-dev` | May 30th     | `sha256:83d09693cf19dc27fec9f7aebb2979bd3dbae5e1669104c7eaaf56ccdad357ac` |
|  `15.7-dev` `15-dev`              | May 30th     | `sha256:7960d826c4a0418a8d8dc950ebe68bd75684b00639e0deaac4eedc738ce6a1b4` |
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

