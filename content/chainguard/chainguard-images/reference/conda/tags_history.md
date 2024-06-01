---
title: "conda Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the conda Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-01 00:50:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/conda/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/conda/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/conda/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/conda/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 31st     | `sha256:eb7c78eda8b47a49bd6f5b7c4c824bb3679fc25af32c3f97923344fab8f9f290` |
|  `latest`     | May 31st     | `sha256:ce585ddbf515a72a0ddbabeefbaf4c935b3efc05a2413ae1ce3005ae2bb17cea` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `24` `24.1.2` `24.1`                 | May 30th     | `sha256:9ad4db2199586bc10651ea44eee0a26868f0821cb44ea885cd376ba65fb95e36` |
|  `24-dev` `latest-dev` `24.1-dev` `24.1.2-dev` | May 30th     | `sha256:1bd46374ad7cc7ff5541661d9af01dd0b2ac796ad890e37c722a40a2b75f3933` |
|  `24.1.1`                                      | May 30th     | `sha256:b7052b92716f5fcd65ddc58655be563ed8baaecad7ff85312616004e2cefda94` |
|  `24.5` `24.5.0`                               | May 30th     | `sha256:c9ae1a3d06826f7fef0c17ec9619369d7bd20915c2d3ed76ed589b2d908d8aa1` |
|  `24.5.0-dev` `24.5-dev`                       | May 30th     | `sha256:3ed8ac9247f8e641fac9acf1fbc095913fbb2f1aa79b5f0e5b98da2c29c5853b` |
|  `24.1.1-dev`                                  | May 30th     | `sha256:2cff45b944d94d57811376f53572f784765484b40f0a139cdf25975144e2f0c8` |
|  `24.4.0-dev` `24.4-dev`                       | May 8th      | `sha256:db25b7d5ccc48668c852b24b06922024347fbd1b5fbd4a3c2dbc184f81d5cfa6` |
|  `24.4` `24.4.0`                               | May 8th      | `sha256:12455aac60e4625f73e166b429c3f526ba9e018cc75b7a6339bde4d7b3618fe4` |

