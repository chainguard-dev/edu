---
title: "kubectl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubectl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubectl/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubectl/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/kubectl/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubectl/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 28th    | `sha256:e317214ae145867682a412694cc082f93d2c1451d7b692d08326e63b44bd7ce6` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.29` `1.29.6`                              | July 3rd     | `sha256:0e582a2b493f964ad9a2ce3837115b9b30c25f285e4b463402f1d331e605efae` |
|  `1-dev` `1.30-dev` `latest-dev` `1.30.2-dev` | July 3rd     | `sha256:b97b2b7b59fe11ed3d64686cddc672860424cd46a927fc22cb8916688d77c676` |
|  `1.29.6-dev` `1.29-dev`                      | July 3rd     | `sha256:810dee03906d5109042a436c9e8194741755b2028d454745bdc7a5628f43019b` |
|  `1.28.11-dev` `1.28-dev`                     | July 3rd     | `sha256:73e92ca7220ed9f75a8ab32a51b3f6ac4fc05f29c2c1b2f317a5b308e72bad49` |
|  `1.28` `1.28.11`                             | July 3rd     | `sha256:fafb55edfcc8b374678d52f0e076b9602e3d478bd583255a23ef0a62bd605588` |
|  `1.30.2` `1` `latest` `1.30`                 | July 3rd     | `sha256:d636e62a87ecdf898d982b060996645527b7b53fbc768288d3fc0cd5eaf8216a` |
|  `1.27.15-dev` `1.27-dev`                     | June 28th    | `sha256:c6738307f1a5377598590b718a6219cddef28046da680671474be6a2582d7e1e` |

