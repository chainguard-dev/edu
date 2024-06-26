---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-26 00:35:03
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jre/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jre/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jre/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jre/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | June 25th    | `sha256:3b1e56e6a39f7b83f2d099f236e9cdd0fc99af733ef8a3d93ae8a7940d6cf30d` |
|  `latest-dev` | June 25th    | `sha256:e35cd1210bfaa72de0c265f896c97bfb738842f51a2dee49035cc7cc440d2c83` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `openjdk-22.0.1-dev` `openjdk-22-dev` `openjdk-22.0-dev`             | June 25th    | `sha256:b8052fa7f185967d498b9b4f20e993a6d1657f911ddb670cf333b0c4370e9425` |
|  `openjdk-14.0.2-dev` `openjdk-14-dev` `openjdk-14.0-dev` `openjdk-14.0.2.12-dev`  | June 25th    | `sha256:02b659d08567c538110f09778acb2d1250f3bc5665f5f33958f4afb690b79123` |
|  `openjdk-17-dev` `openjdk-17.0-dev` `openjdk-17.0.11-dev`                         | June 25th    | `sha256:e7c712e3de7e0a790e4bed12eb360fc195dba13aae284bbe42181eaa30fa1e03` |
|  `openjdk-21.0.3-dev` `openjdk-21-dev` `openjdk-21.0-dev`                          | June 25th    | `sha256:a0c5b35e455d08e8d899d2addbbda4ac663efa4e8e9dff48b51c3671825c2e53` |
|  `openjdk-16.0.2-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0-dev` `openjdk-16-dev`   | June 25th    | `sha256:fed145529258fd2b3c309b2097fdf7b5adb84bce3e66754b115f6af1dbc9dce0` |
|  `openjdk-8.412.08-dev` `openjdk-8.412-dev` `openjdk-8-dev`                        | June 25th    | `sha256:1c5015df7b797e25c18439c5b3dc5e59d254d5925300bdfde9dfd486674601bd` |
|  `openjdk-11-dev` `openjdk-11.0.23-dev` `openjdk-11.0-dev`                         | June 25th    | `sha256:c7e704a2a005440f0b100f5c3fabb7f6d6137af11b5b075b0643d647eca01a14` |
|  `openjdk-15-dev` `openjdk-15.0.10-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0-dev` | June 25th    | `sha256:c401199cfbee03cfe697caf057dacb6fd3ef155f9e02286d2587c66c41de7d25` |
|  `openjdk-8.412` `openjdk-8` `openjdk-8.412.08`                                    | June 24th    | `sha256:760eee089a5a457286c86c9d0978ef387d8505ae0c48c3e4e8a446a8c5a0da63` |
|  `openjdk-22.0` `openjdk-22.0.1` `openjdk-22` `latest`                             | June 24th    | `sha256:1b96694e2410033be933819340a5fab4a6ef2ea14be7e1020210fb7018880fde` |
|  `openjdk-21` `openjdk-21.0.3` `openjdk-21.0`                                      | June 24th    | `sha256:6dc794bf3e573d80c42c87e6806ad4311ecb3b2411c53487ebef2762c89029fb` |
|  `openjdk-14.0` `openjdk-14.0.2.12` `openjdk-14` `openjdk-14.0.2`                  | June 21st    | `sha256:82b80dcfc13d06d1993e65b5a70607a36cba6a89c81b72125527e75ed2908ba2` |
|  `openjdk-15.0.10.5` `openjdk-15.0` `openjdk-15` `openjdk-15.0.10`                 | June 21st    | `sha256:42c8eb7e2af013209a60a7790a9f0172ac9b5c840eebfc43f7dcadda6efa9f53` |
|  `openjdk-17.0.11` `openjdk-17` `openjdk-17.0`                                     | June 21st    | `sha256:7512f448eeac1db9b60bafa33b34723ba2f0dfc2057fd884a1de238f43147875` |
|  `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16` `openjdk-16.0`                   | June 21st    | `sha256:ce37fa61a748b8e3eabf9573c5f4fffd18d0e9eb42a215be896aa0d516eb2c3c` |
|  `openjdk-11` `openjdk-11.0` `openjdk-11.0.23`                                     | June 21st    | `sha256:15cc64da72bd170da9338e3c33d16f40d1e7e4be6cc9149222afd4e672e1cadb` |

