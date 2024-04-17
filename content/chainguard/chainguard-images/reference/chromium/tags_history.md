---
title: "chromium Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the chromium Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-17 00:46:08
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/chromium/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/chromium/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/chromium/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/chromium/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | April 16th   | `sha256:dbd1a2295abd54f1d2958559ce447b34a10070372e746dd5990251371e5ceb92` |
|  `latest-dev` | April 16th   | `sha256:66cb9f2a722fdbd4e06c6f40dd4eb3a39f7fbce931d0ea605df915b3c0660ea7` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                   | Last Changed | Digest                                                                    |
|---------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `123.0` `123` `123.0.6312.122` `123.0.6312`                     | April 16th   | `sha256:56aa652a4a2871ed6e02dc3f058814244fec31cd610206489e194256531fc220` |
|  `123.0.6312-dev` `123-dev` `123.0-dev` `latest-dev` `123.0.6312.122-dev` | April 16th   | `sha256:502f7c92b739fc9cacc9a2ace003d266f2c5d195de7757bd2d4234d7885e3b8c` |
|  `123.0.6312.105-dev`                                                     | April 11th   | `sha256:aea647d0853b24150ddffefab0309c07052ff910317567c07d34ea40256a595b` |
|  `123.0.6312.105`                                                         | April 11th   | `sha256:beb0b076d3f39986b7d346445d69528bfde8d84879673fa77f3dfa3b1747d136` |
|  `123.0.6312.86`                                                          | April 9th    | `sha256:29f8b6c1d90971014abfdbb86900bd5c15b92bc644e8e39e6149fe79b063a195` |
|  `123.0.6312.86-dev`                                                      | April 9th    | `sha256:8f08fcdf95001ba89d2713e84c224c3458d571eee7716fbc4b72ca1a3ba6e08e` |
|  `123.0.6312.58-dev`                                                      | March 27th   | `sha256:bfb3e3cb70016bb4792b00d7021925de744ea1387959298964b79f06d3eccb61` |
|  `123.0.6312.58`                                                          | March 27th   | `sha256:28acf6ada311ea8bfd2385f82e00f52937575516ead9ab72100a8b57e1ce9551` |
|  `122.0.6261` `122.0` `122` `122.0.6261.128`                              | March 18th   | `sha256:205efdb878b9493fbc8320f7d1a882cb93c7513159488189b747d6175f238e9b` |
|  `122.0.6261.128-dev` `122.0.6261-dev` `122-dev` `122.0-dev`              | March 18th   | `sha256:411875021780446e9fafd0c15f4f900ab1f4255d05faad659336df47f3617bbf` |

