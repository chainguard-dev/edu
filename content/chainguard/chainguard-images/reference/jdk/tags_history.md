---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-26 00:35:03
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jdk/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jdk/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jdk/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jdk/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | June 25th    | `sha256:381626976a5fb9881b79ccfeb06be9d0a1f364b12edafc8b6260cbe931a199d8` |
|  `latest-dev` | June 25th    | `sha256:67ad42451b857eabc71ccaa7203c47409d66e93b50a84e085947766ec4462d37` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-15.0-dev` `openjdk-15.0.10-dev` `openjdk-15-dev` `openjdk-15.0.10.5-dev` | June 25th    | `sha256:ffe8123745de7daacb10618f82a57f29749381e8f2025f0c1c28d576073318fc` |
|  `openjdk-14.0.2.12-dev` `openjdk-14.0-dev` `openjdk-14-dev` `openjdk-14.0.2-dev`  | June 25th    | `sha256:b817466460ecc9966dc14bb30a88428e16971909109544b4dec5d84c0ad30ec3` |
|  `openjdk-22.0.1-dev` `openjdk-22.0-dev` `openjdk-22-dev` `latest-dev`             | June 25th    | `sha256:f1426a709b051f9af02892a05bcccfad942a3a217fb7554098ff899d5f57d576` |
|  `openjdk-16.0-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0.2-dev` `openjdk-16-dev`   | June 25th    | `sha256:d0a4c76fa258319aaa7a18a300341228e5c473ca306378025213c54a01257f33` |
|  `openjdk-21.0-dev` `openjdk-21.0.3-dev` `openjdk-21-dev`                          | June 25th    | `sha256:3e0d441ecc87532b0e53c8f9e2e4525d47c1300c8d9e72802027f508edf9cdd8` |
|  `openjdk-8.412-dev` `openjdk-8.412.08-dev` `openjdk-8-dev`                        | June 25th    | `sha256:5195b43cbde80592f742f9f290ea43afb1f52ac332b942e6b944fc1c7be0aef2` |
|  `openjdk-11.0.23-dev` `openjdk-11.0-dev` `openjdk-11-dev`                         | June 25th    | `sha256:9ee2c090df41c72c2cf29a17da06e5cce0d5cf0e3e91d4f47157ce71f728408a` |
|  `openjdk-17.0-dev` `openjdk-17-dev` `openjdk-17.0.11-dev`                         | June 25th    | `sha256:08ab4e4cc6e796522169f900e514b86c49e89547d7ed07be08e097cef3c6a46f` |
|  `openjdk-21.0` `openjdk-21` `openjdk-21.0.3`                                      | June 24th    | `sha256:da9f5f980cfbc144ba6af6760ffa56cb86025e35d0d7216591dc9eb242915e5e` |
|  `openjdk-8.412.08` `openjdk-8` `openjdk-8.412`                                    | June 24th    | `sha256:8c35cac187a396b4fa0b73014db0a6f1162819137a99078bcefd64786f96a346` |
|  `openjdk-22.0` `openjdk-22` `openjdk-22.0.1` `latest`                             | June 24th    | `sha256:8c7eaaa25e8119307e9d000ea73884ea9759e67d0c471c1b373a95058d44546a` |
|  `openjdk-16.0` `openjdk-16` `openjdk-16.0.2` `openjdk-16.0.2.7`                   | June 21st    | `sha256:0f32ee200f7866276699ba02537adf31c0b241d39769873f4b5e3ae7427acf4d` |
|  `openjdk-11.0` `openjdk-11.0.23` `openjdk-11`                                     | June 21st    | `sha256:4d089da270fd6374136527c12f2116a4895633a2846114ced96627f86b04e82e` |
|  `openjdk-14.0.2` `openjdk-14` `openjdk-14.0` `openjdk-14.0.2.12`                  | June 21st    | `sha256:5d9a86f55db57496354a817c0a643c193f1b31da9121986e4407f7eee9bfb862` |
|  `openjdk-15.0` `openjdk-15` `openjdk-15.0.10.5` `openjdk-15.0.10`                 | June 21st    | `sha256:8bff6a483d4f116f237359a346d1da36820132a394376d0cc37fae751ec1134a` |
|  `openjdk-17.0` `openjdk-17.0.11` `openjdk-17`                                     | June 21st    | `sha256:bc97fd212f9eacb822f8deb6051deae5a673508051e3c0259213a4181a0f50a7` |

