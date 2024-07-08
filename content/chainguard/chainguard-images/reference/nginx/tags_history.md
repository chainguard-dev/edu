---
title: "nginx Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nginx Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-08 00:34:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/nginx/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/nginx/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/nginx/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/nginx/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 3rd     | `sha256:ce79797d52efefe7e15277c9cd914998e024961808a81740da44f66153b154d8` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.26-dev` `1.26.1-dev`                      | July 6th     | `sha256:038cd271c797b690c695ad8e8ad705546078b65105cd29f602e1758c9d80292a` |
|  `1.27.0-dev` `1.27-dev` `1-dev` `latest-dev` | July 6th     | `sha256:48f4e01c6137c626792b686a85d3c2aaac64697ead86fd9085b48dd66d8dc2ee` |
|  `1.26` `stable` `1.26.1`                     | July 6th     | `sha256:952a9fa089bea9b436763f35015f7b6a3be327f438dc3f56888e5e7cfc3269ee` |
|  `1.27` `1` `mainline` `1.27.0` `latest`      | July 6th     | `sha256:0d15760e54a330e859ec8605bb5a59f1d08e9eb67bad3b8bcb8a14e6733f55ae` |

