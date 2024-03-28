---
title: "k8s-sidecar Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the k8s-sidecar Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-28 00:50:32
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/k8s-sidecar/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/k8s-sidecar/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/k8s-sidecar/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/k8s-sidecar/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 18th   | `sha256:f31f994a45134c24baa0120f5023e17140649b3d7734a7b9d7de6d0135011f4a` |
|  `latest`     | March 18th   | `sha256:f08bd0be8faad5b6baf99e21b0d9f633e732b1c88e8414758df5af1fa1b2726f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.26.1-dev` `1-dev` `latest-dev` `1.26-dev` | March 27th   | `sha256:8556be7babdbbd3ae1fb35884d56b6ea2b2c50ca57b3c431aa58ee2fd34b861f` |
|  `1.26.1` `1` `1.26` `latest`                 | March 27th   | `sha256:79ff8b1da6b2633ddaefe77ae05dcb5fe0f3d2a5731b35538f559433449e5f5a` |
|  `1.26.0-dev`                                 | March 2nd    | `sha256:fbfacc2f5ca90fbc0933e95b1354a7e397d83b81938181261f498a453c72672d` |
|  `1.26.0`                                     | March 1st    | `sha256:fa244bba955ff2419b401e83fb062f6d2d0e4db5f2955126a71dd866a6847852` |

