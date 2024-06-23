---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-23 00:43:06
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
|  `latest-dev` | June 22nd    | `sha256:2025507287edd8b1079f41f2b13ea58f78b82b8b3dbb1c2af5b2567f5550592b` |
|  `latest`     | June 22nd    | `sha256:fcf3f785786d26aa598b2e4ff48bbccb0858a09d92b440af95d5a89d81db2740` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-16.0` `openjdk-16` `openjdk-16.0.2` `openjdk-16.0.2.7`                   | June 21st    | `sha256:0f32ee200f7866276699ba02537adf31c0b241d39769873f4b5e3ae7427acf4d` |
|  `openjdk-8.412` `openjdk-8` `openjdk-8.412.08`                                    | June 21st    | `sha256:9da80d86858fcdfafdc38cd9de053c6a7d58546fefb0b189f85ece800913e62c` |
|  `openjdk-21.0-dev` `openjdk-21.0.3-dev` `openjdk-21-dev`                          | June 21st    | `sha256:f5ff473d0aa2921097adab019917ae06e8fd7fcb827a532a5aa6e117f7870ec8` |
|  `latest` `openjdk-22` `openjdk-22.0` `openjdk-22.0.1`                             | June 21st    | `sha256:0fedddadb4eddf225ec069ad0737b4ecf96c2fb2e0823bb9fb45d75761a00f91` |
|  `openjdk-22.0-dev` `openjdk-22.0.1-dev` `openjdk-22-dev` `latest-dev`             | June 21st    | `sha256:2cae4985823e25a35267522faf106ec0c418244fa06bf5b1e5b61e7325b7f19a` |
|  `openjdk-15-dev` `openjdk-15.0-dev` `openjdk-15.0.10-dev` `openjdk-15.0.10.5-dev` | June 21st    | `sha256:8c323b61676c08755bc790abfb576410959b7dc8088077a17e9a3593467fe059` |
|  `openjdk-11.0` `openjdk-11.0.23` `openjdk-11`                                     | June 21st    | `sha256:4d089da270fd6374136527c12f2116a4895633a2846114ced96627f86b04e82e` |
|  `openjdk-17.0.11-dev` `openjdk-17-dev` `openjdk-17.0-dev`                         | June 21st    | `sha256:20e462fc3c54527979e179fe60e02d1670fdafd56fb84d96ac76b76c90549a24` |
|  `openjdk-14.0.2` `openjdk-14` `openjdk-14.0` `openjdk-14.0.2.12`                  | June 21st    | `sha256:5d9a86f55db57496354a817c0a643c193f1b31da9121986e4407f7eee9bfb862` |
|  `openjdk-11.0-dev` `openjdk-11.0.23-dev` `openjdk-11-dev`                         | June 21st    | `sha256:7a0754664c23496ac620e8ff8bc563d9c4436d970a7e342f7bc369a9279f61f0` |
|  `openjdk-21.0` `openjdk-21.0.3` `openjdk-21`                                      | June 21st    | `sha256:413a23ff67965539d6b4715139560090d67ba2e78e0d977f09c620fe675a9214` |
|  `openjdk-15.0` `openjdk-15` `openjdk-15.0.10.5` `openjdk-15.0.10`                 | June 21st    | `sha256:8bff6a483d4f116f237359a346d1da36820132a394376d0cc37fae751ec1134a` |
|  `openjdk-17.0` `openjdk-17.0.11` `openjdk-17`                                     | June 21st    | `sha256:bc97fd212f9eacb822f8deb6051deae5a673508051e3c0259213a4181a0f50a7` |
|  `openjdk-14.0.2-dev` `openjdk-14.0-dev` `openjdk-14.0.2.12-dev` `openjdk-14-dev`  | June 21st    | `sha256:45e34687e31e5147473a27968178476b730902727a09c51214eeaab32704951c` |
|  `openjdk-8.412.08-dev` `openjdk-8.412-dev` `openjdk-8-dev`                        | June 21st    | `sha256:98b31a0d34e14d5fab0b7fea4ab62de9d6b6acfd744ac89450f0d8b09cd05ff3` |
|  `openjdk-16-dev` `openjdk-16.0-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0.2-dev`   | June 21st    | `sha256:c1d4938cf0727646480052f44c0f004e62e4f6399978b79df4f5eb957b2508b0` |

