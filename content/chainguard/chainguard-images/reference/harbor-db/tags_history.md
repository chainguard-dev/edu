---
title: "harbor-db Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the harbor-db Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-15 00:39:35
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/harbor-db/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/harbor-db/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/harbor-db/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/harbor-db/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | April 29th   | `sha256:d33d7a54746a3aed2113b5faaa3262cc1115b64b8cfa8fbcb7fc0266572d80f4` |
|  `latest-dev` | April 29th   | `sha256:dbca9af7bbab9ca670d63838844c25596d959ea395377b23b66dc0816c0f5d09` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2-dev` `latest-dev` `2.10-dev` `2.10.2-dev` | May 14th     | `sha256:de14403898d917da9316d7cc4df45d7833edc4cef8a9b54af55676a48bcc6778` |
|  `2.9-dev` `2.9.4-dev`                        | May 14th     | `sha256:3c6d7e2a85e6b191fa7d73cb2cd4b62638709f7465342314ad078b6106e21452` |
|  `2.8-dev` `2.8.6-dev`                        | May 14th     | `sha256:7767bc8f764b406b27adcf15bb96e8085085c5bc6b0f19df8d36141bf2ef9c66` |
|  `2.10.2` `latest` `2.10` `2`                 | May 13th     | `sha256:8f4e1ab1c21ec99b1d6896c0f2939f64c8b5a341e42563894a54e9983a0dcc1d` |
|  `2.9` `2.9.4`                                | May 13th     | `sha256:2e208d9fa3fbf0d82d4b446cb137fb9aab8a45494c24813d58816b3b3ba31d28` |
|  `2.8.6` `2.8`                                | May 13th     | `sha256:0dd7fd012297bef6fa5edca013e17ac9adb8580deb8ec2a89d6c5e022377ce03` |

