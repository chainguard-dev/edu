---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-27 00:41:27
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
|  `latest-dev`        | June 26th    | `sha256:ce65de96b14a7b4bb167dc226eb0ebd5f1e00043ef577ceed8f5534492fa4f1a` |
|  `latest-splunk-dev` | June 26th    | `sha256:4a75664beefa1b4575c73f903ae8b1dcfc2a7c3541c07e8e44e83d53b0edc2fe` |
|  `latest`            | June 26th    | `sha256:972684b6735ef3790d53fce56191fce17e83d1567f21a4156d1a628df5e87afe` |
|  `latest-splunk`     | June 26th    | `sha256:4ef6eb958d4e6e277d648806d2531dac8638d0f8ca9765d28bb3016d84033ec3` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `1` `1.16.5` `1.16`                                                | June 26th    | `sha256:3755500ca8a8340c77fec62d56ca5f56fa1707aba6813e807b04fdaa70023936` |
|  `1.16.5-dev` `1.16-dev` `latest-dev` `1-dev`                                | June 26th    | `sha256:7885133993db888d787d18d9c8d94cad2ba3c93018bbb683acc55bf6d4dec5da` |
|  `1-splunk` `1.16.5-splunk` `1.16.5-r1-splunk` `1.16-splunk`                 | June 26th    | `sha256:2512b09b302fe5bd54f657b69bdb1a974856f92e58b47cf40b7052dac2bc4b86` |
|  `1.16.5-r1-splunk-dev` `1.16-splunk-dev` `1.16.5-splunk-dev` `1-splunk-dev` | June 26th    | `sha256:6eaff75b4240701258baa0d89f19dd0634d33cc0cdc9df26e36c6ec3bad27233` |

