---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
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
|  `openjdk-21` `latest`         | May 2nd      | `sha256:7b08b3e5fbc64ebf87bac08749747364a9e1dbc53e93c56b9e6d8ff5dc27221e` |
|  `latest-dev` `openjdk-21-dev` | May 2nd      | `sha256:5b9b5219762455d0c3f082741e604db4292b3614b0d0f817bce7ff9b50ede5a5` |
|  `openjdk-17-dev`              | May 2nd      | `sha256:2e2f8a84a602d3af53b16aa57b5c2208b29620fd896cdd8164ef740d9ee2677d` |
|  `openjdk-11`                  | May 2nd      | `sha256:8b392da19b310aadde7c9e733c3de2fb14160a4b694725c9078ae9f6d5f26c42` |
|  `openjdk-11-dev`              | May 2nd      | `sha256:882bffdf701481e3403143ac86782d43ada28d524d412705599cb7c7afc8f55b` |
|  `openjdk-17`                  | May 2nd      | `sha256:0a23b694a720fdd1a9dac54e8e729c20ffb8103f2be8873a700b82001a17f67c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-11` `openjdk-11-3.9.6` `openjdk-11-3` `openjdk-11-3.9`                              | May 2nd      | `sha256:a0552c2197a5b1edd8131b01f31b19fc0bd9132c5e4d5a3107257127be9b08cd` |
|  `openjdk-21-dev` `openjdk-21-3.9.6-dev` `openjdk-21-3-dev` `latest-dev` `openjdk-21-3.9-dev` | May 2nd      | `sha256:bbbce356410e4bfd7ce0cf2282332b181ca3db2d5ba0c2e2af7c2bbc48481bed` |
|  `openjdk-17-dev` `openjdk-17-3.9-dev` `openjdk-17-3.9.6-dev` `openjdk-17-3-dev`              | May 2nd      | `sha256:e6726621b063b3d5ad6e8c543b137442d8cb803c0e8149b2ef02948f8f71360a` |
|  `openjdk-11-dev` `openjdk-11-3.9.6-dev` `openjdk-11-3.9-dev` `openjdk-11-3-dev`              | May 2nd      | `sha256:c2c4ee523c9554efbd770620879dbe8e2a4cc4adeb2fd7b1b9c492b9aebb0625` |
|  `openjdk-21-3.9` `openjdk-21-3.9.6` `latest` `openjdk-21` `openjdk-21-3`                     | May 2nd      | `sha256:ebbe013190ee1a7958f3b4fe585ee78564691525d137faa872f5fe876ed55159` |
|  `openjdk-17` `openjdk-17-3.9` `openjdk-17-3.9.6` `openjdk-17-3`                              | May 2nd      | `sha256:6ce1c8d97c2090f3a63d428b17545d298f3f290c2d07485339e61e1e5d7ad76b` |

