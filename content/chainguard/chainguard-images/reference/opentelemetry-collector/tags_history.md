---
title: "opentelemetry-collector Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the opentelemetry-collector Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-05 00:36:13
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/opentelemetry-collector/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | June 4th     | `sha256:284c43997c427235aad4280f3df35f1c0bb790bfff895e11162005e24f76ce77` |
|  `latest-dev` | June 4th     | `sha256:284fdc2416219ca64dd532a31a624bb39c812ea97419e8ecdc94ddabe8fd673e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                         | Last Changed | Digest                                                                    |
|-------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `0` `0.102.0` `0.102`                 | June 4th     | `sha256:2422ba92c4b52fa85605f2389ba56dd2d3f531a6d6173132120e794523b27080` |
|  `0-dev` `0.102-dev` `latest-dev` `0.102.0-dev` | June 4th     | `sha256:51b595e4f5b86db01798984a8d73387df84ba655a6191d23c7fb515fed80eaf5` |
|  `0.101-dev` `0.101.0-dev`                      | June 1st     | `sha256:f1aef7c8b1d8b0a2addd2e5f060942e21f03fdc6fefc4ecd2fc39ec3611be6a0` |
|  `0.101.0` `0.101`                              | May 30th     | `sha256:53282399aa71508aa1b6b5b28f75fc8ab540f2c0a95d0f5a6a410b0dd0c16c2b` |

