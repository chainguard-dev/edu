---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-17 00:44:46
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
|  `latest-splunk-dev` | May 16th     | `sha256:27fc4644047343ac8118d937a2b6128d47ba9ec0163a4e90fbc519be564f72ca` |
|  `latest-dev`        | May 16th     | `sha256:6bea49457ab28277d1dadd7907a4892c0752205a1bf744e40309b09668a3e680` |
|  `latest`            | May 16th     | `sha256:96afddcab8a24c024ed039f8104d42a8da786fa8d6cac142f89457902650751e` |
|  `latest-splunk`     | May 16th     | `sha256:a1cb966cb58bef3c0c919614458a403f4748b7c62a56c2e247735dfbe5801d32` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1-splunk` `1.16.5-splunk` `1.16.5-r0-splunk` `1.16-splunk`                 | May 16th     | `sha256:bcb83d066a1100dbe39de735585b646b5f730a79b2b3f29632a3db54b18fa4ae` |
|  `1.16-splunk-dev` `1.16.5-r0-splunk-dev` `1.16.5-splunk-dev` `1-splunk-dev` | May 16th     | `sha256:26555eaaffb4a0c0564a1ed84f787ed08aed3168ac06bf1aebc6fd29c14c4d8f` |
|  `1.16.5-dev` `1.16-dev` `1-dev` `latest-dev`                                | May 16th     | `sha256:8aaac40e8d2f99dc66174c612194d916b1021db8cd9bfd3f5a8289181f91b389` |
|  `1` `1.16` `latest` `1.16.5`                                                | May 16th     | `sha256:f8b39940dc6d0130682e7f21dbaf3e24f8878697f42e161f41ec6d14c18bd713` |

