---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-03 00:33:11
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
|  `latest` `openjdk-21`         | June 28th    | `sha256:6a07bfa39476a02940a1a2504390640dbd2fb531ae74efc3fbb35a22c500b39d` |
|  `latest-dev` `openjdk-21-dev` | June 28th    | `sha256:c73b56234d5293038d9a08c4ec16188685c4456a0365802543ff9442a9e3a9ce` |
|  `openjdk-11`                  | June 28th    | `sha256:2bd31073d3eef07272fc004278e763ec855dbec5a476e514d54a6bc8fffbc7c7` |
|  `openjdk-17`                  | June 28th    | `sha256:8fa09abcabb2238aec72874452d3ffbd7dc58abfeeffefb49663f8c6e76b19f5` |
|  `openjdk-11-dev`              | June 28th    | `sha256:b17cc299b957ee7132cab21f26cdb71da232e2225f6285a26edd9b5e43850102` |
|  `openjdk-17-dev`              | June 28th    | `sha256:3e5f20d29b709833df7fa2dad98883a96697ce0ea386f6e0e66f2f39e7d4ec72` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-11-3-dev` `openjdk-11-dev` `openjdk-11-3.9.8-dev` `openjdk-11-3.9-dev`              | July 2nd     | `sha256:5c68d19da317e3b60e309a4d5c107d6defc5786070c4c4fea3dc44b3e41fea17` |
|  `openjdk-21-3-dev` `openjdk-21-dev` `latest-dev` `openjdk-21-3.9-dev` `openjdk-21-3.9.8-dev` | July 2nd     | `sha256:7e501e033e15e333efb34ec8d1097b05ce5f90999edfa745a2fcf91ab2e6db12` |
|  `openjdk-11-3.9.8` `openjdk-11-3.9` `openjdk-11-3` `openjdk-11`                              | July 2nd     | `sha256:ef8e9df9343de1927eee5f4de3b7b9e3517243c0adf8c0a612d4a01139595dd7` |
|  `openjdk-21-3` `latest` `openjdk-21-3.9.8` `openjdk-21` `openjdk-21-3.9`                     | July 2nd     | `sha256:2472b8bc9b3da299a60a599cc9a40c98d5153cea79677a4f96cce78fac897cb7` |
|  `openjdk-17-3` `openjdk-17` `openjdk-17-3.9` `openjdk-17-3.9.8`                              | July 2nd     | `sha256:2a9d39175971ff5f72cb577322c71fd47e28a2ca73e360c29b6bc9cc752f5ac9` |
|  `openjdk-17-dev` `openjdk-17-3-dev` `openjdk-17-3.9-dev` `openjdk-17-3.9.8-dev`              | July 2nd     | `sha256:9cff23e5602a9685360f8ceb773b6fea2048bdb493bdfd6aa2fd7dd70a89f283` |

