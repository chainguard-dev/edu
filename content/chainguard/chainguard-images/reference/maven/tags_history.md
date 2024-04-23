---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-23 00:42:59
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
|  `openjdk-17`                  | April 22nd   | `sha256:0a40c03cb1b5af84d83823b4a8161b38dff49c25477db026217580be8947d8d8` |
|  `openjdk-11-dev`              | April 22nd   | `sha256:768147029f501ba368fb075fc15f7685b24684bd4422f4c6fe80a8fe84fc8368` |
|  `latest` `openjdk-21`         | April 22nd   | `sha256:853cf8c52000fb11414596ec76d6829ab74ec830095bee212f2e4568c66ad405` |
|  `latest-dev` `openjdk-21-dev` | April 22nd   | `sha256:bf085d5b2aaaccfeff88d850f867d969c8ee6ae931943227c6e81eb5eeaacbee` |
|  `openjdk-11`                  | April 22nd   | `sha256:25694fbf5ed0c5070fee70b2b7659edb8c443c788b54a32d0e41bb726e0f4faa` |
|  `openjdk-17-dev`              | April 22nd   | `sha256:1cb53e75cb435e0947ed3bab5bd79ad26cdc924762b124302056d14217825f52` |


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

