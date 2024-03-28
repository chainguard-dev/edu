---
title: "nginx Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nginx Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-28 00:50:32
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
|  `latest`     | March 27th   | `sha256:a8768861bf230fcbecc0249a0eab5e092069a4088335c87201afe5c24fb9e03e` |
|  `latest-dev` | March 27th   | `sha256:a2a8ca372ef06b6e3d8625259f820f5f0c22f6f5f2128e762b91b320e64c8cce` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `1.25.4` `1` `1.25` `mainline`      | March 27th   | `sha256:3bf8c1cb93bfc54b0b855aa109e3f384488cd449503c22ffb62e3f851815cd8f` |
|  `1.24` `stable` `1.24.0`                     | March 27th   | `sha256:c5046e6c7e0b6c6aa097c88888b0a78c260ab19cfdc9bf018e36512610bfe9b1` |
|  `1.24-dev` `1.24.0-dev`                      | March 27th   | `sha256:93e1c1f3307a8df83ea925cb49187bb5acc5dcd7263820ceb3c4f24ace83737a` |
|  `latest-dev` `1.25.4-dev` `1.25-dev` `1-dev` | March 27th   | `sha256:12454b742e8d1b500ba246c75c14463a367b0113b44702eb3b8075e1f4c7609d` |

