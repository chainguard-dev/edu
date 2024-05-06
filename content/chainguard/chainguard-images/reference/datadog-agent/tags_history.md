---
title: "datadog-agent Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the datadog-agent Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-06 00:43:57
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/datadog-agent/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/datadog-agent/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/datadog-agent/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/datadog-agent/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 2nd      | `sha256:4ffe36ac095414f13bb38774fbb95eaba755641621826ac69d0599a89b07e8cb` |
|  `latest-dev` | May 2nd      | `sha256:d83a771361ccd34f1dba2612d509767c0e171df69cdfa740e93b42de91f6d3b9` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `7.53` `7` `latest` `7.53.0`                 | May 2nd      | `sha256:f8dc9e81fe79d819dacafae07176bcc27f09dd2b48d30eeed89fb41ce82b8666` |
|  `7.53-dev` `latest-dev` `7.53.0-dev` `7-dev` | May 2nd      | `sha256:36b4a3c9d8306478a50fba4aeeddd5b4fe1d54d23c3c6e89a6217408e6126645` |
|  `7.52.1-dev` `7.52-dev`                      | April 30th   | `sha256:ce92c276ae14211ebedd57d05b69f06d7053ee907e1e96fece1c94b3f3d4e909` |
|  `7.52.1` `7.52`                              | April 30th   | `sha256:3218bf117adfcc04c4849f0531b3097f99ad02f5c55e7f3d6e0b09097c503728` |

