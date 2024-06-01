---
title: "postgres Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the postgres Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-01 00:50:07
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
|  `latest-dev` | May 31st     | `sha256:b7221691f42e30b51b55340c4d4e4582e2d14980404e81dcd1fd99d603caae5c` |
|  `latest`     | May 30th     | `sha256:f359eed58238db0c9dc24b791e11b197e997e799eb42455f31099fc1492617e7` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `14.12` `14`                     | May 31st     | `sha256:fe6b82a1ccf0aadadff98cde9a1412cef34ea42ddac2e79d139b9998201b60c0` |
|  `12` `12.19`                     | May 31st     | `sha256:9249fa250c7b0db868526fe54f6bea67724af3f8f08eb518a0324a503add77b2` |
|  `13.15-dev` `13-dev`             | May 31st     | `sha256:46fa3d12b219820ee2288e820d853c3ac84732add06e5a680afa9c3e0ae33662` |
|  `15.7-dev` `15-dev`              | May 31st     | `sha256:de1c5820063dd12e45c706ab73bac5a4249fb82eff9d1e260c52bff4e461e1bd` |
|  `15.7` `15`                      | May 31st     | `sha256:75b9bc83c130e0887718b511812345c560b112b5f142bb4b4e76d235f298248c` |
|  `14.12-dev` `14-dev`             | May 31st     | `sha256:30adba536d7cc5cf36f2a0b273fee30d83ed96992ed0501faf03d6051e10ad79` |
|  `13.15` `13`                     | May 31st     | `sha256:9eaeab77ae2200dae91bc2653c24c5271062a9804a5c045b1f1a7a8fa6777419` |
|  `12.19-dev` `12-dev`             | May 31st     | `sha256:2f3445bdd57587528e4d52f1cca456d4265ff87250e6418511cccf1ba443e5ad` |
|  `latest` `16.3` `16`             | May 30th     | `sha256:301cb508dcbaa3f6d36b9da3bd132a91af1e82be0d58a3823f74863d70645f9b` |
|  `16-dev` `16.3-dev` `latest-dev` | May 30th     | `sha256:83d09693cf19dc27fec9f7aebb2979bd3dbae5e1669104c7eaaf56ccdad357ac` |
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

