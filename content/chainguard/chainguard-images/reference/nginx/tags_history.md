---
title: "nginx Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nginx Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
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
|  `latest`     | June 28th    | `sha256:a10afd49df1df9caff1dedaddef54a2c0b2e1174db5acd539981a22b61356d2b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.27-dev` `1-dev` `latest-dev` `1.27.0-dev` | July 3rd     | `sha256:4676b89e253314df58cc38656f1d88b515f571118a02163a6627c66c9e32efe0` |
|  `1.26.1-dev` `1.26-dev`                      | July 3rd     | `sha256:ae45709fd986bfab58b31d8fb95711e59b548f6249ab430325769dfc848fe302` |
|  `mainline` `1` `1.27` `latest` `1.27.0`      | June 28th    | `sha256:248a89847e8cab8f9e1c2230d974a02460e9cbe452ac67b9e6fdf18dd0d597a6` |
|  `1.26.1` `stable` `1.26`                     | June 28th    | `sha256:b787682cf22c83f809027e214a1cc849fd1896809ebba0713e4e1b9a64812874` |

