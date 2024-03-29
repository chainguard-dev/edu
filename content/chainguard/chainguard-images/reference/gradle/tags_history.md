---
title: "gradle Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gradle Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-29 00:47:42
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gradle/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gradle/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/gradle/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gradle/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)   | Last Changed | Digest                                                                    |
|-----------|--------------|---------------------------------------------------------------------------|
|  `latest` | March 28th   | `sha256:28e3bab828035c5ca93a9cea5b6067511780fee5422fe02b84d4b01fae1e9676` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-21-8.7.0` `openjdk-21-8.7` `openjdk-21-8` `latest` `openjdk-21`                     | March 28th   | `sha256:6cd2bab7a920831816780165a268b205d87fd688a54f1776403021b6f2707662` |
|  `latest-dev` `openjdk-21-8.7.0-dev` `openjdk-21-8-dev` `openjdk-21-dev` `openjdk-21-8.7-dev` | March 28th   | `sha256:8b2a5277bf0b202fccdf9706a557232bb60c5ce0dc2fc4dc590c2e4ed0732741` |
|  `openjdk-17-8.7.0-dev` `openjdk-17-dev` `openjdk-17-8-dev` `openjdk-17-8.7-dev`              | March 28th   | `sha256:adccd9334bf6669c4baf3e56e4e6377afba1dc8b6871166a1c194df3cdaf7c23` |
|  `openjdk-17-8.7` `openjdk-17-8` `openjdk-17` `openjdk-17-8.7.0`                              | March 28th   | `sha256:0bc94d8dfc95da393a75a7d144dc0261023aea3c0ed4210ea7216080247faa71` |
|  `openjdk-21-8.6.0` `openjdk-21-8.6`                                                          | March 18th   | `sha256:0ce6d8d683f2399fce2cfe4447d79f80d123a70512d344d162fa2c319b87d3c8` |
|  `openjdk-17-8.6.0` `openjdk-17-8.6` `8.6` `8.6.0` `8`                                        | March 18th   | `sha256:4a6a4439baabe5b258b08708670bd38fa47707efc387dd6d3b7b41821ffbf1b7` |
|  `openjdk-17-8.6-dev` `openjdk-17-8.6.0-dev` `8-dev` `8.6.0-dev` `8.6-dev`                    | March 18th   | `sha256:4bad8ea8f7e412179408686c2376c770a33cbb22867d54de5e0a8245bc484c62` |
|  `openjdk-21-8.6.0-dev` `openjdk-21-8.6-dev`                                                  | March 18th   | `sha256:7c5bd6899907cd1f1cacb8fc0617472843a66650bb8960d24342d4283f90649d` |

