---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
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
|  `openjdk-21-dev` `latest-dev` | May 15th     | `sha256:3f93aec400bdf5120261508dcfeb709cf750111f266da0b27b334f34432221a8` |
|  `latest` `openjdk-21`         | May 15th     | `sha256:a9cff60b073efce0191b2046f6cc83437ed92d17374c580881bf8b481334ea4b` |
|  `openjdk-17`                  | May 15th     | `sha256:e27642df566decdeec813d1c1bf740814b0a9786af3e6d0d8707e95c964e80d8` |
|  `openjdk-11`                  | May 15th     | `sha256:b5c1b6d5ef6a8fb75ef7f1f6308fc26cff0bfe677f00380300fb99fa3872d3fd` |
|  `openjdk-17-dev`              | May 15th     | `sha256:24e64da067a06706dd4ec76746b98ab8bc9adae125b62b26846f180fdf4d7a1a` |
|  `openjdk-11-dev`              | May 15th     | `sha256:324a8b3ad54985c83d695b79a49a2fe02d43b820f6e752ee29c7113363b683a2` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `openjdk-21-3-dev` `openjdk-21-3.9-dev` `openjdk-21-dev` `openjdk-21-3.9.6-dev` | May 15th     | `sha256:9b5633da5abe93f65095a4d7568b45fba4100af2292398815299b0fc6bcfb19f` |
|  `openjdk-21-3` `latest` `openjdk-21-3.9.6` `openjdk-21` `openjdk-21-3.9`                     | May 15th     | `sha256:3ae710014cea626f412358d9f1984eef5f167a75f44698b620e9bc97eeae7377` |
|  `openjdk-17-3-dev` `openjdk-17-3.9-dev` `openjdk-17-3.9.6-dev` `openjdk-17-dev`              | May 15th     | `sha256:0d600e2c8f305fff0cd82f8ecd399a8991dbcdb1905e4d914a33165b41802341` |
|  `openjdk-11-3.9-dev` `openjdk-11-3.9.6-dev` `openjdk-11-3-dev` `openjdk-11-dev`              | May 15th     | `sha256:5f248c07469d315ef2955359ee911cf2268a06a508ef563b88fde3eec8b8f53e` |
|  `openjdk-11-3.9.6` `openjdk-11-3.9` `openjdk-11-3` `openjdk-11`                              | May 15th     | `sha256:753e82b6fdd23d30b13e21a3b50567355db757ed8889a1e11448962812c41151` |
|  `openjdk-17` `openjdk-17-3.9.6` `openjdk-17-3` `openjdk-17-3.9`                              | May 15th     | `sha256:de35bd55f4e92f7ed2d5da039f82b29f8008a281feaf8c90025c170ffa7f634a` |
|  `openjdk-17-3.9.1`                                                                           | May 13th     | `sha256:0e4eaeb21b03f72e24767d4696b49935cd6b8838852d89e5243ba19fee27afc8` |
|  `openjdk-11-3.9.1`                                                                           | May 13th     | `sha256:617690269a5361add65e7ef9ed24d5daf94300c5728c41d796a92b680d7d5b41` |

