---
title: "tigera-operator Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the tigera-operator Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-29 00:53:42
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/tigera-operator/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/tigera-operator/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/tigera-operator/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/tigera-operator/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 22nd   | `sha256:b0c53e5ed0951e09df1fd092fe25a75756b59be77ca095dcc5ac958e955155eb` |
|  `latest`     | April 22nd   | `sha256:b9253b5afdb4a630908d323ef6c6fc6dd9a1d7d0d4cb97ec37f9b833e1067d68` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                        | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.33.0` `v1.33.0` `v1.33` `1` `vlatest` `1.33` `latest` `v1`                                 | April 20th   | `sha256:35c0437fc77b03132f103562c28b7114f6deb586838c6fda0c648c65a37b292f` |
|  `latest-dev` `v1.33-dev` `v1-dev` `1.33-dev` `1-dev` `1.33.0-dev` `v1.33.0-dev` `vlatest-dev` | April 20th   | `sha256:7e56fcb23683d831a3b43e9a92b9dbc9bcb7e8249456f0ca5632d187cfc8d43a` |
|  `1.31-dev` `1.31.2-dev` `v1.31.2-dev` `v1.31-dev`                                             | April 20th   | `sha256:a84689fc7ac3f0a53462f8257a37fe14fec8bd2766096204db1c4e4bce1e5725` |
|  `v1.30-dev` `v1.30.10-dev` `1.30.10-dev` `1.30-dev`                                           | April 20th   | `sha256:f7d3e62ae94f2cb64c3979837b0869dad8316c0bfd25fac00af520359f22d5fd` |
|  `v1.32-dev` `1.32.7-dev` `1.32-dev` `v1.32.7-dev`                                             | April 20th   | `sha256:49860fece2870aa9929e94dbfc618b11b0e1b683dd5eb8e93c99f8da7db6dfea` |
|  `1.32.7` `1.32` `v1.32.7` `v1.32`                                                             | April 4th    | `sha256:c0aea25fe31c5323d4dfb4be8b2706cc7a7713ea2b8be610adb1318f9fa1221e` |
|  `1.31.2` `1.31` `v1.31.2` `v1.31`                                                             | April 4th    | `sha256:624316f6ab4d668fea7eec9f1013bbc425d2df72f2a80b0308de14eb7074a1e0` |
|  `v1.30` `1.30` `1.30.10` `v1.30.10`                                                           | April 4th    | `sha256:6ef74df64c4ac1aeab5820a6eddedaf59a305367dbb5332f58038deaa8fbcc48` |
|  `v1.32.6-dev` `1.32.6-dev`                                                                    | April 1st    | `sha256:79a068bcc41e0cc7308e0cd2c3331385fb51782e22e908798e3c2af0a4231d6f` |

