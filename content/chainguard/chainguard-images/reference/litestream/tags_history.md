---
title: "litestream Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the litestream Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-31 00:48:45
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/litestream/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/litestream/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/litestream/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/litestream/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 27th     | `sha256:f17bdfafffd0d8d4922c39c8658cfdce3f2924dc84a8f75a513471b229821c30` |
|  `latest-dev` | May 23rd     | `sha256:046bb9460613bbf3b941bdd5846857b6fb0b2e2ef8215a487a1cde27998a1b5a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `0.3-dev` `latest-dev` `0.3.13-dev` | May 30th     | `sha256:a5983dcf9977cf10117a4de2361d2824682c25ada45467fa370c3deeb18c3fc4` |
|  `latest` `0.3` `0.3.13` `0`                 | May 26th     | `sha256:6ef73eacb8da712357aea367ff11a2d847f527c1f02894cfb153a844c5cd99eb` |

