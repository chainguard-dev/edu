---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-04 00:50:16
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
|  `latest-splunk-dev` | June 3rd     | `sha256:374df252ff4d4f2776b41238101853cdbabb4d1d1eb24c6c2987a9aae2778aee` |
|  `latest-splunk`     | June 3rd     | `sha256:e96b885d0680ed2af7157f128ddaf5e66049c8a744f331fffc7d8e0bfc53228e` |
|  `latest-dev`        | June 1st     | `sha256:2e63fa10ce06e17f0d2a88893fdec8bdd89a3a57d9055537e2dd879f33a4e47d` |
|  `latest`            | May 30th     | `sha256:b30d783ff0c3e0939ee9bda01e6e4d4c6d8fca48d7d0a85f1b15b98061a8bdcf` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `1.16` `1.16.5` `1`                                                | May 30th     | `sha256:792415970f6b95b57b5743494220a1ea2db4ae7156af432c973768cef7598133` |
|  `1.16.5-splunk` `1.16-splunk` `1-splunk` `1.16.5-r1-splunk`                 | May 30th     | `sha256:9f7917814e9daf7f74a4c20d406b5a568240836f3b51aefab2d389b9dedfcb94` |
|  `latest-dev` `1-dev` `1.16.5-dev` `1.16-dev`                                | May 30th     | `sha256:cb2ba3c0652471e5dc25ca094c117a02690d8433ea89e0c9b0a670f85f1673a1` |
|  `1.16.5-r1-splunk-dev` `1.16.5-splunk-dev` `1-splunk-dev` `1.16-splunk-dev` | May 30th     | `sha256:370040078fd86f063bfdf6fd6c393f3fd058448e02d0fffa2a4ee5db715cca04` |
|  `1.16.5-r0-splunk`                                                          | May 23rd     | `sha256:741677b3870ced9463d436491c9168ba3861acc2f66fb6e4d469418bde6e670a` |
|  `1.16.5-r0-splunk-dev`                                                      | May 23rd     | `sha256:124507aed6595fc380269d13f107009ad72fe0fc20ad31dad9b531a7da1f157f` |

