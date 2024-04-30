---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-30 00:52:22
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
|  `openjdk-21-dev` `latest-dev` | April 29th   | `sha256:c7f7a8af2827724e68d379c6b12733bf2c9727d91571245ab6720a314692bd42` |
|  `openjdk-17-dev`              | April 29th   | `sha256:b2137de322c0af3d1e7b868d5489c1ebd87bfadecfdaf05c26d713231d327467` |
|  `openjdk-11-dev`              | April 29th   | `sha256:fddb096c7a0040438ebe0bcab3092dc7db16c07255a91cd98609c158eb55f005` |
|  `openjdk-17`                  | April 22nd   | `sha256:0a40c03cb1b5af84d83823b4a8161b38dff49c25477db026217580be8947d8d8` |
|  `latest` `openjdk-21`         | April 22nd   | `sha256:853cf8c52000fb11414596ec76d6829ab74ec830095bee212f2e4568c66ad405` |
|  `openjdk-11`                  | April 22nd   | `sha256:25694fbf5ed0c5070fee70b2b7659edb8c443c788b54a32d0e41bb726e0f4faa` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-17-3-dev` `openjdk-17-3.9.6-dev` `openjdk-17-dev` `openjdk-17-3.9-dev`              | April 29th   | `sha256:39e16a75c565f28793ff00db0c86bb799303e902975f4a1b1c704e6d52ad0168` |
|  `openjdk-11-dev` `openjdk-11-3-dev` `openjdk-11-3.9.6-dev` `openjdk-11-3.9-dev`              | April 29th   | `sha256:d42dec13ee23f59c4329788a73461d87453c9a8995a00f92029e210b6865ac83` |
|  `openjdk-21-dev` `latest-dev` `openjdk-21-3-dev` `openjdk-21-3.9.6-dev` `openjdk-21-3.9-dev` | April 29th   | `sha256:4ac2b6176f090ffe7fda04d508312e19b12c507f38cc691a8af25e2f2f7309c0` |
|  `openjdk-17` `openjdk-17-3` `openjdk-17-3.9.6` `openjdk-17-3.9`                              | April 21st   | `sha256:aac68dbe428a6bfb05c0ba2e15fb13716eac1a41ee69097c714a680dd0b61b2b` |
|  `openjdk-21-3.9` `openjdk-21-3.9.6` `latest` `openjdk-21` `openjdk-21-3`                     | April 21st   | `sha256:1af4b84f007e70f71eb2226dfd88562a906791f4d3499f2ece226ed4d3960f60` |
|  `openjdk-11` `openjdk-11-3.9` `openjdk-11-3.9.6` `openjdk-11-3`                              | April 21st   | `sha256:37a412c1bbeb3dc771282793f8fec723bc61ef77fc703b3510d7419b629d6aca` |

