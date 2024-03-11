---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-11 00:52:51
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
|  `latest`            | March 8th    | `sha256:d1948e648cf9be91cbb8985c719f263887dcbc64f3fea09ad918dc00212bc8b0` |
|  `latest-dev`        | March 8th    | `sha256:59c56c1c05115279b69c93104697208197a1bae776861d891a8dd411c25faa39` |
|  `latest-splunk`     | March 8th    | `sha256:c3d2a05830a4d2128803bd8fe9517eb601cbe8e8a93f54362567a4fea4d5bcc6` |
|  `latest-splunk-dev` | March 8th    | `sha256:94d207e5965a4626cb4c09611c72c3f3e0b8882dad3392fe6577decc2194c3df` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `1-dev` `1.16-dev` `1.16.3-dev`                                | March 10th   | `sha256:9b395a316497b7f8f6e03e613b7871e70b1541968d64d24283237e70445b8e28` |
|  `1.16.3-splunk-dev` `1.16-splunk-dev` `1.16.3-r1-splunk-dev` `1-splunk-dev` | March 10th   | `sha256:d1cddd52ae7ce6a663f938008414eeabbecc124924ba28d1c623905f66a57110` |
|  `1.16-splunk` `1-splunk` `1.16.3-r1-splunk` `1.16.3-splunk`                 | March 8th    | `sha256:6db270059edb00345b7937524f10017a20a5a10514ed42e047addf77046d2539` |
|  `1.16` `latest` `1` `1.16.3`                                                | March 8th    | `sha256:7928ba856248d3cc90eb66186ed887538d9bdbbc48c554b2ef819341a36dcce5` |

