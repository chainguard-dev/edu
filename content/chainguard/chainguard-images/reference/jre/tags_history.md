---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-03 00:33:11
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jre/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jre/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jre/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jre/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 28th    | `sha256:11041bb40ddc77530428d4b6dc24cfa1e92ac1247c893f1b153081443feca213` |
|  `latest`     | June 28th    | `sha256:fc0e81c1af2e96e2ab881e1561cbd9d1a9c1d13a35fbf42f1ee9bde6046d5b92` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-21.0-dev` `openjdk-21-dev` `openjdk-21.0.3-dev`                          | July 2nd     | `sha256:8ef908c114170fdb82738d7742ef0d9956dab712f0367e525f0c7b0ad50aa336` |
|  `openjdk-15.0.10` `openjdk-15.0.10.5` `openjdk-15.0` `openjdk-15`                 | July 2nd     | `sha256:4f70a4fb7fdb9d2300ee6d0e8edbf9ab570483aca8e1be4d31e29a7d3c6a6a9f` |
|  `openjdk-11` `openjdk-11.0` `openjdk-11.0.23`                                     | July 2nd     | `sha256:be739bc4c7236d8f43b2a60776788ac1aada6e545e245c8a4248e493c9defa93` |
|  `openjdk-17.0.11-dev` `openjdk-17-dev` `openjdk-17.0-dev`                         | July 2nd     | `sha256:fe972398c51e970f4a024230b54da7e519112605792cd7636a75c1d1511f912c` |
|  `openjdk-16.0.2-dev` `openjdk-16.0.2.7-dev` `openjdk-16-dev` `openjdk-16.0-dev`   | July 2nd     | `sha256:b3cf87b1e0e9a826c9dee2b5dd208cded998f3a569e9ad9027fa23a10eeb0d05` |
|  `openjdk-8.412.08-dev` `openjdk-8.412-dev` `openjdk-8-dev`                        | July 2nd     | `sha256:f68430f1bf4abc7dd1b210d9447df1778de518295a1cafbf294d5dd2163dc874` |
|  `openjdk-15.0.10.5-dev` `openjdk-15.0.10-dev` `openjdk-15.0-dev` `openjdk-15-dev` | July 2nd     | `sha256:3dc8437a62970236a9b650a309eb7f3876cfabe2e68fd4e067d24aea704d6c80` |
|  `openjdk-8.412.08` `openjdk-8.412` `openjdk-8`                                    | July 2nd     | `sha256:dedf55bb207449bccc6e6ce9d9328195b118cb738e8879d84f77ba504b87f7f2` |
|  `openjdk-22.0.1` `openjdk-22.0` `openjdk-22` `latest`                             | July 2nd     | `sha256:6689594cc18be4e7c84dfa13877112555af6f181f491f3fd6531ee8462fca415` |
|  `openjdk-22-dev` `openjdk-22.0-dev` `openjdk-22.0.1-dev` `latest-dev`             | July 2nd     | `sha256:d940c163ea1dd4926a626882c98e8f31b61663f9740201aa6d38e387ae50420b` |
|  `openjdk-21.0.3` `openjdk-21` `openjdk-21.0`                                      | July 2nd     | `sha256:85713324a385786d1bb03108365636d59efc8c7c0b1f567cc758702d6b41d623` |
|  `openjdk-14.0.2.12-dev` `openjdk-14.0.2-dev` `openjdk-14.0-dev` `openjdk-14-dev`  | July 2nd     | `sha256:3922b77f3877b92d5c4c0d976b4bc4bd3c74b244c9833254081b2ba7ac0d2f43` |
|  `openjdk-14.0` `openjdk-14.0.2` `openjdk-14.0.2.12` `openjdk-14`                  | July 2nd     | `sha256:600d8e15d4153ac1dbb5949384bca3bb3779cdf8cf4c1791a3cefce66af2e243` |
|  `openjdk-11.0-dev` `openjdk-11.0.23-dev` `openjdk-11-dev`                         | July 2nd     | `sha256:236cf4d5f6d81d1e58ba8ca65f28d12c7cf02b9c4978d96f8971745371339616` |
|  `openjdk-16` `openjdk-16.0.2.7` `openjdk-16.0` `openjdk-16.0.2`                   | July 2nd     | `sha256:e9970f0956ba958551ecf446fe7e3f7d3dd8e802ba624f5675a4ff3714b7de34` |
|  `openjdk-17.0.11` `openjdk-17` `openjdk-17.0`                                     | July 2nd     | `sha256:2b75a82d80f89dbc25a0abcf3b1388980ae7b0565edf3229053da42867ee81b9` |

