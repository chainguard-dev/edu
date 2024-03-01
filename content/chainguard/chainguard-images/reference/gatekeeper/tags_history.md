---
title: "gatekeeper Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gatekeeper Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-01 12:14:22
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gatekeeper/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gatekeeper/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/gatekeeper/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gatekeeper/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest`     | February 27th | `sha256:8a3b1f68fd30b2952a9dbcbc7ec8c9fdc760706cc6ebaef290d91e04f2e3ada7` |
|  `latest-dev` | February 27th | `sha256:2de4c85e3f1f4dbe2780adb08fbfbbe835183360e66769bb4a0c15d520f3eaad` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed  | Digest                                                                    |
|-----------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `3.14` `3.14.0` `latest` `3`                 | February 26th | `sha256:31338ae4eba8284f6561d72f26b4dc316ba2de806b69e10045087edd912ab50a` |
|  `3.14.0-dev` `latest-dev` `3.14-dev` `3-dev` | February 26th | `sha256:b3436ac5e35843c4133e8f90247c1ee4035555ca417dd99c5bf003410491f91b` |
|  `3.12.0` `3.12`                              | February 26th | `sha256:c3fc05a627213b43d9afda205e86f1f65cc77b139b74ba771ce03da5b29d5daa` |
|  `3.13.4` `3.13`                              | February 26th | `sha256:94b7391bbc9dc29a3797788b6ac41a7091c4775fc16ba645b9d2e964803bc6db` |
|  `3.12.0-dev` `3.12-dev`                      | February 26th | `sha256:a37b1ef30c5eb3edd29c2987e1f0efa90eedd986e4f7144938b788a6e4d7c013` |
|  `3.13-dev` `3.13.4-dev`                      | February 26th | `sha256:a289fbea968147d4327db1f9ef24c92213f6a63b540a0994fcab25d6d13c9a66` |

