---
title: "cadvisor Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cadvisor Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-19 00:54:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cadvisor/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cadvisor/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cadvisor/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cadvisor/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | March 18th   | `sha256:1e26283d888b2bb77c3d335264dc12069286af9973e9c56e544d1bb1757368e1` |
|  `latest-dev` | March 18th   | `sha256:32f101524d938a94ca4aa21ad306b1bd50db05f0d078f700de6642fb1b354dc7` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0` `0.49.1` `0.49` `latest`                 | March 18th   | `sha256:0ecd1f62037af229762af6378ad4c6f32891efe9400c99a56d55b28b01f87b79` |
|  `0.49.1-dev` `0-dev` `latest-dev` `0.49-dev` | March 18th   | `sha256:014509ce44b33dba7673b33f1696731fca8e65576810469e9f926ad665eb4010` |
|  `0.49.0-dev`                                 | March 2nd    | `sha256:a971164e22d772972554153655bfaa591ad5298a2b29493bbb4a870129f88ba6` |
|  `0.49.0`                                     | March 1st    | `sha256:4f1a3aa68b9c19ca7f17988b93e42aabeb2a7e6ec36aa1e79b7185bb1a32877a` |

