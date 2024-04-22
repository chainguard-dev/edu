---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-22 00:45:38
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
|  `latest-dev` `openjdk-21-dev` | April 21st   | `sha256:75abac26f050a64396f03e2f31bc707ea0ac3eb85cd37b192a8e4ebfd5fc2c65` |
|  `openjdk-17-dev`              | April 21st   | `sha256:340b69e18874e7962c0787c05e321ec786378a3d167eb84e3b9fa257253a31e1` |
|  `openjdk-11-dev`              | April 21st   | `sha256:7c5b1591b6eaccdafa8b9ead12314357bd201190ba2478a36b0d631af99548fe` |
|  `latest` `openjdk-21`         | April 17th   | `sha256:3c0e7ca99ef5f1f8473328c711884eacbdee87fc1adab6d14ee7d42c0ab448d9` |
|  `openjdk-11`                  | April 17th   | `sha256:f060dda1205baece2f31e0e2d61018b78aefcda950a51571726956b5612ae2af` |
|  `openjdk-17`                  | April 17th   | `sha256:068be81a074f98947a962efb5735f45dd175a0b6f03e67372857fbbe969ba8b9` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-17` `openjdk-17-3` `openjdk-17-3.9.6` `openjdk-17-3.9`                              | April 21st   | `sha256:aac68dbe428a6bfb05c0ba2e15fb13716eac1a41ee69097c714a680dd0b61b2b` |
|  `openjdk-21-3.9` `openjdk-21-3.9.6` `latest` `openjdk-21` `openjdk-21-3`                     | April 21st   | `sha256:1af4b84f007e70f71eb2226dfd88562a906791f4d3499f2ece226ed4d3960f60` |
|  `openjdk-17-3.9-dev` `openjdk-17-3-dev` `openjdk-17-3.9.6-dev` `openjdk-17-dev`              | April 21st   | `sha256:963f32e70b58322c855fc7db61b1128ac60b4332885ae2a52fdd7b1d2dc69f2d` |
|  `openjdk-11` `openjdk-11-3.9` `openjdk-11-3.9.6` `openjdk-11-3`                              | April 21st   | `sha256:37a412c1bbeb3dc771282793f8fec723bc61ef77fc703b3510d7419b629d6aca` |
|  `openjdk-11-3.9-dev` `openjdk-11-3-dev` `openjdk-11-dev` `openjdk-11-3.9.6-dev`              | April 21st   | `sha256:2900cbe379a98d9083752781be1bb6806869bdffa33f93ddcd921a044ca939ed` |
|  `openjdk-21-3-dev` `openjdk-21-dev` `latest-dev` `openjdk-21-3.9-dev` `openjdk-21-3.9.6-dev` | April 21st   | `sha256:bf95795b0ba0fe052e440370fbd886139efad4fcfbd193bfb9da62f427dcf6a6` |

