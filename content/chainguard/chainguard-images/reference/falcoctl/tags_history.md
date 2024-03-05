---
title: "falcoctl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the falcoctl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-05 17:06:05
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/falcoctl/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/falcoctl/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/falcoctl/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/falcoctl/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 1st     | `sha256:ac949a1b54e9082a09a41503a38e10b039ad0b75a6812a81a457b4f773944bd7` |
|  `latest`     | February 27th | `sha256:6507a0adb6a767d311e411b1c1e475e6af58d9a19d5a260caad78d48cad9136a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `0.7-dev` `0.7.3-dev` `0-dev` | March 5th    | `sha256:8098b2209e1df9ea2edec13e080d3c74983e672e7f4262a1baf41b74f8f49570` |
|  `0.7.3` `latest` `0` `0.7`                 | March 5th    | `sha256:dcdedddfceb67ad7d392eeff3e4cdffc4ddbb47d1cef6df79ef6252603cf78ab` |

