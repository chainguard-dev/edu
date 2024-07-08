---
title: "aws-cli-v2 Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the aws-cli-v2 Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-08 00:34:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/aws-cli-v2/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/aws-cli-v2/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/aws-cli-v2/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/aws-cli-v2/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | July 4th     | `sha256:5fa5deaa473dd2753ac991a06faf03aed85b92ed182a343818f9ecb54c3e0c14` |
|  `latest-dev` | July 4th     | `sha256:8082bd64368e41c27a858837449f6d2afc249a0889193c4e5380a9c299ce02ce` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `2.17.9-dev` `2.17-dev` `2-dev` | July 6th     | `sha256:cfa8acbd3531ee44a2886a2402df20c023d26ccc051e3a2c8d8f39f1c6a13d7e` |
|  `2.17.9` `2` `2.17` `latest`                 | July 6th     | `sha256:1974c236b2b184bfa51964a94eea73fff37014a92a655f3ebf63f0bd7c291dee` |
|  `2.17.8`                                     | July 3rd     | `sha256:4752f18146d920d661b0bee6c1be5c0cde891d657eec3fd6deecb03ab1d1b069` |
|  `2.17.8-dev`                                 | July 3rd     | `sha256:7357a7b497930d3daed7f709b6dd6763ac4dd289999f0afb48f28805d03e1b88` |
|  `2.17.7-dev`                                 | July 3rd     | `sha256:f2b319c873312a15082dd194b0d71e3c8f7ee456f57286eba5e09a05c1773559` |
|  `2.17.7`                                     | July 2nd     | `sha256:05ada930ecc9a1a00f43d31bcdb7c1aa8f8c0b16d88503581f5910023328d1bf` |
|  `2.17.6`                                     | July 1st     | `sha256:8ec264ed35c77b494c75c6c4460a836280b704e17d3cca0d3c99810b2d0c4c84` |
|  `2.17.6-dev`                                 | July 1st     | `sha256:fdb808e59f148c844fb67010c2d67c2d21446420d3c5c4b3baf6bfb518e9e7d2` |

