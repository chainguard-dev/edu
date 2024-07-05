---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
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
|  `latest-dev`        | July 3rd     | `sha256:655713d459c1b445ccecce3585dcfce178f46d59f32f2e6c5ed6ac8b69ee3945` |
|  `latest-splunk-dev` | July 3rd     | `sha256:3bf8e6598ffd18c8aba87c0280fddf0c20c4de254d133a26cd36e648d8613d33` |
|  `latest`            | July 3rd     | `sha256:32eb4cb6e0f55f98fa8c7ffdd2951981ca0915c0b2f7d17850bb984987bb3483` |
|  `latest-splunk`     | July 3rd     | `sha256:d016bac081103e810b389dd3a2d393cefd417754d57f1c826f58fd77128e0d9b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16.5-dev` `1.16-dev` `1-dev` `latest-dev`                                | July 3rd     | `sha256:cf392a159f6591c1009bae7398c1dccc349dfde176080bd232e2ec023af2b3ba` |
|  `latest` `1.16` `1.16.5` `1`                                                | July 3rd     | `sha256:938c45290b61695906e92687d91cff28ba0392dbd153b8e2cc88c009114231a6` |
|  `1-splunk-dev` `1.16.5-splunk-dev` `1.16.5-r1-splunk-dev` `1.16-splunk-dev` | July 3rd     | `sha256:a9a6d511f27f819963a88147988d6d031855163bbe9d8ef2169f1924e1378d68` |
|  `1.16.5-splunk` `1.16.5-r1-splunk` `1-splunk` `1.16-splunk`                 | July 3rd     | `sha256:5c715cbafc555899b4725d70e70ff5a495d884bd9f17c11d4f2bcee971c481d6` |

