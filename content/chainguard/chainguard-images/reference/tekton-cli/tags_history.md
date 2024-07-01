---
title: "tekton-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the tekton-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-01 00:36:20
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
|  `latest-dev` | June 28th    | `sha256:f3c9d36c97753ef5341c0ec89205ac7c5b3701f8268f5100c1da5a96209676cc` |
|  `latest`     | June 26th    | `sha256:5b453031f75c4a176b1bc6f22a890cd382e78203b61c98e001ef38083c4b3f97` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `0.37-dev` `0.37.0-dev` `0-dev` | June 28th    | `sha256:75dfbcb84b526fced9c1300faf579bc9b1be043ccb4e4dadb52cadfa8e40003f` |
|  `0.37.0` `0.37` `0` `latest`                 | June 25th    | `sha256:4bf7501ca4fd64d49c33b27be11cefdec761a52e24b1b42fb2f9343866e9d373` |

