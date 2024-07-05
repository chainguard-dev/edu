---
title: "step-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the step-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/step-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/step-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/step-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/step-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 3rd     | `sha256:209ba3c2851b2b9d4ada4eab3ca7271eb029092dc923a8a4d925a8ea3d9e51ad` |
|  `latest`     | July 3rd     | `sha256:3edf078c94f3f3360ea0c17d14df25b83cc890ca88ea6fa97d8bccced1366a7a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `latest-dev` `0.26.2-dev` `0.26-dev` | July 3rd     | `sha256:a0fa704fad82edbd132d1f1e1202a883b89f663bb8bebb3afbea41bbf430e9bb` |
|  `0.26` `0` `latest` `0.26.2`                 | July 3rd     | `sha256:ba8df5600121ed10531e04db73b61a67ad614926efe5d838d715127a46f5530d` |

