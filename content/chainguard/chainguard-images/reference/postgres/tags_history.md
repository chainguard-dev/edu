---
title: "postgres Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the postgres Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-13 00:52:18
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
|  `latest-dev` | March 12th   | `sha256:471bc26d4a48bbe4a0f00689914a4756c14e0560536d88347cd31386fefce991` |
|  `latest`     | March 11th   | `sha256:dc1f72cbda4b41ee3838171da57eb98cfa7fbcd90bc81611dae5996b757793e4` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `13-dev` `13.14-dev`             | March 12th   | `sha256:af7b2954b7f426d0a1b91971e6549544e183dade7f29f28e25e10c32a698cdad` |
|  `12.18-dev` `12-dev`             | March 12th   | `sha256:9d9b132c1e6d4c1082812b59d5fd05fef38c435e33e5cbdf86dc304597902472` |
|  `15.6-dev` `15-dev`              | March 12th   | `sha256:24eccaac2598c9a902e6bc47039742145cae32036a1ba697ff988a65013589f0` |
|  `16-dev` `16.2-dev` `latest-dev` | March 12th   | `sha256:41cc56c4f5a67040443bebc145601165cabf9fee79f0fe7814814663bcad42c2` |
|  `14-dev` `14.11-dev`             | March 12th   | `sha256:c8ff831269d3ea39ee23cd88f9b53c6d31ef6ada4cfc8e95dac6d46760e5a553` |
|  `13` `13.14`                     | March 11th   | `sha256:ed923024cf11fc255806a6135471d434257cd6e75da01cbf3c61ccf698901d84` |
|  `14.11` `14`                     | March 11th   | `sha256:67cc765191d181464a5e99749f64a8a173d7e712f6c2863fbb921720320871f0` |
|  `16.2` `latest` `16`             | March 11th   | `sha256:7b8598b3407682b73a83a7939519cbece600bc5a0464999922c979e10ee9eb3a` |
|  `12.18` `12`                     | March 11th   | `sha256:b0702a119ef9b102ff7be142e21240df1be8dca14eadc2bd5e1bfaa60e11d777` |
|  `15` `15.6`                      | March 11th   | `sha256:bce7e3598948493d1b0044c1aabf0de8464182a72777c2c59f044b1887748cdc` |

