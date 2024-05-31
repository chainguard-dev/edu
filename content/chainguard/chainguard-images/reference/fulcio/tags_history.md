---
title: "fulcio Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fulcio Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-31 00:48:45
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/fulcio/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/fulcio/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/fulcio/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/fulcio/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 30th     | `sha256:acd948469c6a25215deb6f52d80ae9f7ab85de8e3c21097675f1414ae7d00a56` |
|  `latest`     | May 23rd     | `sha256:72cb9cfb8ce937caf8aff3ce0bbb98129019c7b5046e94ca1f4e48a12347d087` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.4-dev` `1-dev` `latest-dev` `1.4.5-dev` | May 30th     | `sha256:6d1d1d0a465a57d0bf78cd04cfb2714b43141858230ca488b6e19d028787c57f` |
|  `latest` `1.4` `1.4.5` `1`                 | May 23rd     | `sha256:c095768d8b02e9534206edf5f14591bd3835021c44bcce8b617cecf30fe39e24` |

