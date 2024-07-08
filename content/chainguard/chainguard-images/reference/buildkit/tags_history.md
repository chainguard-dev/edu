---
title: "buildkit Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the buildkit Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-08 00:34:55
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
|  `latest-root-dev` | July 3rd     | `sha256:f656298adf0a254412e7afe04104bc916a88155132013a99e576e95fe8ef633f` |
|  `latest-root`     | July 3rd     | `sha256:937c0e138fce0b002fd35182f0eb7a0cccbb028f81b100df7a67400cf702dce2` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `latest-dev` `0.14.1-dev` `0.14-dev` | July 6th     | `sha256:fcaa23a9ed27ab3dd706210f753c2ae4386801e48dd4bf38c91f5cc20f838782` |
|  `latest` `0` `0.14` `0.14.1`                 | July 6th     | `sha256:179c3fcf6f4c41632c33a8c8399e1bbb980c36ab8081157a8d1665e8bf552455` |

