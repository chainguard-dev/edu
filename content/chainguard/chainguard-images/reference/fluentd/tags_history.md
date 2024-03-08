---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-08 00:56:03
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/fluentd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/fluentd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/fluentd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/fluentd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)              | Last Changed | Digest                                                                    |
|----------------------|--------------|---------------------------------------------------------------------------|
|  `latest`            | March 7th    | `sha256:5e0903076d818bebfe9c3caa50ecd354121fa8e306b2534f14e0338c0eb9112c` |
|  `latest-dev`        | March 7th    | `sha256:580c21dd202f2767dd35ba9a382b49fa023254f435f26bbc1aa9c3b96ad74ebb` |
|  `latest-splunk-dev` | March 7th    | `sha256:cd34ff62f34ed5ad4b1f028376b13a4067c810d384c318b1cb4f38f8ff54f263` |
|  `latest-splunk`     | March 7th    | `sha256:8b2202a5a8a84d3fc69ded9368e1fd1efd4655258b1caf4b61e3936a3147a78b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16-splunk` `1.16.3-splunk` `1-splunk` `1.16.3-r1-splunk`                 | March 7th    | `sha256:2f5ad88af02a33f9ec6dbf88c6dadd3a8505083149d2723e91e99daaebebac2b` |
|  `1.16.3-r1-splunk-dev` `1.16.3-splunk-dev` `1-splunk-dev` `1.16-splunk-dev` | March 7th    | `sha256:c9f4055819a4fc89f431b4e6ebcf9444598b881d5bb8f73ad9adfe396758d81f` |
|  `1-dev` `latest-dev` `1.16-dev` `1.16.3-dev`                                | March 7th    | `sha256:687268fcb1764141350898d918cf5516c1213c80d35fe57e10fc5a51c12245b6` |
|  `1` `1.16.3` `latest` `1.16`                                                | March 7th    | `sha256:e94dda4c73bb8636d87ae8ff4406563961de0b488ef2d80696198de9b160a4ab` |
|  `latest-splunk-dev`                                                         | February 9th | `sha256:b2d2725bb9fbd7541c09a3b94952eb73751a93c5d99377eebd46ae7dbaeb6853` |

