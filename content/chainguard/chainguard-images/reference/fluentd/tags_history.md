---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-01 00:36:20
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
|  `latest-splunk`     | June 29th    | `sha256:4bcefb38ffb2b37fb892c25669a247f7d8dc5bf942e263d7624dccdee3a0525f` |
|  `latest-splunk-dev` | June 29th    | `sha256:87b9cdf9905860d8d4899bd41211586e1457002a05629507285d2cffe79ff59e` |
|  `latest-dev`        | June 28th    | `sha256:279f528d62238041811f31bf554d660cb214181b02f8257161b87972c92274d5` |
|  `latest`            | June 28th    | `sha256:c9ed9fe666e64d95d72570722ad366c9c6b08135d9f2aa0ac98781a07931136e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1-splunk-dev` `1.16.5-splunk-dev` `1.16.5-r1-splunk-dev` `1.16-splunk-dev` | June 28th    | `sha256:272017a71fec994976905009899e17e0ff872e77454a8c654b9c941f19300ddf` |
|  `1.16.5-r1-splunk` `1.16-splunk` `1-splunk` `1.16.5-splunk`                 | June 28th    | `sha256:7efa49fbdb26525f109284d4d03c7ccf983cf28ae32eff4fc6001bed4a774b36` |
|  `latest` `1.16.5` `1` `1.16`                                                | June 28th    | `sha256:6541770516e3cbd6a250e712c748c8fefb22135371ad6e54e295d1d5fe76e6dc` |
|  `latest-dev` `1-dev` `1.16-dev` `1.16.5-dev`                                | June 28th    | `sha256:198127b58496760831d5ab26200c87813e25a1d32ce0a70c85bd6007079bf109` |

