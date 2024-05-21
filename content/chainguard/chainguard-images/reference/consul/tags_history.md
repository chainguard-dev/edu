---
title: "consul Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the consul Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-21 00:38:36
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
|  `latest-dev` | May 20th     | `sha256:ce2caa2ab73337630f5a341d9dd3ad70f3d5b8424b1d8a5c1d7510cc235966fc` |
|  `latest`     | May 20th     | `sha256:a47b039d095002ef5f9d60711e5b31ee7230404c30e36f181443324e0b12fcb0` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16.7-dev` `1.16-dev`                      | May 20th     | `sha256:5963af8174791b1f375ab2e4ab4e357e048c66f6c94dbd7371e00e02617f2e7e` |
|  `1.15` `1.15.11`                             | May 20th     | `sha256:c7570ada67b4e712472861decfd884f0122308cd03ea7777d88618c33f3d8385` |
|  `1.17` `latest` `1.17.4` `1`                 | May 20th     | `sha256:b80fc617940d6fe52d9de79a73bc3a72fc461146ac52e3fa1e4e6a242f07ff5b` |
|  `latest-dev` `1.17.4-dev` `1-dev` `1.17-dev` | May 20th     | `sha256:db91288bde5af6a66bd5c53b45bb4881ad1b343a4abddb6d123142b1e9abcab4` |
|  `1.16` `1.16.7`                              | May 20th     | `sha256:1c84f44b4693b29022efc6e119bb310a9f734cfc13369135eb119d3e965c8cd3` |
|  `1.15-dev` `1.15.11-dev`                     | May 20th     | `sha256:4b6f6d8f42100cb5beee98845f64e9ac9d807536a2cd9924e9ac795ecd4863f7` |

