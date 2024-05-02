---
title: "step-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the step-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
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
|  `latest`     | May 1st      | `sha256:d043a33d4cc96cb340578a5f06cf93480aa5808d67064a62f0fb7d7584395421` |
|  `latest-dev` | May 1st      | `sha256:33c35a15d458e225d5d471097d5c2bbba3f3de55e5eb76044d1ca7f72b42b7e5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.26-dev` `latest-dev` `0-dev` `0.26.1-dev` | May 1st      | `sha256:0f3a0efcd28186a83daf3791992dad56ad4836aa223182fe9a854316f29ca582` |
|  `0.26` `latest` `0` `0.26.1`                 | May 1st      | `sha256:d0165c16f5c1e254d5dcc9f194bc99e2141f9ee01cd3d09e1090e7090571a486` |
|  `0.26.0-dev`                                 | April 21st   | `sha256:c58861a16bbf5286470f8608892591da684289394dbebd736841a0cbc9f1dcfa` |
|  `0.26.0`                                     | April 21st   | `sha256:5f8d80635bbc72c9eae0d69c4cbdd7b0d515cad0980eaa77c466136cc70434d8` |

