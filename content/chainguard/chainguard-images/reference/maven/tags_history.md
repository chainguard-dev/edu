---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-22 00:47:17
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/maven/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/maven/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/maven/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/maven/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                        | Last Changed | Digest                                                                    |
|--------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-17-dev`              | May 21st     | `sha256:9a57603960890847c84b7df663d0beec8b21e55a62c1093e4695f35216b24145` |
|  `openjdk-11-dev`              | May 21st     | `sha256:4799ba5b00900c044d09cdb4bed48aa397f4f772e463fdcca3d34e9193bc1153` |
|  `openjdk-21` `latest`         | May 21st     | `sha256:5868223e330189e6b703a52a9dd2f4de17b302eddf624dd4071cfbd70338bb42` |
|  `latest-dev` `openjdk-21-dev` | May 21st     | `sha256:65456b136bbe43e1ee98928516cdfc08b5d59737c6f48ad88b45589c48dd6212` |
|  `openjdk-17`                  | May 21st     | `sha256:d636dea545757e943036dd6ce06a83de2acdfdbec8d8b7399012273ffafcc7e9` |
|  `openjdk-11`                  | May 21st     | `sha256:82d7f8f29580bf81eaba3da7071c85cc1692830e4606a0287876a0f1253687e1` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-21-3-dev` `openjdk-21-3.9-dev` `openjdk-21-3.9.6-dev` `openjdk-21-dev` `latest-dev` | May 21st     | `sha256:ac539573227fe4dbe49c875f4bc0bacb509cda4fc637ffb19ebe8ebb03e2edcb` |
|  `openjdk-11` `openjdk-11-3.9.6` `openjdk-11-3.9` `openjdk-11-3`                              | May 21st     | `sha256:fd65f58309acdf6a1c1589a65b486e6250ff2a4f152f2f96edfdc3d39636f46d` |
|  `openjdk-17-3.9-dev` `openjdk-17-3.9.6-dev` `openjdk-17-3-dev` `openjdk-17-dev`              | May 21st     | `sha256:dfa30c385b9504fa2eb1c9c9337282f1802dc78a5f209d501e9c3a7e0e0d4a2d` |
|  `openjdk-11-dev` `openjdk-11-3.9-dev` `openjdk-11-3-dev` `openjdk-11-3.9.6-dev`              | May 21st     | `sha256:ab9140cb365346210b2c97ac2313dd36e04083982584e86428b64782c2099d40` |
|  `openjdk-21` `openjdk-21-3.9.6` `openjdk-21-3.9` `openjdk-21-3` `latest`                     | May 21st     | `sha256:83b04edf95dc9d4d81c6fbd26e8467fdf6db021d84fbdb4cf53bc2440a84e540` |
|  `openjdk-17-3.9.6` `openjdk-17-3.9` `openjdk-17` `openjdk-17-3`                              | May 21st     | `sha256:0746cf73a41f49e4dab4b44bee0736879413686bde6e9c86bdcf13cdc4431fca` |
|  `openjdk-17-3.9.1`                                                                           | May 13th     | `sha256:0e4eaeb21b03f72e24767d4696b49935cd6b8838852d89e5243ba19fee27afc8` |
|  `openjdk-11-3.9.1`                                                                           | May 13th     | `sha256:617690269a5361add65e7ef9ed24d5daf94300c5728c41d796a92b680d7d5b41` |

