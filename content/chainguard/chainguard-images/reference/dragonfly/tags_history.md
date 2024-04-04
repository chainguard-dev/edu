---
title: "dragonfly Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the dragonfly Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-04 00:51:18
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/dragonfly/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/dragonfly/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/dragonfly/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/dragonfly/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 3rd    | `sha256:94cfeec184d8cfa5642e033dd0839a236dc09a2beab6522f19563bae0ca7a52c` |
|  `latest`     | March 31st   | `sha256:344afed047bb6a24492f16dfa4feae6d800b1732656b4eb8198e2b6d70423446` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1-dev` `latest-dev` `1.15.1-dev` `1.15-dev` | April 2nd    | `sha256:b6510f6a2352943392d87efdda086e2dc87d6ac156a459c98d7994f39996474a` |
|  `1.15` `1` `latest` `1.15.1`                 | March 29th   | `sha256:57bb2cfcb772cb801e9c54f48f8819f83ef413e0b5ee9acf55eaa6dd1ffed64e` |

