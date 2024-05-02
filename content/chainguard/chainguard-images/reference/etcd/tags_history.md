---
title: "etcd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the etcd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/etcd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/etcd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/etcd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/etcd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 1st      | `sha256:3ce0f84476253549cf7f77afe41432d6e40ec2e29594bf598c7c108dc2eba6f5` |
|  `latest`     | May 1st      | `sha256:9659ff7372e63f2cad2fa3651df57255c50c3b2f35f6eca05b4c8a82c0830bd0` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `3.5.13-dev` `3-dev` `3.5-dev` | May 1st      | `sha256:d838fb27d46a568d0dc2b34931bd73f4172d0c17d18b51f7cc580c2cffa20529` |
|  `3.4.32-dev` `3.4-dev`                      | May 1st      | `sha256:1b379b8dcbb5b5e822b11f94c2a3064c4345b148b662ff2cd5ce50c96291ecfe` |
|  `3.4.32` `3.4`                              | May 1st      | `sha256:5281e3fb23b5e236720a19119caa11fe106f09c0c0963a2e27427126efe079c9` |
|  `3.5.13` `latest` `3` `3.5`                 | May 1st      | `sha256:6a98ab2ef69decf7587319d539a5fd02f38127dc5f20c2ca12743bf60b0ac579` |
|  `3.4.31`                                    | April 21st   | `sha256:5d8abbcfb187978ef20eaca3d2b18382debc0f9e4095113a82136db41e34c04a` |
|  `3.4.31-dev`                                | April 21st   | `sha256:20d7842e9556329750de78172129f388f124a41b10aa679d691d01eec64eecd7` |

