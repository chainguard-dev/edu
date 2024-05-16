---
title: "tekton-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the tekton-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/tekton-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/tekton-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/tekton-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/tekton-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 15th     | `sha256:5ad6dea830eb2da796544a0352aff268562364c5f1ed1f98b40ee631742eb47a` |
|  `latest-dev` | May 15th     | `sha256:5f35635a4d2c3e2504feb7bd4260db970cf25b771d8f7cf78bc27e4d8341c96a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `latest-dev` `0.37.0-dev` `0.37-dev` | May 15th     | `sha256:d1fc30564f31091e456f80040063f29efefd2e364c11a4c51bbdd1b662dcca48` |
|  `0` `0.37` `latest` `0.37.0`                 | May 15th     | `sha256:defca81686e30c08c7b803b4e9a123f65b0ae2b7e1fdb280fcd8452c59dfbc5c` |
|  `0.36.0` `0.36`                              | May 10th     | `sha256:be0e47acf606f9344fd1015e17d18c345f6f8177264e772f3fd2d8973a0d285f` |
|  `0.36-dev` `0.36.0-dev`                      | May 10th     | `sha256:bee13c0e0f8db635f7c7db33aa1545b3d4d04b09f732808aa73b44fa8d4a58b4` |

