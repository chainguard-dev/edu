---
title: "consul Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the consul Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-30 00:52:22
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/consul/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/consul/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/consul/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/consul/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 29th   | `sha256:24bd5b691c3d61c0130a54ac81ef776b7c14d463db9498abb653f2b298e397bd` |
|  `latest`     | April 24th   | `sha256:54f4ce2905300e5e52ed63da8db76517f4161c1518b134e43385638eb29a1c98` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `1-dev` `1.17-dev` `1.17.4-dev` | April 29th   | `sha256:362a9458d0a8192b026ecaefb83a1f4f75b07745d6da8653ddb84c1345040ab2` |
|  `1.15.11-dev` `1.15-dev`                     | April 29th   | `sha256:671daca846a884f8fe5a3a459dfc751a796dfa999887a66d8242161510f5fe7f` |
|  `1.16.7-dev`                                 | April 29th   | `sha256:1b1639c1928fcc7708c95ea50893b6ee4b74700a34e06cc9405657fde7ebfd0a` |
|  `1.16-dev`                                   | April 29th   | `sha256:9814d99a11c905780a7deed52918053d64c9745c9e527b90b01411603d237143` |
|  `1.16.7` `1.16`                              | April 25th   | `sha256:c2adad9dbf0abafad98a6c76321a227001992dcc324dc82c79536ff9f3e9946c` |
|  `1.15.11` `1.15`                             | April 21st   | `sha256:9f9522b1d04dd8bc2862628cc2e47a6ee5da82fce39ca214d4f2b168e22bb134` |
|  `1.17.4` `1` `latest` `1.17`                 | April 21st   | `sha256:8dbd54154cd9c606cd41868b29799da7cfe8a444d950ce032907bb702d4d45ec` |

