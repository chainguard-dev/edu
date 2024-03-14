---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-14 00:37:02
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/maven/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/maven/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/maven/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/maven/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                        | Last Changed | Digest                                                                    |
|--------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `openjdk-21-dev` | March 13th   | `sha256:43112a6d4c483c670f4b8accd7f2da34fc93972a23642b35ac3116b47bdad0f9` |
|  `openjdk-17`                  | March 13th   | `sha256:6d8f0292410d0d0cae517d9dd4aa5f457b7e7239a56a31de534e134589fa82a2` |
|  `latest` `openjdk-21`         | March 13th   | `sha256:e9e33abbef1a3b42232786ee98b260a5ba1c16b1fc07a7772a6f811b3dab8b33` |
|  `openjdk-11-dev`              | March 13th   | `sha256:a9f8c8916108f3de229fd7a297fa037ba54993039a8ef27e2d75b45b11c52e6f` |
|  `openjdk-17-dev`              | March 13th   | `sha256:89a184c0b8ad0d108cb444e0a09ffa5c3c3e1412996ad94d00cd53673d3bee88` |
|  `openjdk-11`                  | March 13th   | `sha256:70d25881d620b9c3801c2133d80e6b8c1b3b271868d5286263d73f96d377a4ea` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-17-3` `openjdk-17` `openjdk-17-3.9.6` `openjdk-17-3.9`                              | March 13th   | `sha256:b9a3fe9c626676c73d823fa4b529fd88d69e531836263f88bce297b01ae6db8b` |
|  `latest-dev` `openjdk-21-dev` `openjdk-21-3.9.6-dev` `openjdk-21-3-dev` `openjdk-21-3.9-dev` | March 13th   | `sha256:df6f79ff2ffeb9777aa35e24fe370618683b1bdb635298cccacfd5ee2811559e` |
|  `openjdk-17-3.9-dev` `openjdk-17-3-dev` `openjdk-17-3.9.6-dev` `openjdk-17-dev`              | March 13th   | `sha256:2b647e56967a85bc91194aa7e34f8b7bb17089c093cef854775a37cd58a8a951` |
|  `openjdk-11-dev` `openjdk-11-3-dev` `openjdk-11-3.9.6-dev` `openjdk-11-3.9-dev`              | March 13th   | `sha256:037f64162f2dbc4fccd4f2daf07a69efd1c88ead4b4ebf452339c930449779b1` |
|  `openjdk-11-3.9.6` `openjdk-11-3` `openjdk-11-3.9` `openjdk-11`                              | March 13th   | `sha256:a2ba2c71c8fe777d3271b7ab2c5b1dd33dcf9d018601c46068b6758fcaa62839` |
|  `openjdk-21-3.9.6` `openjdk-21-3` `openjdk-21` `latest` `openjdk-21-3.9`                     | March 13th   | `sha256:f142c037f5534c7a92ecff4bee4d5a7a3561ca7f89c1466094eba7c47ede36c5` |

