---
title: "yara Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the yara Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-24 00:45:45
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/yara/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/yara/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/yara/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/yara/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 23rd     | `sha256:a9b9a997e803cdfef9485e01b92628955a46cb67b390a8ebb885d62dd8d0edc0` |
|  `latest`     | May 23rd     | `sha256:71ad5ef6718115506f52d166fe3683d4acee8f1ca87c9af70df450a23055ebef` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `4.5-dev` `latest-dev` `4-dev` `4.5.0-dev` | May 23rd     | `sha256:4a7638c0ed7610512b5b4bce9278860c60acdab0312a353ed48c5b38a36b05e9` |
|  `4` `4.5.0` `4.5` `latest`                 | May 23rd     | `sha256:7e31c41f75e6717270977a21045467296435360bfdf4135279c654f92b689644` |

