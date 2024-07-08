---
title: "vt Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vt Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-08 00:34:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/vt/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/vt/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/vt/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/vt/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 3rd     | `sha256:4b977295c47573e00d7f79f7ed26f7adcfeb230fa05f54e8e90a86beb0578974` |
|  `latest`     | July 3rd     | `sha256:55f81002da81896e095a9df809f5b57cf8d85ea7f3ac19149ff3bb42185147ca` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `1` `1.0` `1.0.0`                 | July 6th     | `sha256:5dc41745963db02b9a87e51af3cec366e3def01bf069f11b1c9a191effcd0f62` |
|  `1.0-dev` `latest-dev` `1.0.0-dev` `1-dev` | July 6th     | `sha256:f2038b4a3a1f022d41366f3cb1116dad8d6bb7713b43932e09c039e5ef4daee8` |

