---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-06 00:48:16
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
|  `latest-splunk`     | June 5th     | `sha256:6a2577283c6b58b4edb49d69e922c78e4a0eb2b064e725bb639977b3d2d8d337` |
|  `latest-splunk-dev` | June 5th     | `sha256:de7d25d4d921707c058405bb0f6587c0451c8f0a3317b647e100a2a472debea9` |
|  `latest`            | June 5th     | `sha256:c72810f2fa0cdddcf1caed02c9ae921f542237ad269395c980011ab59d836093` |
|  `latest-dev`        | June 5th     | `sha256:f896c40b189ca9d892491600c795ac7c73119c73bda54f7869002ef0544ebe43` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16-splunk` `1-splunk` `1.16.5-splunk` `1.16.5-r1-splunk`                 | June 6th     | `sha256:472e65a669a7a89377c81515f9034106373c764123bad6e9df464bc6e1d8575b` |
|  `1.16.5-r1-splunk-dev` `1.16-splunk-dev` `1-splunk-dev` `1.16.5-splunk-dev` | June 6th     | `sha256:a7304c26079b927b5d738e29b78c9b8f955d851d610813eed702f96c958aa65f` |
|  `1.16.5-dev` `1.16-dev` `latest-dev` `1-dev`                                | June 6th     | `sha256:36d53f081520ecff7ee3c3484bf65c031b1b7b79e6b40ea3828745618b22757d` |
|  `latest` `1` `1.16.5` `1.16`                                                | June 6th     | `sha256:503bc009b3c2b2237d28a11d423a13847a95d254bf49ebe7c7b490b43fb7ae76` |

