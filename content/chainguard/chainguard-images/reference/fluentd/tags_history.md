---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
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
|  `latest-splunk-dev` | July 8th     | `sha256:2f3f7b52d1e9cf9204268d3aed0e75c77e02b31a34eb7bf9dad0085d5a718ef3` |
|  `latest`            | July 8th     | `sha256:0d81a46b5dcac068ae27fba3908fbe18dac4fbd9bb4c8faa68211661b6e51272` |
|  `latest-dev`        | July 8th     | `sha256:4c3835887552551780c96551327799d514617cbc89725e9c1b36e7ecb2e8b6f6` |
|  `latest-splunk`     | July 8th     | `sha256:01f7246e36b44b56238c5ca18c3970f889f95b91e031f191dc5715fe38862ef6` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16.5-dev` `1.16-dev` `latest-dev` `1-dev`                                | July 9th     | `sha256:d005c3a9ff0edd6ec739c72d1e7fb3496e0ec1d5cce1e4fc56e8ac323ed1b6fd` |
|  `1.16.5-splunk` `1-splunk` `1.16-splunk` `1.16.5-r1-splunk`                 | July 9th     | `sha256:b198eab60d3cb3814d0b46859a6586e981f85020139cbb29834538bbc79060db` |
|  `1` `1.16` `1.16.5` `latest`                                                | July 9th     | `sha256:84a6cfda9e45cb547c3adf943d7b429618e51d1a7ee8eddd0aa46c3b1d5596a7` |
|  `1.16-splunk-dev` `1-splunk-dev` `1.16.5-splunk-dev` `1.16.5-r1-splunk-dev` | July 9th     | `sha256:3edca991b1ac777d1c83a32c0e946b6a2b862f5b39a3f422466cfb7eb8c6e740` |

