---
title: "rekor-server Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the rekor-server Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/rekor-server/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/rekor-server/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/rekor-server/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/rekor-server/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 2nd      | `sha256:c42b653311e509a6b0d1dab627b38803d487c84965b73ba5f85742472b55e293` |
|  `latest-dev` | May 2nd      | `sha256:25697524a9f6c84dfd1680ec0356a24bf55f8e97641e56f24cd498f31280c581` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1-dev` `latest-dev` `1.3.6-dev` `1.3-dev` | May 2nd      | `sha256:5844c2f7de52cb601ffdd91027f5fdf0a7752b617d003cb558b8b4399545cf4e` |
|  `1` `latest` `1.3.6` `1.3`                 | May 2nd      | `sha256:2140f65aaabfbadfdc00ef84f8fc7d8dbb217a73de32e307bad4438ea9cae8e7` |

