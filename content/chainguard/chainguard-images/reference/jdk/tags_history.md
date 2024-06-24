---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-24 00:43:49
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
|  `openjdk-11.0-dev` `openjdk-11-dev` `openjdk-11.0.23-dev`                         | June 23rd    | `sha256:a3f219a689a8cbd71fef2b0fb2cdb29b73aef4adfd7d8613c512bb6be8d267b6` |
|  `openjdk-14.0.2-dev` `openjdk-14.0-dev` `openjdk-14.0.2.12-dev` `openjdk-14-dev`  | June 23rd    | `sha256:e266df1f09ff2a115111ffd7a3e07ffd45fee926d85442a03498e2062351e9fd` |
|  `openjdk-15.0-dev` `openjdk-15-dev` `openjdk-15.0.10-dev` `openjdk-15.0.10.5-dev` | June 23rd    | `sha256:f22ac3f572dde9bfa2757b1bb0ba373ba7bbf77e7b1d808fa2c81fd4c1dce2de` |
|  `openjdk-22-dev` `openjdk-22.0.1-dev` `openjdk-22.0-dev` `latest-dev`             | June 23rd    | `sha256:79bd3ea0017f62faa6faed657fcc18196099b5d43757b6035b3220349ce4506b` |
|  `openjdk-17.0.11-dev` `openjdk-17-dev` `openjdk-17.0-dev`                         | June 23rd    | `sha256:277181aea0266f751921ee57e6d885bfcf247de6c37fa0d5b4f6b9d97f132e1e` |
|  `openjdk-21.0-dev` `openjdk-21.0.3-dev` `openjdk-21-dev`                          | June 23rd    | `sha256:f2ef7efe33aa984c4746f40a765443043a56d2af8dd9d158b85cc62807ec5abc` |
|  `openjdk-16-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0.2-dev` `openjdk-16.0-dev`   | June 23rd    | `sha256:2e67a65c227e4491ed20d0c99a2dd6317d5d7887ef7e7b1612a515fd84c1299a` |
|  `openjdk-8.412-dev` `openjdk-8.412.08-dev` `openjdk-8-dev`                        | June 23rd    | `sha256:c0456c657641a171469781ae130250c7b74ae0589a65798d87a167fa17287a4a` |
|  `openjdk-16.0` `openjdk-16` `openjdk-16.0.2` `openjdk-16.0.2.7`                   | June 21st    | `sha256:0f32ee200f7866276699ba02537adf31c0b241d39769873f4b5e3ae7427acf4d` |
|  `openjdk-8.412` `openjdk-8` `openjdk-8.412.08`                                    | June 21st    | `sha256:9da80d86858fcdfafdc38cd9de053c6a7d58546fefb0b189f85ece800913e62c` |
|  `latest` `openjdk-22` `openjdk-22.0` `openjdk-22.0.1`                             | June 21st    | `sha256:0fedddadb4eddf225ec069ad0737b4ecf96c2fb2e0823bb9fb45d75761a00f91` |
|  `openjdk-11.0` `openjdk-11.0.23` `openjdk-11`                                     | June 21st    | `sha256:4d089da270fd6374136527c12f2116a4895633a2846114ced96627f86b04e82e` |
|  `openjdk-14.0.2` `openjdk-14` `openjdk-14.0` `openjdk-14.0.2.12`                  | June 21st    | `sha256:5d9a86f55db57496354a817c0a643c193f1b31da9121986e4407f7eee9bfb862` |
|  `openjdk-21.0` `openjdk-21.0.3` `openjdk-21`                                      | June 21st    | `sha256:413a23ff67965539d6b4715139560090d67ba2e78e0d977f09c620fe675a9214` |
|  `openjdk-15.0` `openjdk-15` `openjdk-15.0.10.5` `openjdk-15.0.10`                 | June 21st    | `sha256:8bff6a483d4f116f237359a346d1da36820132a394376d0cc37fae751ec1134a` |
|  `openjdk-17.0` `openjdk-17.0.11` `openjdk-17`                                     | June 21st    | `sha256:bc97fd212f9eacb822f8deb6051deae5a673508051e3c0259213a4181a0f50a7` |

