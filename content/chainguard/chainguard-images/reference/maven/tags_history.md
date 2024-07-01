---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-01 00:36:20
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
|  `openjdk-21` `openjdk-21-3.9.8` `openjdk-21-3.9` `openjdk-21-3` `latest`                     | June 28th    | `sha256:1fbefb887f26459aa5719b3efe6483bf73d5b70a116096157c8540ad0bc0ee05` |
|  `openjdk-17-3` `openjdk-17` `openjdk-17-3.9` `openjdk-17-3.9.8`                              | June 28th    | `sha256:10f363891c821a720b6970c2c98cbe8b0c22af97d4b2b70f676c2fb0ae863848` |
|  `openjdk-21-3.9-dev` `openjdk-21-3-dev` `latest-dev` `openjdk-21-3.9.8-dev` `openjdk-21-dev` | June 28th    | `sha256:4788e91ba9ff3d956a4e350786c15c46ed33a62d88029ca3f7885a8c6c18cf55` |
|  `openjdk-11-3.9.8-dev` `openjdk-11-3.9-dev` `openjdk-11-3-dev` `openjdk-11-dev`              | June 28th    | `sha256:2f477b23804f339622f5a35822ee6856936b1ac1c5e95e2bec069973a6b452bc` |
|  `openjdk-11` `openjdk-11-3` `openjdk-11-3.9` `openjdk-11-3.9.8`                              | June 28th    | `sha256:7af7d6cd541180f9d26e2795b91fd05c8dee9cc558d3823a1daf9161025e32a5` |
|  `openjdk-17-3.9.8-dev` `openjdk-17-3.9-dev` `openjdk-17-3-dev` `openjdk-17-dev`              | June 28th    | `sha256:1404915094d6b8b14c9d01177bd639f8fbcbff094d6e9f312fbb5b444cc6f709` |

