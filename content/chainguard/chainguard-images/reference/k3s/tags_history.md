---
title: "k3s Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the k3s Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-26 00:38:30
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/k3s/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/k3s/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/k3s/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/k3s/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | March 21st   | `sha256:055bf8db29bff169a5a22043f09b46a6bdfb02c42ed86b8d47dfad57fb9ad4f9` |
|  `latest-dev` | March 21st   | `sha256:b9821c1245083966c9dbdd37428bbc880dbcfee11fec0fa8a6799ada2ef543c9` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed  | Digest                                                                    |
|-----------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `1-dev` `1.29.2-dev` `1.29-dev` `latest-dev` | March 25th    | `sha256:7331bdadb92ff8a9d97fdf00d8ae9560199969d2aa0e4b5e54785bc83f157c98` |
|  `1.29.2` `1.29` `1` `latest`                 | March 25th    | `sha256:a842618f9addc44a09702baa417879e9836810075a58847399381d2484875e1a` |
|  `1.29.0-dev`                                 | March 2nd     | `sha256:b416758e770504a47b960f0ce1ef8909c0b4754fa1457a1b9d720b045cf971fb` |
|  `1.29.0`                                     | February 26th | `sha256:85b5d15887278ed110a626dd53309f1e7096ca6e3ab7764ab1ea7815b8adc1b3` |

