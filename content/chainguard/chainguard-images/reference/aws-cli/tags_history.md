---
title: "aws-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the aws-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-29 00:53:42
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/aws-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/aws-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/aws-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/aws-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 27th   | `sha256:80fcf683d32200a682e50061e24f78756c1db38779b2ef885f9c75ff18a2e8f3` |
|  `latest`     | April 27th   | `sha256:41e2efa1f9af3f525862c68a9d5df388f7fad2b6ac2143551d5d32d8f4656a84` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.32.71-dev` `1-dev` `1.32-dev` `latest-dev` | April 27th   | `sha256:7fdefeaa84366cbe9a01abd08c539f0f804c7908c7d68c426dae6ff15c697f9a` |
|  `1.32` `1` `latest` `1.32.71`                 | April 27th   | `sha256:e3a22ca7b00124b9e2838f56b1b047fdf2f6dbbd996d80bce74b548a53a9cfcd` |

