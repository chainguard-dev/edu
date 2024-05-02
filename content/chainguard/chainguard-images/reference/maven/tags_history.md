---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
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
|  `latest-dev` `openjdk-21-dev` | May 1st      | `sha256:b2a279c1220b28f825a752f4f5176a7329db4d3bdae57adc73e6ebe5973d6510` |
|  `latest` `openjdk-21`         | May 1st      | `sha256:4271b37ecff9d2e235fdd7db9e04d3b3696cad51f721604fab854dbe92bf5ad3` |
|  `openjdk-11-dev`              | May 1st      | `sha256:99927e080019cd91dc6aa634191a51849848e2e7c7e460e60b7b2bd4eef49f29` |
|  `openjdk-17-dev`              | May 1st      | `sha256:7325c0f11c9948efdf6763880900e2f02d1a9a064547dd509ffc8e28e8df3d38` |
|  `openjdk-17`                  | May 1st      | `sha256:8fe2cbc813f8e02a89d271aa370c13e9da64c93f95e71865039da6e6e934de2f` |
|  `openjdk-11`                  | May 1st      | `sha256:9ca5b2c7736a82a8f03100ec1df97666423aeb4e0e80be16d2f08583076c1c61` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-11` `openjdk-11-3` `openjdk-11-3.9.6` `openjdk-11-3.9`                              | May 1st      | `sha256:6b54b4b3470cfbe441d04f997796e7ac8e471afb49ed1bbc5b634fe76cfbc240` |
|  `openjdk-21-3.9` `latest` `openjdk-21-3.9.6` `openjdk-21` `openjdk-21-3`                     | May 1st      | `sha256:4c243d569333b24c98845a5dd379279d7a84b54d981db43a290431f385cd27b7` |
|  `latest-dev` `openjdk-21-3.9-dev` `openjdk-21-3.9.6-dev` `openjdk-21-3-dev` `openjdk-21-dev` | May 1st      | `sha256:d0544a29747ddb92834e54e7565bacb46f97db2f5a15486f917722df30572af1` |
|  `openjdk-17-3.9.6-dev` `openjdk-17-3.9-dev` `openjdk-17-dev` `openjdk-17-3-dev`              | May 1st      | `sha256:f23feb41e4f7c02b6ff0755238d795eb87f186a7d037203878cdc43cce7f95f8` |
|  `openjdk-17-3` `openjdk-17-3.9.6` `openjdk-17` `openjdk-17-3.9`                              | May 1st      | `sha256:bf2190b2469dc87915d2a43035b1f9e7a30d61a7ada133502e9964d02dfce62f` |
|  `openjdk-11-3.9-dev` `openjdk-11-3-dev` `openjdk-11-dev` `openjdk-11-3.9.6-dev`              | May 1st      | `sha256:174f8eac1521f9045d6a6983e74f32131dcc4e78d2f0c9bdd62b45a196bf549e` |

