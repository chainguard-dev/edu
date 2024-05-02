---
title: "grype Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the grype Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/grype/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/grype/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/grype/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/grype/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 29th   | `sha256:6ff1c0903cb93434e74f9709f3e59131cc62f3025d205bac5b0f1c468eda255e` |
|  `latest`     | April 27th   | `sha256:3f8b89c2b2f6957734510a88b962b6764fad5fc715277d88dd427291877d1ef9` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0` `latest` `0.77` `0.77.2`                 | May 1st      | `sha256:b24fefdbd97e1be041d8de10bee46b67f9053a46e9d185f0810e1d3f3cb95231` |
|  `0.77-dev` `0-dev` `latest-dev` `0.77.2-dev` | May 1st      | `sha256:6c0ffac73a40f16265f5fd3d4965fb67d4b22fe8c94a8db4ebae0e652eee2bb4` |
|  `0.77.1-dev`                                 | May 1st      | `sha256:0f9ee9c83dc3b8920cf49bc2a145ee9d09f8da647bf024583cbd5a5daf328a8e` |
|  `0.77.1`                                     | May 1st      | `sha256:d843569f324eee5bb52a1b20405444b0ebb4cd08fe36671c220ed59277a4680f` |
|  `0.77.0-dev`                                 | April 21st   | `sha256:341638335599028da312b6e765de204b84f39028fabe375fc5342f71b8a75ef0` |
|  `0.77.0`                                     | April 21st   | `sha256:0a1622f25939eb8b7218266f5372711ae7c171504538c7cc24cfbe0ce2a6e8fc` |
|  `0.76.0` `0.76`                              | April 16th   | `sha256:b6e387080410e11d2fd0a2d92947a3ce7a2d8b2827d81a61c7cbc5f376ea8ab6` |
|  `0.76.0-dev` `0.76-dev`                      | April 16th   | `sha256:6c91a94c3963e4bab3afad1cc5a2cd048dc56b7e74f48c940648a4fec3380925` |
|  `0.75-dev` `0.75.0-dev`                      | April 11th   | `sha256:0f3838a53ddca6eb00961b3ed8d95c908453c019432f956416205b6aae95c35d` |
|  `0.75` `0.75.0`                              | April 4th    | `sha256:cf42976650078eca72070ef8f882df8dda648ff6bccaa16c13bc9946692c07a4` |
|  `0.74.7-dev` `0.74-dev`                      | April 4th    | `sha256:2b7411ab77222fc8d3e7f91543150391404b4031e9f9342477e67448ee169adb` |
|  `0.74` `0.74.7`                              | April 4th    | `sha256:dd9f631c8fe8112e1f13b3feb4137e8cfcc5b41a748985d2aaaa6e724e2d28dd` |

