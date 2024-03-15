---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-15 00:51:40
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
|  `latest-dev` `openjdk-21-dev` | March 14th   | `sha256:f331f22037f3f673631416ddb249e3222f425763cee77e11043e16527912c280` |
|  `latest` `openjdk-21`         | March 14th   | `sha256:8791392a64a3b61dd80502333d13f9638a3e33cedbee12e1cd4dd10193218312` |
|  `openjdk-17`                  | March 14th   | `sha256:fbde45d67ecee58234c753f30b346b876fba22f04067ed5d5e384cf87d61ce45` |
|  `openjdk-11-dev`              | March 14th   | `sha256:3f0da525fc7e7a059aedb574a982e02948748a2ba9bff3d290a53b3ed24a9363` |
|  `openjdk-11`                  | March 14th   | `sha256:d42f3f83745a48620523c9f5d30e0d67ebe7b4a08b4d55b4283276913ade21f3` |
|  `openjdk-17-dev`              | March 14th   | `sha256:2baea3317f5913738ee2a972da124842775de1809e3553a6f21a5285a23fef32` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-21-3.9` `openjdk-21-3` `latest` `openjdk-21-3.9.6` `openjdk-21`                     | March 14th   | `sha256:6ec9985c423e74026b06c3e8ab50c4dac2e4bdda756070f15b6916eb96db478a` |
|  `openjdk-17-dev` `openjdk-17-3.9.6-dev` `openjdk-17-3-dev` `openjdk-17-3.9-dev`              | March 14th   | `sha256:1daf5ace4b6f241501b15e12be37cfc6c0267f17531e0154a8f75b86abb85fd0` |
|  `latest-dev` `openjdk-21-3.9.6-dev` `openjdk-21-3-dev` `openjdk-21-3.9-dev` `openjdk-21-dev` | March 14th   | `sha256:4f94f8b73bce93929b65e9cfe8f75fedcd5dc8ff340466a2219f885a83721a87` |
|  `openjdk-11-3-dev` `openjdk-11-3.9.6-dev` `openjdk-11-3.9-dev` `openjdk-11-dev`              | March 14th   | `sha256:adaf88356c824553a67e3ebc2082dd718b92e7d262370a77aaf17863a74f920f` |
|  `openjdk-17` `openjdk-17-3.9` `openjdk-17-3` `openjdk-17-3.9.6`                              | March 14th   | `sha256:1f65e50a53931d53feb6da3059cbc2564481ad89bee995cd1073669463db1e04` |
|  `openjdk-11-3` `openjdk-11` `openjdk-11-3.9.6` `openjdk-11-3.9`                              | March 14th   | `sha256:dbe9f5fe82dc5a2a55dcdf28deaedb4b4950321bbf77a9dcfd6e73872dcca3a0` |

