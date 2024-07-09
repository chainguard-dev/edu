---
title: "hugo Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the hugo Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/hugo/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/hugo/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/hugo/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/hugo/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | July 8th     | `sha256:2c8eaedec7266e846c1336b93b151f02f4f04eb3e58ac60b9200928181481750` |
|  `latest-dev` | July 3rd     | `sha256:a3218a642ab88f46aeb485dd47e748df27c7e78faa4070ed698c6686b608df2d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                         | Last Changed | Digest                                                                    |
|-------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.128.2` `0` `latest` `0.128`                 | July 8th     | `sha256:c8bbdc1ba94d788c8cb0f5bfdd856920306cb7d1ad4dce8806310e90bd52dcbe` |
|  `0.128-dev` `0.128.2-dev` `0-dev` `latest-dev` | July 8th     | `sha256:c3f7537ddaef2025a38ea1b12143334bf6fe53b93c9067b05d84fd02201025b8` |
|  `0.128.1`                                      | July 3rd     | `sha256:6f4a5d165b7f1094f2d45350a53f797daf4c3f10164fda0d230be0a8ba98dccd` |
|  `0.128.1-dev`                                  | July 3rd     | `sha256:810c7e5f6a699fc955b71386f87f499db9ba810b1de0b7cfd36165900268bf20` |

