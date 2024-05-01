---
title: "buildkit Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the buildkit Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-01 00:46:56
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
|  `latest-root-dev` | April 30th   | `sha256:04f7d0343fdf3999f8d936c17a930044298afd5becd1a7ba6c3210f50b99890b` |
|  `latest-root`     | April 26th   | `sha256:0089ffb8f68f9c0e71bc62165436d64c9871186eb696c4a04cc880aa57a00f26` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `0.13.2-dev` `latest-dev` `0.13-dev` | April 30th   | `sha256:377054c94f239c4772c2b6b396be293e755f1bdf0ff6fc09c66dde4117074d5a` |
|  `0.13.2` `0.13` `latest` `0`                 | April 26th   | `sha256:971938f192171032000ab8b9b1110028e0bfce8906ad7626312c1df102de2375` |
|  `0.13.1`                                     | April 25th   | `sha256:54d7ef9f620df47c729766de5bdd8cf35a346c745369fedbe2f0a14c934ca238` |
|  `0.13.1-dev`                                 | April 25th   | `sha256:1d339d3636ee6b86c3d7a70f5ed6896b974f26e50858cca844b2ae5c962a7597` |

