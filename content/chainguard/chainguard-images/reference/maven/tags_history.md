---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-11 00:54:43
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
|  `openjdk-21-dev` `latest-dev` | April 9th    | `sha256:7095f3ddaa3987e67484dc5e4e04999b13da88bc908d6e44b567804b20207151` |
|  `openjdk-11`                  | April 9th    | `sha256:d9cf83d8e229dbdcbb419af03bf71a17b8575128db0713c29cabc816d976b2d7` |
|  `latest` `openjdk-21`         | April 9th    | `sha256:025b1cc7a4af0633d897ed6548e8512c8330a34bbb83401ec465d72fdd604068` |
|  `openjdk-17-dev`              | April 9th    | `sha256:cd8d415996339a61ccd37a7d2d4ea713dea8033b34d1485e05b6268f539cb7f9` |
|  `openjdk-11-dev`              | April 9th    | `sha256:9f7bc85ee726d923464161627bbb46065c7e6c31ab7ac2e91562257a2a62830f` |
|  `openjdk-17`                  | April 9th    | `sha256:d527d779687d72c085fc32f857ee87affa82929117fad8cd451ba5b3ace65cb7` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-17` `openjdk-17-3.9` `openjdk-17-3` `openjdk-17-3.9.6`                              | April 9th    | `sha256:183e2b34911c172821ce47ef5a608792f45dbf28a9cf878fe120dbf4cef9660e` |
|  `openjdk-11-3.9.6-dev` `openjdk-11-3.9-dev` `openjdk-11-dev` `openjdk-11-3-dev`              | April 9th    | `sha256:8113ea192013a3841ae2e6234e1de4c70badecdeccf7001c80692b26db8b5837` |
|  `openjdk-21-3.9` `openjdk-21` `openjdk-21-3.9.6` `openjdk-21-3` `latest`                     | April 9th    | `sha256:cc14d18ca270d3dc7f6f9812b5e30245859a5d3934d8866eedea5954c3793550` |
|  `openjdk-17-3-dev` `openjdk-17-3.9.6-dev` `openjdk-17-dev` `openjdk-17-3.9-dev`              | April 9th    | `sha256:7a26e0a8990178ef24f71b9e10b2b11ff1b89168c094f5d45ec994f92820d6ef` |
|  `latest-dev` `openjdk-21-dev` `openjdk-21-3-dev` `openjdk-21-3.9-dev` `openjdk-21-3.9.6-dev` | April 9th    | `sha256:cf1af87142f709b540f742d4443cb1e0ca96a56ec8e01e571a349bfc26ee353c` |
|  `openjdk-11-3.9.6` `openjdk-11` `openjdk-11-3.9` `openjdk-11-3`                              | April 9th    | `sha256:972b63056d16cf55a0d1b0e4a741e88b045f673df157b4f96f9e9d795f7bc3f8` |

