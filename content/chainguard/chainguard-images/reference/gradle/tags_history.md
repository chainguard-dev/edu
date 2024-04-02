---
title: "gradle Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gradle Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-02 00:36:12
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
|  `latest` | March 31st   | `sha256:76d0d38abb6054bf1f4e1d35d1c1a339dc3ead30b4c26237c4b8a30217314769` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `openjdk-21-8.7-dev` `openjdk-21-dev` `openjdk-21-8-dev` `openjdk-21-8.7.0-dev` | April 1st    | `sha256:7b8e0971a643e7ec03fa8815d59dfd81167fc6700faa94114308f69edc2ad705` |
|  `openjdk-17-dev` `openjdk-17-8.7.0-dev` `openjdk-17-8-dev` `openjdk-17-8.7-dev`              | April 1st    | `sha256:84f97938c523083c454899ee227685187c7d08c792d7c4a91e861b9268644752` |
|  `openjdk-17-8.7` `openjdk-17-8.7.0` `openjdk-17` `openjdk-17-8`                              | March 31st   | `sha256:d4f247c8574971eebba64944a1863954099fc2c5f645fa208de23308402244b7` |
|  `openjdk-21-8` `openjdk-21` `openjdk-21-8.7` `latest` `openjdk-21-8.7.0`                     | March 31st   | `sha256:240ea4a342db7e3ce342739c78063e70e2fbf96abfb6a45f8b49c5dbe504a57a` |
|  `openjdk-21-8.6.0` `openjdk-21-8.6`                                                          | March 18th   | `sha256:0ce6d8d683f2399fce2cfe4447d79f80d123a70512d344d162fa2c319b87d3c8` |
|  `openjdk-17-8.6.0` `openjdk-17-8.6` `8.6` `8.6.0` `8`                                        | March 18th   | `sha256:4a6a4439baabe5b258b08708670bd38fa47707efc387dd6d3b7b41821ffbf1b7` |
|  `openjdk-17-8.6-dev` `openjdk-17-8.6.0-dev` `8-dev` `8.6.0-dev` `8.6-dev`                    | March 18th   | `sha256:4bad8ea8f7e412179408686c2376c770a33cbb22867d54de5e0a8245bc484c62` |
|  `openjdk-21-8.6.0-dev` `openjdk-21-8.6-dev`                                                  | March 18th   | `sha256:7c5bd6899907cd1f1cacb8fc0617472843a66650bb8960d24342d4283f90649d` |

