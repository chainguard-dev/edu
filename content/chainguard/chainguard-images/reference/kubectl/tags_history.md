---
title: "kubectl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubectl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-15 03:08:24
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
|  `latest-dev` | April 11th   | `sha256:f0f36cec885b3fa66462e75deb587dffc92c120f4a0311981d7ba13ec2440ee4` |
|  `latest`     | April 4th    | `sha256:5869d857db2e4207f13580e2a28b72968a50b04e83d49219d0c9b6a5568923a5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.27.12-dev` `1.27-dev`                     | April 11th   | `sha256:3e212905c5dc3fd722dda20aa21114301fda5da6c3b00db5e8caa6f6bc153ea1` |
|  `1.25.16-dev` `1.25-dev`                     | April 11th   | `sha256:e22e87159347724debf1aca00265b4f6680eead9cca27d54f032a92ce181ba4a` |
|  `1.26-dev` `1.26.15-dev`                     | April 11th   | `sha256:6699d5fc23b59ce426e1164c72106a6dd4620fba242e4696c0fbfe7485c3ba1c` |
|  `latest-dev` `1.29.3-dev` `1.29-dev` `1-dev` | April 11th   | `sha256:1fef740978daccc104572c9e5c13a2353d0085a56f11ba560c422cea667e5796` |
|  `1.28.8-dev` `1.28-dev`                      | April 11th   | `sha256:a84b751ba5b7e09c4ce9fc27339976f87a626f29d885a61da54ed183c2591942` |
|  `1.27` `1.27.12`                             | April 4th    | `sha256:4efb5f3802b099d9571990d2fffa989392632e0c48c8e9e539310cdbbf8aa227` |
|  `1.29` `1.29.3` `latest` `1`                 | April 4th    | `sha256:8f4d97526b12d7d185f285e7c2fa44366c5e7b07d4cf08cb26e04b5d828eebbf` |
|  `1.28` `1.28.8`                              | April 4th    | `sha256:e03d1dd4f1313b435087d33228a1810fe32a0b98c7c480e63abd419bc27c0954` |
|  `1.26.15` `1.26`                             | March 28th   | `sha256:c455c348adfe0fe2fd2e83f14f5c39c4944f09d17a000c1eeb1c4563037ab7f4` |
|  `1.25.16` `1.25`                             | March 28th   | `sha256:714ef12adc3074644347016121b06d540331299c217989db5730db4c67561897` |

