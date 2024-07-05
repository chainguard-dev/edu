---
title: "rekor-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the rekor-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/rekor-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/rekor-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/rekor-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/rekor-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 3rd     | `sha256:9ee22e86cff2a5e42238b2a231799bd69f5949ff8953c92d2af8fd8462ea0ab3` |
|  `latest`     | July 3rd     | `sha256:946a772fdc4b12dd59fa05e2b154f6cc07458160a2a81c1bae329999163acfb6` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1-dev` `1.3.6-dev` `1.3-dev` `latest-dev` | July 3rd     | `sha256:46817c6902266df26c0b475dcee981678658fbf4e4a4192824b5ccf50fdcea6d` |
|  `1` `1.3` `1.3.6` `latest`                 | July 3rd     | `sha256:43fcd8d1d75ab79ac34cec9d0719cc39b9beff5c9e405871ecf53b340e9577f6` |

