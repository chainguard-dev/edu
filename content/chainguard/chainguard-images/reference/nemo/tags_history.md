---
title: "nemo Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nemo Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-23 00:42:59
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
|  `latest`     | April 22nd   | `sha256:3f1ce19326b1fadb017035c5a286895662d79396ddc02bc2fd6005a4b73ef6a3` |
|  `latest-dev` | April 22nd   | `sha256:e15090b77c0910920f14cf1cfd00fc543e86fffdc67aec11382faeb7ef36d716` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.23.0-dev` `1-dev` `latest-dev` `1.23-dev` | April 21st   | `sha256:db2834d2f706b4ac7878f641b7a440138b207fcb9da1ee383b4c109061f538d8` |
|  `1.23.0` `1.23` `1` `latest`                 | April 21st   | `sha256:49d4f1097b8028cb002081d27558ae386e05377e481cafe8744aeffb58852ba4` |

