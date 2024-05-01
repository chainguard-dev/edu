---
title: "node Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-01 00:46:56
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

| Tag (s)                  | Last Changed | Digest                                                                    |
|--------------------------|--------------|---------------------------------------------------------------------------|
|  `next-dev` `latest-dev` | April 30th   | `sha256:7d24d8df94ec6316d86360e4e107333229a084243dca959f61ddaff6b8d8e252` |
|  `next`                  | April 30th   | `sha256:d981f4f64b465e06d3fc44bfd55dd0185f6e37a628636f9a1f27a0753f4ea0f4` |
|  `latest`                | April 30th   | `sha256:d0525c76481749fbeeb7eb1fa75187a83094dc03caaa14e165bceee99c0b7892` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                   | Last Changed | Digest                                                                    |
|-----------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `18.20` `18.20.2` `18`                                   | May 1st      | `sha256:68e0a53857685a806c15b6e862923e07efd3303c848cccbe2670dfd15f0f8859` |
|  `20.12.2` `20` `20.12`                                   | May 1st      | `sha256:e38e3ae0bcbab22ce0993463cb35759a8cc3a237a3f39488c09fa72f76ea380d` |
|  `22.0.0-dev` `22.0-dev` `next-dev` `latest-dev` `22-dev` | May 1st      | `sha256:8ab95939ec4299b596b0194ed288c553907da755f66e11d436019d96c9e6034f` |
|  `18-dev` `18.20-dev` `18.20.2-dev`                       | May 1st      | `sha256:b9b7224cbaced27920d48c8781697dfa3f3c28e8d08b90bdf40dc176f7ce66de` |
|  `latest` `22.0.0` `22` `22.0`                            | May 1st      | `sha256:027957607220a76153b3da3b953fdf61607ca944392947d1d15b215033f19b9e` |
|  `20-dev` `20.12-dev` `20.12.2-dev`                       | May 1st      | `sha256:543d7047e6288fcdbf8bb3a4edc5f5d5c5e7bf226884e234ac539f2269a8ac91` |
|  `next`                                                   | April 30th   | `sha256:0cd5343c2634c26f6dfe3a316180f70198613f14058916915a90316a416e5f16` |
|  `21.7.3` `21` `21.7`                                     | April 26th   | `sha256:7092934c1ccba70e209b1c4a147ed786fe1a910e58f45e07815ab22c5a410f6b` |
|  `21-dev` `21.7-dev` `21.7.3-dev`                         | April 26th   | `sha256:fc751328e8521e58f88c8be282a266106f96c97d164d7af9246b6d77751d5e7e` |
|  `18.20.1-dev`                                            | April 9th    | `sha256:d754b4ac7941229753008026b8e4ae14bac29e0a7d3f2388b2ee23945fb7e24c` |
|  `20.12.1`                                                | April 9th    | `sha256:13a239cc5bb1fba4cc90e7f3796ace78930915c61f8f3b5a9c9c25df8d4d12a2` |
|  `20.12.1-dev`                                            | April 9th    | `sha256:2de522e612d199b6df72b706d371f0e3a206d5bbd5f8f721c006fa4af5c67c1f` |
|  `18.20.1`                                                | April 9th    | `sha256:ce2b68aaeccef49e3c7ee87d031ff52010c376bf99424d9d08251a503354adbc` |
|  `21.7.2-dev`                                             | April 9th    | `sha256:12fde7eb020635684cd9e9e550e4826656c1006f5b549210048a79a8c6c9c25b` |
|  `21.7.2`                                                 | April 9th    | `sha256:f17c4a90e196a4fa7047ae64c1629e3577ebd45470029a1970a9c1a5a86aa529` |
|  `20.12.0`                                                | April 3rd    | `sha256:b0b755db7dd968c07d9a75d51b4b3764679bb1183a629314837cc143b2b486bb` |
|  `21.7.1-dev`                                             | April 3rd    | `sha256:1dd2ea1fc6f4d70d6560c3cd869fa7f4168556f0b4f22535998c690a2bea5767` |
|  `21.7.1`                                                 | April 3rd    | `sha256:fbd0d7df25026770d73c3260f9f84592f1aabc592bca01b9714b2461f7e09a42` |
|  `20.12.0-dev`                                            | April 3rd    | `sha256:47dc806dbacd5f8c0dc9541cde1fdfbedead308f4a9bbb69d448b8cbaad2c072` |
|  `18.20.0`                                                | April 3rd    | `sha256:8aea9f756f30e3e962b1823c9b1093740c67cf8c2dcb5b855b3516e3a7f55bf4` |
|  `18.20.0-dev`                                            | April 3rd    | `sha256:1d690ca26b47f51ffc42346a74229e59d6b862eca58e2e4bf4de75b78a1cd6c1` |
|  `16.19.1-dev` `16.19-dev`                                | April 13th   | `sha256:bba7820a61df3f1a8560ed8e58cc472b63bde7211a28c53408ddc037de324b39` |
|  `16.19.1` `16.19`                                        | April 13th   | `sha256:3cb3f6b898f8cd15aea39688a54a20035e0f62fed358799fcd162283f535bb54` |

