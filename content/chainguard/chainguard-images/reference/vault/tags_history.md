---
title: "vault Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vault Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-28 00:50:32
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/vault/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/vault/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/vault/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/vault/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | March 18th   | `sha256:00c09364906f8d27786e4d7c0ce98101292bc99066c7193f6404ca65143c73dd` |
|  `latest-dev` | March 18th   | `sha256:7b50c96b439df48c7bda32e4beacf906c2608a076770ba7178f952871ef60d29` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `1.14.10-dev` `1-dev` `1.14-dev` | March 27th   | `sha256:cabc4ed6e671508e9fb796c0ed91211b6c784f68c616192ffaa64b4c93b320f7` |
|  `1.14.10` `1.14` `latest` `1`                 | March 27th   | `sha256:1d82cafaa559cd1ba801d5bab1bd511c3daa60965f07e96e90454e44fd6c737a` |
|  `1.13.13` `1.13`                              | March 27th   | `sha256:8135fd5d5b165cb4db162a581a1dbb4ebe8b29d9c8a34134182566bd17ca803d` |
|  `1.13-dev` `1.13.13-dev`                      | March 27th   | `sha256:22963e17f990f9cb978f5761cd8fbc7d5bbb848219713c7fcf7c8b5f964dcdfc` |

