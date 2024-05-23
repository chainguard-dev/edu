---
title: "buildkit Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the buildkit Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-23 00:45:07
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
|  `latest-root-dev` | May 22nd     | `sha256:2abe1361463869fd3c45ecd8b55d05608af5004eb13da32d99e7ccabbdb0d223` |
|  `latest-root`     | May 21st     | `sha256:a7f56c4875fdabaa7039c3a5e30ff109b18a1770fcfb5d39a8b7a5896a963bfc` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.13.2-dev` `0-dev` `latest-dev` `0.13-dev` | May 22nd     | `sha256:5db13dd622afba4762a5dc093618c3b1fce8e74b3b316c4cb3871515b45d8eca` |
|  `latest` `0.13.2` `0` `0.13`                 | May 21st     | `sha256:70f3aaca3a8f49ed84bead2552bfd541763626a518201f5269d9898eefa65d71` |
|  `0.13.1`                                     | April 25th   | `sha256:54d7ef9f620df47c729766de5bdd8cf35a346c745369fedbe2f0a14c934ca238` |
|  `0.13.1-dev`                                 | April 25th   | `sha256:1d339d3636ee6b86c3d7a70f5ed6896b974f26e50858cca844b2ae5c962a7597` |

