---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-01 00:50:07
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
|  `latest-dev` `openjdk-21-dev` | May 31st     | `sha256:5f7eb6d906ddfe510ec811ee66b9fb24c5159b244ef0c21a0cdf515e9877eedb` |
|  `latest` `openjdk-21`         | May 31st     | `sha256:58f1b71fb6d7e3af790ff4d7188b74ead774fa4af51b5507662919c04f587b5a` |
|  `openjdk-17`                  | May 31st     | `sha256:3aff57d56af02f279a0947edb78c1c1385c7e482945bd8bb3106dd6e43e47639` |
|  `openjdk-11-dev`              | May 31st     | `sha256:3108cb09164a30dbcab48b6e78de7774bd23334f1058233bd7d5c943c2ecccf4` |
|  `openjdk-17-dev`              | May 31st     | `sha256:ace738e7819e6ce8fcd91435b264b9df0e7145ea7e0227642f79209f4428361c` |
|  `openjdk-11`                  | May 31st     | `sha256:3a649f95b57a054d283cd6655928533ad5580e5ec435888d5ceaef70e6d405a7` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-21-3.9.7` `openjdk-21` `openjdk-21-3.9` `openjdk-21-3` `latest`                     | May 30th     | `sha256:991c6ab14b5036ac986d9441ebe90c84de1b05b4f542493c552996556d49e2aa` |
|  `openjdk-17-dev` `openjdk-17-3-dev` `openjdk-17-3.9-dev` `openjdk-17-3.9.7-dev`              | May 30th     | `sha256:cf78827b3695ac36d17c5cec0268cf15951d427e8a9ec66f812166387563949b` |
|  `openjdk-21-3.9.7-dev` `latest-dev` `openjdk-21-3-dev` `openjdk-21-dev` `openjdk-21-3.9-dev` | May 30th     | `sha256:c19f9126437075e0a641b0c77589de15113bdf31363162e55a4fd7305ababeef` |
|  `openjdk-11-3-dev` `openjdk-11-3.9.7-dev` `openjdk-11-dev` `openjdk-11-3.9-dev`              | May 30th     | `sha256:a1d994daf98ea53a05143d57f53332ea65c6b97d7fa2137b72032f2c7e5d36d6` |
|  `openjdk-17` `openjdk-17-3.9` `openjdk-17-3.9.7` `openjdk-17-3`                              | May 30th     | `sha256:bb2fd09642225f27d13e9742a8cae62e2945f57a77b6c5de80238f47e2b1d5a3` |
|  `openjdk-11-3` `openjdk-11` `openjdk-11-3.9.7` `openjdk-11-3.9`                              | May 30th     | `sha256:8a72c14607e159e9e7b5ac3774468ff53deb61fdef3c66c1e944ae96362b60ce` |
|  `openjdk-21-3.9.6-dev`                                                                       | May 24th     | `sha256:41a304153886d639b5a4bd7252ebb424b45f5a2643621e01e52e235517d53677` |
|  `openjdk-17-3.9.6-dev`                                                                       | May 24th     | `sha256:cf79812c268bed86ddd82b10daad0d00ff26dab42683748f999b06c33f8b79eb` |
|  `openjdk-17-3.9.6`                                                                           | May 24th     | `sha256:f66fede4dc6e40733a5fe4ee3aa305d1661d8c4489cc0e284e094ba7d047516d` |
|  `openjdk-11-3.9.6-dev`                                                                       | May 24th     | `sha256:2088c7722de52417f78eefa527cf0f98bbbcfeb55255d884fc92ff134fefee49` |
|  `openjdk-11-3.9.6`                                                                           | May 24th     | `sha256:5d4d3884b01eaadddee1df3da6bec97a65d8cb5da746fd15eb0c180f004f82a0` |
|  `openjdk-21-3.9.6`                                                                           | May 24th     | `sha256:8d06f826321c7c588b896feaeb89cdda13d3d4793f60fb28ec38405b7a522b45` |
|  `openjdk-17-3.9.1`                                                                           | May 13th     | `sha256:0e4eaeb21b03f72e24767d4696b49935cd6b8838852d89e5243ba19fee27afc8` |
|  `openjdk-11-3.9.1`                                                                           | May 13th     | `sha256:617690269a5361add65e7ef9ed24d5daf94300c5728c41d796a92b680d7d5b41` |

