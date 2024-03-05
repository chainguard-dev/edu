---
title: "nemo Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nemo Chainguard Image"
date: 2024-03-05 17:06:05
lastmod: 2024-03-05 17:06:05
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/nemo/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/nemo/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/nemo/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/nemo/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | March 1st    | `sha256:ab434d5d52b05c5894d389890caef9e6734ffbc46c4f6bb95d2689d0563e2828` |
|  `latest-dev` | March 1st    | `sha256:cb26aeced14fcb630d62648298421ba20d7e2ba6701312f4a09338410a8f9c1c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.23.0` `1.23` `1` `latest`                 | March 2nd    | `sha256:7687aa237daa9fc4452809d035c3eb9e816dfdf29fc310d010e42e6667c79ad9` |
|  `1-dev` `1.23-dev` `1.23.0-dev` `latest-dev` | March 2nd    | `sha256:db41a27da2ade74f2b5920829ccc8ce7be4e5e9aa6f7f02bc57dee2bf1a1eaf6` |

