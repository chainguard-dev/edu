---
title: "step-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the step-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-01 00:50:07
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
|  `latest-dev` | May 31st     | `sha256:18c5dc03cc687bc97355bd8b71a6ceb99f7e16f27b75929862ebbeff75680a2a` |
|  `latest`     | May 23rd     | `sha256:a65b2bfa14fbe5bcfa999833208451051eb71a792e44d0392715da51c75941c0` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `0.26.1-dev` `0.26-dev` `0-dev` | May 30th     | `sha256:fc70121b9b514caf21a7713580765ff6e6cea9a3c100e638e46458f4b29043ca` |
|  `latest` `0.26` `0` `0.26.1`                 | May 23rd     | `sha256:7d0420734c84792f4d4cfc44d80ec97cb7032fc2b130beff58d3f4540fc255ca` |

