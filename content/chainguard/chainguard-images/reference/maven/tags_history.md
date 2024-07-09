---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
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
|  `openjdk-11-dev`              | July 8th     | `sha256:06d4d446049f3fbbb61faeb8360e77c38d5f42577d6bcf36edd040bfcb5497e7` |
|  `latest` `openjdk-21`         | July 8th     | `sha256:a5518fb10906ff3cbd87e191504bd9e753d7272811e287e10fe8da99bcf5b774` |
|  `latest-dev` `openjdk-21-dev` | July 8th     | `sha256:52d94799f5451cff5cc821018a9d4877eb98e6ed6f4ffe962b59dbf5f0d548b7` |
|  `openjdk-11`                  | July 8th     | `sha256:7dc0364a1091a4ca32a0cdcdb94f381681215e7601cc324aa79a526571c72201` |
|  `openjdk-17`                  | July 8th     | `sha256:e4dc039fc307dcc11223859c403149b18116bf5bc625316ad3d735e2e76196f0` |
|  `openjdk-17-dev`              | July 8th     | `sha256:87f09428806fc16567569c053e1296d3dc6d6675aab0e477c4377a95d1c117a6` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-11-3-dev` `openjdk-11-3.9-dev` `openjdk-11-dev` `openjdk-11-3.9.8-dev`              | July 8th     | `sha256:51a2424c22965778ab74c7fc1d92c06b8fe8fcf821491cb6d2803914911e1f66` |
|  `openjdk-21-3.9.8-dev` `openjdk-21-3-dev` `openjdk-21-3.9-dev` `latest-dev` `openjdk-21-dev` | July 8th     | `sha256:acf73119d99b51665544685fc606fda58be62651a330a4cf23371415cfef2c75` |
|  `openjdk-17-3-dev` `openjdk-17-3.9.8-dev` `openjdk-17-3.9-dev` `openjdk-17-dev`              | July 8th     | `sha256:f25369edd5b9b6591a599cb69dea8efef03d4011d13048fb8707df9153da2c72` |
|  `openjdk-17-3.9.8` `openjdk-17-3` `openjdk-17` `openjdk-17-3.9`                              | July 8th     | `sha256:7e15eb27c83845305e9ae1f8fce673e0bc9b8d3b14e324210a0c1696bb9d1595` |
|  `openjdk-11-3.9` `openjdk-11-3.9.8` `openjdk-11-3` `openjdk-11`                              | July 8th     | `sha256:da18722680e885a48799c1e2238e9301fa85579beaa8978ecd38ab7f66d3f216` |
|  `openjdk-21` `latest` `openjdk-21-3` `openjdk-21-3.9.8` `openjdk-21-3.9`                     | July 8th     | `sha256:28ade75b1646e568d6330d489a53377706fb0d9d4ca9279e395484aa521e507e` |

