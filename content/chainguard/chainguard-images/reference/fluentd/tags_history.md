---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-26 00:35:03
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
|  `latest-splunk-dev` | June 25th    | `sha256:c0d71dee4f104fe640fdef9ccadbf8a99058d270a3485f61bda519795aca5df3` |
|  `latest-dev`        | June 25th    | `sha256:fc6656876d534b67d84b53f6357bdfe16b415eea7838daa99bbc0beb9d95105b` |
|  `latest-splunk`     | June 23rd    | `sha256:6c039535789171c5e2719c11bb0ae71bb2a9d31f398694f5b49c7fa1ed22217e` |
|  `latest`            | June 22nd    | `sha256:9cae41d704678280c169e3ae6054601944988ceab348e1be9cc522d587dbf69f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1-splunk-dev` `1.16-splunk-dev` `1.16.5-r1-splunk-dev` `1.16.5-splunk-dev` | June 25th    | `sha256:5675294297f02cae6eb9d430537dc4d6a23348c0b5bfa2607fe17fbcc96cbc9c` |
|  `1.16.5-r1-splunk` `1.16.5-splunk` `1.16-splunk` `1-splunk`                 | June 25th    | `sha256:e215286548e80c3d18f45dbd7c77ef71b7e272f7ce28766a1a7c877f4b1d7948` |
|  `1-dev` `latest-dev` `1.16-dev` `1.16.5-dev`                                | June 25th    | `sha256:dd43ad4796f1da9d95176ccf44d026ed2d5f5a3a86bccdd78a237fb3ea8abee5` |
|  `1.16` `latest` `1` `1.16.5`                                                | June 21st    | `sha256:d61bb4ccdca638a5d5dec2ce4c0feb13df0f64eff1b2e2a94e82bd30718b7671` |

