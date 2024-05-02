---
title: "buildkit Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the buildkit Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
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
|  `latest-root`     | May 1st      | `sha256:de0919e512201404cd1a4af8a03692b515a8b90663b5d0573a3e85a2fd2f63cd` |
|  `latest-root-dev` | May 1st      | `sha256:b75f0f028e7ab11f5f0e53ac0db2808f45964043f85b3f141c7d7f3225767622` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `latest-dev` `0.13-dev` `0.13.2-dev` | May 2nd      | `sha256:f028980662b7c570693ac1a12fce13a7b1a37dd5d9c9f08c3aea375081a253b2` |
|  `0.13` `0` `latest` `0.13.2`                 | May 2nd      | `sha256:30fab06945546abe8b06c26babbb7f1e26ca1c94ae0a0b275d2a200735cf4739` |
|  `0.13.1`                                     | April 25th   | `sha256:54d7ef9f620df47c729766de5bdd8cf35a346c745369fedbe2f0a14c934ca238` |
|  `0.13.1-dev`                                 | April 25th   | `sha256:1d339d3636ee6b86c3d7a70f5ed6896b974f26e50858cca844b2ae5c962a7597` |

