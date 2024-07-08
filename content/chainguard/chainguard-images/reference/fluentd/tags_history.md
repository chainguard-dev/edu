---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-08 00:34:55
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
|  `latest` `1.16` `1.16.5` `1`                                                | July 6th     | `sha256:bd0122f4a3d69a4c5c1917217e626da9d3ca4391051bff5e55a5fcb91b092b12` |
|  `1.16.5-r1-splunk` `1.16.5-splunk` `1-splunk` `1.16-splunk`                 | July 6th     | `sha256:9a91f0e1f60dc7e7957e29bbeccd6624431201c4cc8bc9b2d31bb24749123d70` |
|  `latest-dev` `1.16-dev` `1.16.5-dev` `1-dev`                                | July 6th     | `sha256:95b2b69061cd777833596881a695d030a01eb797e2ca85faa23a2d6188e08838` |
|  `1.16.5-r1-splunk-dev` `1-splunk-dev` `1.16.5-splunk-dev` `1.16-splunk-dev` | July 6th     | `sha256:642e1d21cfacffb6268c46aaffaa0adef42016803f40f840b40be5505fc4728c` |

