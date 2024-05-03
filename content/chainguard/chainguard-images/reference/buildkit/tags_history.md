---
title: "buildkit Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the buildkit Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/buildkit/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/buildkit/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/buildkit/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/buildkit/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)            | Last Changed | Digest                                                                    |
|--------------------|--------------|---------------------------------------------------------------------------|
|  `latest-root`     | May 2nd      | `sha256:55a4898fcd81a8cdd84fe81dcecb4c119cf0783431420347e43fdb4f9165ca9e` |
|  `latest-root-dev` | May 2nd      | `sha256:112130cc072fa956d39c9f0edbebcd8c9f406c4f56cb94c82a881faddf19f1e0` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `0.13` `0.13.2` `0`                 | May 2nd      | `sha256:6b96b57c0658dd9e1a116601d918ff82be174eb5145809f9350528951b76a0f7` |
|  `0-dev` `0.13.2-dev` `0.13-dev` `latest-dev` | May 2nd      | `sha256:6e243e11e3224c4dd21abf415c1e0f34b724c4b083ce3c627f445929187e7f2c` |
|  `0.13.1`                                     | April 25th   | `sha256:54d7ef9f620df47c729766de5bdd8cf35a346c745369fedbe2f0a14c934ca238` |
|  `0.13.1-dev`                                 | April 25th   | `sha256:1d339d3636ee6b86c3d7a70f5ed6896b974f26e50858cca844b2ae5c962a7597` |

