---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-06 00:48:16
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
|  `openjdk-11`                  | June 5th     | `sha256:3a649f95b57a054d283cd6655928533ad5580e5ec435888d5ceaef70e6d405a7` |
|  `latest` `openjdk-21`         | June 5th     | `sha256:58f1b71fb6d7e3af790ff4d7188b74ead774fa4af51b5507662919c04f587b5a` |
|  `openjdk-11-dev`              | June 5th     | `sha256:32398ee6c8349fc6c406f15736a0ef9d8d01bd156fb8856939a8a2ba85d7e6a7` |
|  `openjdk-21-dev` `latest-dev` | June 5th     | `sha256:2c3e2386c9e9ef466ee2a1517c5309d751b6edb3f5da426b062eef3a9132d4bc` |
|  `openjdk-17-dev`              | June 5th     | `sha256:4f81b65facd96e57a2661d05b1067f06c3b3dcaac61cde12e28d5f073f2215c9` |
|  `openjdk-17`                  | June 5th     | `sha256:3aff57d56af02f279a0947edb78c1c1385c7e482945bd8bb3106dd6e43e47639` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-21` `openjdk-21-3.9.7` `latest` `openjdk-21-3` `openjdk-21-3.9`                     | June 5th     | `sha256:991c6ab14b5036ac986d9441ebe90c84de1b05b4f542493c552996556d49e2aa` |
|  `openjdk-17-dev` `openjdk-17-3-dev` `openjdk-17-3.9-dev` `openjdk-17-3.9.7-dev`              | June 5th     | `sha256:dfb52a3c4c8810859d1c7c7853cc8581ff6e9263f4d31a0ee5fe093360d58237` |
|  `openjdk-11-3.9.7` `openjdk-11-3.9` `openjdk-11-3` `openjdk-11`                              | June 5th     | `sha256:8a72c14607e159e9e7b5ac3774468ff53deb61fdef3c66c1e944ae96362b60ce` |
|  `openjdk-17-3.9` `openjdk-17` `openjdk-17-3` `openjdk-17-3.9.7`                              | June 5th     | `sha256:bb2fd09642225f27d13e9742a8cae62e2945f57a77b6c5de80238f47e2b1d5a3` |
|  `openjdk-11-3.9-dev` `openjdk-11-dev` `openjdk-11-3-dev` `openjdk-11-3.9.7-dev`              | June 5th     | `sha256:e71fefc4e91f34a4d715050fb8bb34e05f88120292ddea93f3c72fa59093c11b` |
|  `openjdk-21-3-dev` `openjdk-21-3.9.7-dev` `openjdk-21-3.9-dev` `openjdk-21-dev` `latest-dev` | June 5th     | `sha256:228eb4a2fd2118dd0e1ebf143cab6ae6d5252edc877e85b1692c1e45bd21123d` |

