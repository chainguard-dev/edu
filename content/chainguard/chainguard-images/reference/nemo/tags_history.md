---
title: "nemo Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nemo Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
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
|  `latest`     | May 2nd      | `sha256:7347c1956aa1024c9fb598129659484f662792357c3de8ea7766a6ac11fe18dc` |
|  `latest-dev` | May 2nd      | `sha256:376e0c37d6c7c7612a3c3030f672666db34c4ae4b32232f5f88bc5b9a7cf44e3` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1-dev` `1.23-dev` `1.23.0-dev` `latest-dev` | May 2nd      | `sha256:90b88bb668605c4a37a44a0bc738e2b799162d4f358b2caeb3509a018ee3aec7` |
|  `1` `1.23.0` `1.23` `latest`                 | May 2nd      | `sha256:b5c650864af81bfac9cf6ee57a5c09d8bc6e6dd0ef8faedbd834c326bf0f12de` |

