---
title: "helm Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the helm Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-08 00:38:35
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/helm/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/helm/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/helm/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/helm/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 5th    | `sha256:442d46cdb153a434fd0504ca5c6fd852e87dcc345ccf5d271ecf3d8d41adef23` |
|  `latest`     | April 4th    | `sha256:fe38ad7939573bf65aab5223c33e2a31e961ed242b6e791af828689c3f71f588` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3-dev` `3.14-dev` `3.14.3-dev` `latest-dev` | April 5th    | `sha256:65173b26c889580d1f4d0e5ed0ff792141eb82aaae4cfe0d05af82410eebbe1d` |
|  `3.14.3` `3` `latest` `3.14`                 | April 4th    | `sha256:c57cd32451be1e94046f2359a2edaac2b84e4ecd52b8af40d74c623485302b1a` |
|  `3.14.2-dev`                                 | March 12th   | `sha256:bf5622787e582b6d786ba9d0e9892ef34c60cc56ff7ce9c12e771a9519049e95` |

