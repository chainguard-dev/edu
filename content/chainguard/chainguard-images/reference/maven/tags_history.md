---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-05 17:06:05
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
|  `openjdk-17` `latest`         | March 1st    | `sha256:302c3d25cfcef959920772f741dc29740138888b9cd02f4404f8cf3b0d7a85f3` |
|  `openjdk-17-dev` `latest-dev` | March 1st    | `sha256:4939b38fc116e10f0c1424349cf8e9e086dd2b393fe37eff3c7b53cc787fc3d0` |
|  `openjdk-11-dev`              | March 1st    | `sha256:f899f7a85bc4fdffb4bd432f9f9c2a1fe94b3dd21a7274017089aca7ba0051fd` |
|  `openjdk-21`                  | March 1st    | `sha256:dc9208dfad14bcd653c80119aef1323ac33a9be7b44edd4bd6f34df3753f1ac1` |
|  `openjdk-21-dev`              | March 1st    | `sha256:2ecdd46129f81e9f42656aca814d8789c4bb804d0c79f9db860e9beee54c4fa8` |
|  `openjdk-11`                  | March 1st    | `sha256:9e8ee988e1a8e13a12efc118cba8bc639ae3dc07337ceb82393e58e9e8c4785f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `openjdk-17-3-dev` `openjdk-17-3.9-dev` `openjdk-17-3.9.6-dev` `openjdk-17-dev` | March 2nd    | `sha256:88d3d50cf02ab6c467be9fca2d203fb9d55defafe18c43b6a51646409e3ffb83` |
|  `openjdk-11-3.9-dev` `openjdk-11-3-dev` `openjdk-11-3.9.6-dev` `openjdk-11-dev`              | March 2nd    | `sha256:eb2973deeea01ed9df42d3b54949f24dc7a43ece1ea2fb99c7d25bcf8ea3b9de` |
|  `openjdk-21-3-dev` `openjdk-21-3.9.6-dev` `openjdk-21-dev` `openjdk-21-3.9-dev`              | March 2nd    | `sha256:6bf90ea7b925902fa1b2326da18d3d395e49cfa00100acb807f50be3f131e24e` |
|  `openjdk-21-3.9` `openjdk-21` `openjdk-21-3.9.6` `openjdk-21-3`                              | March 1st    | `sha256:6d4a531bc017c42311255608c41fb68ab5ff02ce4ad933fbd2bfa6741dde795a` |
|  `openjdk-17-3.9` `openjdk-17-3` `openjdk-17` `latest` `openjdk-17-3.9.6`                     | March 1st    | `sha256:fe80f89e99d1d0377ce0042bc678ab91e825be6f1acf6f38990aa62a6a6a4e38` |
|  `openjdk-11-3` `openjdk-11` `openjdk-11-3.9` `openjdk-11-3.9.6`                              | March 1st    | `sha256:ed8af89a1ff2e20d7bf9a8dd2c3ddb0d929c90114a584973a315ad64b668d0ab` |

