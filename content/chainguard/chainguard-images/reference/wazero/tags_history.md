---
title: "wazero Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the wazero Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-16 00:33:13
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/wazero/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/wazero/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/wazero/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/wazero/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 14th   | `sha256:81630915873b101c0c9dad79fba601f3ff7517e7e3f1b14eccc01a3ff84e17f0` |
|  `latest`     | March 7th    | `sha256:f85771c05290ff713520d9767e56f8ce522a74505aa039c53a6fb7f8ec2d4b96` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.7.0-dev` `1.7-dev` `latest-dev` `1-dev` | March 15th   | `sha256:021c9b1219362d8d67389dcffe50ab1d61fd43e9c1877bc1f495b5173e453b16` |
|  `1.7.0` `1` `latest` `1.7`                 | March 15th   | `sha256:8bb01082c862ff4a1e04af1593a2b7969c3d0747dbfd2b2fec332121af5d0860` |
|  `1.6.0-dev` `1.6-dev`                      | March 14th   | `sha256:3c0a93ae52271f8a662a63303866ebc91c32392793a3de4624c27d1fa3f38a06` |
|  `1.6` `1.6.0`                              | March 14th   | `sha256:0836ad07b9c3792c5bcb7dea7fb71c5c871477b4726b0ced23186ed85c54bcf9` |

