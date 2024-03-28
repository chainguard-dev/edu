---
title: "prometheus Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the prometheus Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-28 00:50:32
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/prometheus/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/prometheus/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/prometheus/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/prometheus/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 27th   | `sha256:b06258e8b6529442508de651a31273249f3836d6d512bc37703a038f71c778a8` |
|  `latest`     | March 27th   | `sha256:52c4e9784f146199451a3852333356b7ef4c4d7c45194ac3ab3138f3fdf260d6` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.51.0` `2` `2.51` `latest`                 | March 27th   | `sha256:67d98516367d72bac8b6b415843c1a2980f61c17b5fbff631d068940c5e88446` |
|  `2.51-dev` `latest-dev` `2.51.0-dev` `2-dev` | March 27th   | `sha256:61333028417a314c65f7ae1e840c307c5251f17286fa2afc493d272ac15c1f8f` |
|  `2.50.1-dev` `2.50-dev`                      | March 18th   | `sha256:c4eae816f969baa1ba9752bf55e8357993d3ac3ddf0daa9349b423eb96c48a87` |
|  `2.50.1` `2.50`                              | March 18th   | `sha256:2429ff2c41627a0b47bc2e518b0f6efe26e3c94c286221e8e1b1e22e88ade7cc` |

