---
title: "k8s-sidecar Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the k8s-sidecar Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-07 00:45:47
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/k8s-sidecar/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/k8s-sidecar/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/k8s-sidecar/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/k8s-sidecar/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 29th   | `sha256:7ec2086c613576e77f139fe584042890a671a2e6c757e6dd9f434a84deaa94be` |
|  `latest`     | April 25th   | `sha256:1a68b84034d922aca601b6b90b9ab23c64b290ddc496c7d9a29d8c8ddbff7f76` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.26.2-dev` `latest-dev` `1-dev` `1.26-dev` | May 6th      | `sha256:e303c3529f9e77e696ba3df74a78c562520acd9dd5b2439a155c5db29ec8c63a` |
|  `1` `1.26.2` `latest` `1.26`                 | May 6th      | `sha256:c4fc00cfe65a412415d265808dea86fdae9698b3fadf1705c19b1eaf3ea28328` |
|  `1.26.1-dev`                                 | May 2nd      | `sha256:af5976619d32fac8181ae3bf1ea96a2edb30019309bfa3760400484deeaba0a0` |
|  `1.26.1`                                     | May 2nd      | `sha256:39a5f9fc7ffda1f998c207f4df69c9681485b0f8d970322ef1dc74224d5ea547` |
|  `1.23.1-dev`                                 | May 3rd      | `sha256:8ac1b1b9db15611fb6cf25180a6d47d6c41d4981b2a04101e49effd15eca53e6` |
|  `1.23.1`                                     | May 3rd      | `sha256:fcd6d8dadb2db5a8ae2298523d3918117e8ed4951ac8217fe46365c491428adc` |

