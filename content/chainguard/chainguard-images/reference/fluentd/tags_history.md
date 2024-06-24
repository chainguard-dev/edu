---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-24 00:43:49
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
|  `latest-splunk-dev` | June 23rd    | `sha256:31006f9608200d1cda4ae1003709877ca6e6997f295d73eb053071f8f81e0e28` |
|  `latest-splunk`     | June 23rd    | `sha256:6c039535789171c5e2719c11bb0ae71bb2a9d31f398694f5b49c7fa1ed22217e` |
|  `latest-dev`        | June 22nd    | `sha256:0d7a2744f393dde0e92c4ec9f1359736d204890589379f904c71f25f9ab4c2ba` |
|  `latest`            | June 22nd    | `sha256:9cae41d704678280c169e3ae6054601944988ceab348e1be9cc522d587dbf69f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16.5-dev` `1-dev` `1.16-dev` `latest-dev`                                | June 23rd    | `sha256:713485a6f071a14c8a643759ed0d1c7922f87933d5086a0e97a8a4b9cf8d9399` |
|  `1.16.5-splunk-dev` `1-splunk-dev` `1.16.5-r1-splunk-dev` `1.16-splunk-dev` | June 23rd    | `sha256:763bd990908b3be70bb6994b6eed35c3bef25b0b1b7bb9072901943f8315646f` |
|  `1-splunk` `1.16-splunk` `1.16.5-splunk` `1.16.5-r1-splunk`                 | June 22nd    | `sha256:2b2a375157a85efb4c6ecb0054c9719c63db0ff33ef6e4e3d1a316bd26368858` |
|  `1.16` `latest` `1` `1.16.5`                                                | June 21st    | `sha256:d61bb4ccdca638a5d5dec2ce4c0feb13df0f64eff1b2e2a94e82bd30718b7671` |

