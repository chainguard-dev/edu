---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-21 00:38:36
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
|  `latest-dev` `openjdk-21-dev` | May 20th     | `sha256:d79bc68e13bd21aa12c10bef971b11a316afb77b1212c93680611acb6846d781` |
|  `openjdk-11-dev`              | May 20th     | `sha256:f8015fe94d281afbeeb0c39a414f8d3ee3a59faf8c4d5ee02097d779ce808081` |
|  `openjdk-17-dev`              | May 20th     | `sha256:dc4e40fffb23ecde896826dddfe9a8a64eb388dda8480ac6e5dc5b68b1f4e508` |
|  `latest` `openjdk-21`         | May 17th     | `sha256:af751a0107840326abb34e693580365aa31421f77fcea40bf903bb541a16c3d5` |
|  `openjdk-11`                  | May 17th     | `sha256:9dc74655b718a3f85f22c1af34e283366ca4003be37f89e301b94c2e06e6afe1` |
|  `openjdk-17`                  | May 17th     | `sha256:fdf8e7a163276f6071b5863eaae0fe90f5fc0ebd327bb17617176c7db6e5de5e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-11-3.9.6-dev` `openjdk-11-3-dev` `openjdk-11-3.9-dev` `openjdk-11-dev`              | May 19th     | `sha256:a84ec8aa896442b49674ac82048f366f32bbb263cdc48beba1192ea608464f8f` |
|  `openjdk-17-3.9.6-dev` `openjdk-17-3.9-dev` `openjdk-17-3-dev` `openjdk-17-dev`              | May 19th     | `sha256:94c2d3bc4da57be438b7b832ace55d0a0cb229329c6f6e0cc2e67ea5c881b9dd` |
|  `latest-dev` `openjdk-21-dev` `openjdk-21-3.9.6-dev` `openjdk-21-3.9-dev` `openjdk-21-3-dev` | May 19th     | `sha256:9fc651211ab5ea63e7766edff8c1548d30bd4be864d898f9048f59fa571e49c7` |
|  `openjdk-11-3.9.6` `openjdk-11-3.9` `openjdk-11` `openjdk-11-3`                              | May 17th     | `sha256:64b338bcfe43b04666a3aa9252ed943d3aac0a4899d9d30596c20a8622e9895b` |
|  `openjdk-21-3.9` `latest` `openjdk-21-3` `openjdk-21` `openjdk-21-3.9.6`                     | May 17th     | `sha256:91f7a2c1e2cee15cb05127a2a31c631ca776eacc83f21e8da7eb31cb1df3c28f` |
|  `openjdk-17-3.9.6` `openjdk-17-3.9` `openjdk-17` `openjdk-17-3`                              | May 17th     | `sha256:4fe6c143e6b794ec3bf91a5367b39e60831fd825ff697c98a0259a093cb7a651` |
|  `openjdk-17-3.9.1`                                                                           | May 13th     | `sha256:0e4eaeb21b03f72e24767d4696b49935cd6b8838852d89e5243ba19fee27afc8` |
|  `openjdk-11-3.9.1`                                                                           | May 13th     | `sha256:617690269a5361add65e7ef9ed24d5daf94300c5728c41d796a92b680d7d5b41` |

