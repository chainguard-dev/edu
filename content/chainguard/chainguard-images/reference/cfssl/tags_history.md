---
title: "cfssl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cfssl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-17 00:44:46
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cfssl/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cfssl/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cfssl/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cfssl/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 16th     | `sha256:cd18defaec71d5fcc2e7813647a6e845611bc2e5d0320b3a103e7ebe5ac3bae5` |
|  `latest`     | May 15th     | `sha256:cd30987e78324229c0aef4e84cbee82651d430f18c17400e87caa539fdf46e70` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.6-dev` `1.6.5-dev` `latest-dev` `1-dev` | May 16th     | `sha256:d04865b7e4bed6c5d610bd70cfc4892a1fcb97d73692429b0cb41737199c4d45` |
|  `1.6` `1.6.5` `latest` `1`                 | May 15th     | `sha256:08e37fbf8a1261d0876801eb9c9070943c8ef8691150cf9dd3de279125a5308b` |

