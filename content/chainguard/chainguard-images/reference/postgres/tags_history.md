---
title: "postgres Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the postgres Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-14 00:37:02
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
|  `latest-dev` | March 13th   | `sha256:d21c4f48f7e694ee27784720964b7b89df0694eded55379744187dc05645bbce` |
|  `latest`     | March 11th   | `sha256:dc1f72cbda4b41ee3838171da57eb98cfa7fbcd90bc81611dae5996b757793e4` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `12.18-dev` `12-dev`             | March 13th   | `sha256:c0de54c06b2c7f23a26f6a881e4ddf4b7009551ee3a9f33f638b4fc85483f440` |
|  `13-dev` `13.14-dev`             | March 13th   | `sha256:be6ca6f9b1eb67640176d10ee0dafd1b95fa357b591111c30fb20ad10b810243` |
|  `latest-dev` `16.2-dev` `16-dev` | March 13th   | `sha256:1d69912818b340e5ce619d14e7d908f460b8688cf7dce8f84d2f8b1119710dd3` |
|  `15-dev` `15.6-dev`              | March 13th   | `sha256:23c3d0e342a1418dbad0a6a4e1b4da90019698fef184353ed5c2094cba065ba0` |
|  `14.11-dev` `14-dev`             | March 13th   | `sha256:8353a6fd1cea3d519b2e645acbd8ddb8a041294d7847681c35bdd16e309a698c` |
|  `13` `13.14`                     | March 11th   | `sha256:ed923024cf11fc255806a6135471d434257cd6e75da01cbf3c61ccf698901d84` |
|  `14.11` `14`                     | March 11th   | `sha256:67cc765191d181464a5e99749f64a8a173d7e712f6c2863fbb921720320871f0` |
|  `16.2` `latest` `16`             | March 11th   | `sha256:7b8598b3407682b73a83a7939519cbece600bc5a0464999922c979e10ee9eb3a` |
|  `12.18` `12`                     | March 11th   | `sha256:b0702a119ef9b102ff7be142e21240df1be8dca14eadc2bd5e1bfaa60e11d777` |
|  `15` `15.6`                      | March 11th   | `sha256:bce7e3598948493d1b0044c1aabf0de8464182a72777c2c59f044b1887748cdc` |

