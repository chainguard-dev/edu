---
title: "cilium-agent Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cilium-agent Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-05 17:06:05
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cilium-agent/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cilium-agent/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cilium-agent/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cilium-agent/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 2nd    | `sha256:8cec9cdd081793e7b911fc58b5e1b0f7202e3291e75969e36c76c840de1a36d6` |
|  `latest`     | March 2nd    | `sha256:13024193a8563325b7794ba7abd2e10d857f17342436f2b7077ac545bc6bcab0` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed  | Digest                                                                    |
|-----------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `1-dev` `latest-dev` `1.14-dev` `1.14.6-dev` | March 2nd     | `sha256:a959c49cb11a36839755ca24feb41523577d8352c5111b951c68483186cd86ba` |
|  `1.14.6` `1` `1.14` `latest`                 | March 1st     | `sha256:d79fdef9ed1b061cb8dd1d5bda47e68894a4155b90c13e92bfacf21a2e8b9da4` |
|  `1.15` `1.15.1`                              | February 26th | `sha256:4eb92a59cfe5a919175bad63d86196b9d929c1b9a6db5ba07ef91b06de3902fa` |
|  `1.15-dev` `1.15.1-dev`                      | February 26th | `sha256:1290ac91905e2b371d0ce2243e178cd428f020cf4a346db88e0c0f69cde44087` |
|  `1.15.0-dev`                                 | February 13th | `sha256:2440c61dd9706c407200d1dfd9a551c50a12f8bd4317f623caf300ca9c13e645` |
|  `1.15.0`                                     | February 13th | `sha256:0062292d64e805e68e1a3b49021fc101067a204c9369745fb43402799249845c` |

