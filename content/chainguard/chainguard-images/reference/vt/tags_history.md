---
title: "vt Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vt Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-11 00:52:51
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
|  `latest-dev` | March 8th    | `sha256:608094e500b4a961b8c0e8b0d5c85bc34ee2d5d593c7f13ec47c4412ba5f6d90` |
|  `latest`     | March 8th    | `sha256:ef6f35cbdde6a7d6070d99097cc89cd205f2cfa281ae8fd57948f76fa1ce872b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.0-dev` `1-dev` `1.0.0-dev` `latest-dev` | March 10th   | `sha256:b955429ca1c19bcb2fa2e67a2577e2010b059da9e396ef90cb841ce973244e63` |
|  `1.0.0` `1.0` `1` `latest`                 | March 8th    | `sha256:1ba4ae662dcc18c09efda0c72cdb49c9f709c14452212790bdb94f24f5f4ed25` |

