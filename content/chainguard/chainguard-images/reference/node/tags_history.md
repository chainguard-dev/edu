---
title: "node Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-23 00:42:59
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/node/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/node/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/node/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/node/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 22nd   | `sha256:a144e925d28ab66b5a0e83aebeac7efcd32358091f69feab3c7480d50baadac1` |
|  `latest`     | April 22nd   | `sha256:16f1eaeff1f2bf2b6e2912299c7332fe163105b0dace694f8732df20c438e224` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `21.7.3-dev` `21.7-dev` `21-dev` `latest-dev` | April 21st   | `sha256:a4dc0c613c7e4baac74b56c04101bc0dfbc2c1d2144ecddb7edf6e6fc4544eab` |
|  `20` `20.12` `20.12.2`                        | April 21st   | `sha256:00a2441c1fc4c5e318cb3f5dbb486a0c4086d475f3856731137cfd6636a6824b` |
|  `latest` `21` `21.7` `21.7.3`                 | April 21st   | `sha256:16339b86c250e617adbfa2c97428b5f6a57a59fe812e9b227bf1c9f28bc602c6` |
|  `20.12.2-dev` `20-dev` `20.12-dev`            | April 21st   | `sha256:ce73bc0f36df7cdff8af9f3e0ca719ce7361b3e88a25a767b13420c824c7d05d` |
|  `18-dev` `18.20-dev` `18.20.2-dev`            | April 21st   | `sha256:abcdc87d4a29e842f4ec9dc69c9e25490428df0472c804a0a780badbdae9e704` |
|  `18.20` `18` `18.20.2`                        | April 21st   | `sha256:217bb634a72b2c98c2ebfc97519f3eae1676fb1509e366a3cb5832947a589881` |
|  `18.20.1-dev`                                 | April 9th    | `sha256:d754b4ac7941229753008026b8e4ae14bac29e0a7d3f2388b2ee23945fb7e24c` |
|  `20.12.1`                                     | April 9th    | `sha256:13a239cc5bb1fba4cc90e7f3796ace78930915c61f8f3b5a9c9c25df8d4d12a2` |
|  `20.12.1-dev`                                 | April 9th    | `sha256:2de522e612d199b6df72b706d371f0e3a206d5bbd5f8f721c006fa4af5c67c1f` |
|  `18.20.1`                                     | April 9th    | `sha256:ce2b68aaeccef49e3c7ee87d031ff52010c376bf99424d9d08251a503354adbc` |
|  `21.7.2-dev`                                  | April 9th    | `sha256:12fde7eb020635684cd9e9e550e4826656c1006f5b549210048a79a8c6c9c25b` |
|  `21.7.2`                                      | April 9th    | `sha256:f17c4a90e196a4fa7047ae64c1629e3577ebd45470029a1970a9c1a5a86aa529` |
|  `20.12.0`                                     | April 3rd    | `sha256:b0b755db7dd968c07d9a75d51b4b3764679bb1183a629314837cc143b2b486bb` |
|  `21.7.1-dev`                                  | April 3rd    | `sha256:1dd2ea1fc6f4d70d6560c3cd869fa7f4168556f0b4f22535998c690a2bea5767` |
|  `21.7.1`                                      | April 3rd    | `sha256:fbd0d7df25026770d73c3260f9f84592f1aabc592bca01b9714b2461f7e09a42` |
|  `20.12.0-dev`                                 | April 3rd    | `sha256:47dc806dbacd5f8c0dc9541cde1fdfbedead308f4a9bbb69d448b8cbaad2c072` |
|  `18.20.0`                                     | April 3rd    | `sha256:8aea9f756f30e3e962b1823c9b1093740c67cf8c2dcb5b855b3516e3a7f55bf4` |
|  `18.20.0-dev`                                 | April 3rd    | `sha256:1d690ca26b47f51ffc42346a74229e59d6b862eca58e2e4bf4de75b78a1cd6c1` |
|  `16.19.1-dev` `16.19-dev`                     | April 13th   | `sha256:bba7820a61df3f1a8560ed8e58cc472b63bde7211a28c53408ddc037de324b39` |
|  `16.19.1` `16.19`                             | April 13th   | `sha256:3cb3f6b898f8cd15aea39688a54a20035e0f62fed358799fcd162283f535bb54` |

