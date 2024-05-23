---
title: "helm Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the helm Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-23 00:45:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/helm/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/helm/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/helm/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/helm/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 22nd     | `sha256:c76975c0d2f31ea02a35b2aecf43fa9e332a64dce082ace1e313e9861e1d362f` |
|  `latest`     | May 22nd     | `sha256:2dea770ee3c61f54cb30691d63c8a5ac41981c19fd9a33705a9760e303b98ac2` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.15` `3.15.0` `latest` `3`                 | May 22nd     | `sha256:646d4a0dacfdafee175addeb01268dbf94a5e31e84ede5d5439c4f330d803b11` |
|  `3.15-dev` `latest-dev` `3-dev` `3.15.0-dev` | May 22nd     | `sha256:38c92312def067e2ede85834d8721147c22fa9cf058bee7cf972931d156e95ab` |
|  `3.14.4` `3.14`                              | May 15th     | `sha256:0c177fb85d6a7f3fc6f3de13db8322905b5ddeb2fdea2113a68b5bf5ddcb8bdb` |
|  `3.14-dev` `3.14.4-dev`                      | May 15th     | `sha256:b719b4a6efbece5213320216dc6004777a23a3f73b4cb8b16fe88178525d096f` |
|  `3.11.3-dev` `3.11-dev`                      | May 13th     | `sha256:d19f95e05b32385f5bad1aabd0d3da598752a530f9b0bb9abed33ed96c17bbae` |
|  `3.11.3` `3.11`                              | May 13th     | `sha256:0ea603774d017c1a29e5664a95cfa1eab62906d8f13b2a508a55bf331254a248` |

