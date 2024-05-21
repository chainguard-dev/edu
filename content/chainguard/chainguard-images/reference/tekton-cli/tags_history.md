---
title: "tekton-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the tekton-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-21 00:38:36
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
|  `latest-dev` | May 20th     | `sha256:7559d93c77ccc3972ee847eb9ab643c57b9f944ee68feb831f03d38501e2ba4a` |
|  `latest`     | May 17th     | `sha256:5586daf9bd922aa9e38ac573807b1b78196111b91d4e7de9d1d0956b26523bbe` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.37-dev` `latest-dev` `0.37.0-dev` `0-dev` | May 19th     | `sha256:d1d693be06fc8f044c1795536992c237cad2737b3df8e2faba57ea757cc4daed` |
|  `0.37` `latest` `0` `0.37.0`                 | May 17th     | `sha256:c5e2ceeef33446b240dd5e21759840b11fbac4aeed652c207d14d1f3266c6eff` |
|  `0.36.0` `0.36`                              | May 10th     | `sha256:be0e47acf606f9344fd1015e17d18c345f6f8177264e772f3fd2d8973a0d285f` |
|  `0.36-dev` `0.36.0-dev`                      | May 10th     | `sha256:bee13c0e0f8db635f7c7db33aa1545b3d4d04b09f732808aa73b44fa8d4a58b4` |

