---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-22 00:47:17
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
|  `latest-dev`        | May 21st     | `sha256:a145796a3daec56a35054e5ee16f235474a36c70bcfc15b0d1c17b21ea28cf7a` |
|  `latest-splunk-dev` | May 21st     | `sha256:a4ed65723da0d744be2f86153c26155348181cc608225b1ce92a237a8da32a2f` |
|  `latest`            | May 21st     | `sha256:17afb92fcb3741d57e88cc24fc7442cc0b20a94e4807d24efa222951b7191574` |
|  `latest-splunk`     | May 21st     | `sha256:55350dda41b2b35799647bf397042bf4ff04e2599f5ac084e594e180a3c10d24` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16.5-splunk-dev` `1-splunk-dev` `1.16.5-r0-splunk-dev` `1.16-splunk-dev` | May 21st     | `sha256:f326cca41ae455817b783e4d039aabc19978341db0ca55fd2a7cec4f044e87ed` |
|  `1.16` `1` `1.16.5` `latest`                                                | May 21st     | `sha256:c7a94bf0c527b223afc7569dc122edb471e0812f23b3696340f316fc8af368de` |
|  `1.16.5-dev` `1.16-dev` `1-dev` `latest-dev`                                | May 21st     | `sha256:dd7aaef883da6b97b28ebd56d867327c049b02da286e2af9d8defd4e4b3df917` |
|  `1-splunk` `1.16.5-r0-splunk` `1.16-splunk` `1.16.5-splunk`                 | May 21st     | `sha256:0844ea268cbc8802e5bfdb7c51496b9551b39c87d981bc3594fb5d44354a0820` |

