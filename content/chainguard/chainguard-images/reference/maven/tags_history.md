---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-29 00:47:42
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
|  `openjdk-17`                  | March 28th   | `sha256:0fb8ff6873065eac762823d046925518e2c0a06d735ff85e61757621e2d2a9cc` |
|  `openjdk-11`                  | March 28th   | `sha256:32ae61397e2f8ebaabc650cdd99591f41a68a5cb121241223ff261f76ed25bec` |
|  `openjdk-21-dev` `latest-dev` | March 28th   | `sha256:feb81c98e6c36a9baa65c696bd73b6affcf4cf60cb90084dbb6a10c5f0cfc4a9` |
|  `openjdk-11-dev`              | March 28th   | `sha256:fc9978f59d53f1d4931dd77cfabb59b3e7757b1720080d65a1d5780f3ad07bd0` |
|  `latest` `openjdk-21`         | March 28th   | `sha256:fb37580a6984c9c8be5b8f51f119b1ca3953546077d71f4d0531344fdbbeb052` |
|  `openjdk-17-dev`              | March 28th   | `sha256:ace8507eede5c6d75c565e6dd6e884c2fe544e175b44de3eda48c85101e853ac` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `openjdk-21-3.9.6-dev` `openjdk-21-3-dev` `openjdk-21-3.9-dev` `openjdk-21-dev` | March 28th   | `sha256:13770c1d698e7409f1b218c94556bbe24b834a98e35bfcb7d3f893c1ad9071ff` |
|  `openjdk-21-3.9` `openjdk-21-3` `openjdk-21-3.9.6` `openjdk-21` `latest`                     | March 28th   | `sha256:199b9675e333588897db4759f30df4c819161d59dc16915b3136a2fea8df745c` |
|  `openjdk-11-dev` `openjdk-11-3.9-dev` `openjdk-11-3-dev` `openjdk-11-3.9.6-dev`              | March 28th   | `sha256:6646d4161e691f21093b47d8f700ed6854ef35cb83c9567927696df512b89021` |
|  `openjdk-17` `openjdk-17-3.9.6` `openjdk-17-3` `openjdk-17-3.9`                              | March 28th   | `sha256:5169ea493897e97351df5de0b657286c51cf28dea651ee6566c7a5dcd66bea76` |
|  `openjdk-17-3.9-dev` `openjdk-17-3-dev` `openjdk-17-dev` `openjdk-17-3.9.6-dev`              | March 28th   | `sha256:ada2fe5d8459b14a6a5321fb74c33fe561a0dd20017a8ca72eb38318ff2f789e` |
|  `openjdk-11-3.9` `openjdk-11-3` `openjdk-11-3.9.6` `openjdk-11`                              | March 28th   | `sha256:8a49c91a9e6f716405fb734bd0505d437172b6a65c14fddd9d9a5ab18b8fa638` |

