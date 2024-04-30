---
title: "node Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-30 00:52:22
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
|  `latest-dev` `next-dev` | April 29th   | `sha256:fd8e12d86b7e05d1af1ee88b32a71d61fd6893a99a493c78d736a1ab3c7bdb91` |
|  `next`                  | April 26th   | `sha256:e011dc31fae151ad7b95f15d8d87e9bcdef774460d10e388dd49c748da0c31f8` |
|  `latest`                | April 26th   | `sha256:d673cc4318f598ea158c4944186bfc290b5bbbc465dc8ae5533ab5959aeaef92` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                             | Last Changed | Digest                                                                    |
|-------------------------------------|--------------|---------------------------------------------------------------------------|
|  `next-dev` `22.0-dev` `22.0.0-dev` | April 29th   | `sha256:5c4e60219081bc411a51dfa51364e42cf351022b0cb4c6a9308bcc670349f07b` |
|  `20.12-dev` `20.12.2-dev` `20-dev` | April 29th   | `sha256:60f26ac3e12376e8eb3cd0321e04baf3526a29d69cd0dbeff727b08ea9b2cd50` |
|  `18.20.2-dev` `18-dev`             | April 29th   | `sha256:058f8a92b113282bfe45ff2ce2be7d1b06e1852cc1c3314b54b5eeca9fe1e810` |
|  `latest-dev` `22-dev`              | April 29th   | `sha256:6e816deb4638513d501c438e53d5a71ca6446951a2d4573dd2300e4430e70a91` |
|  `18.20-dev`                        | April 29th   | `sha256:494e6a7a1c52f1d7d493d072e4273cab4291179a6e7238b1131addf9b36b48c4` |
|  `18.20` `18.20.2` `18`             | April 26th   | `sha256:5790c8699577f778f8e691d62a080355da117db29596a489fd6093dac74ad4fe` |
|  `latest` `22.0.0` `22` `22.0`      | April 26th   | `sha256:de57f7aee7516bc268e8afb190056ecc2d08ae666d18f9f040d3e8e29905b55a` |
|  `20` `20.12` `20.12.2`             | April 26th   | `sha256:784635cc67bccfd2dd61261f83dfdc459005c29184080411488582ed378fbc26` |
|  `next`                             | April 26th   | `sha256:fe112af7c98149bad13eaeeacacec5ac561f76349d06ec571832b476688d8765` |
|  `21.7.3` `21` `21.7`               | April 26th   | `sha256:7092934c1ccba70e209b1c4a147ed786fe1a910e58f45e07815ab22c5a410f6b` |
|  `21-dev` `21.7-dev` `21.7.3-dev`   | April 26th   | `sha256:fc751328e8521e58f88c8be282a266106f96c97d164d7af9246b6d77751d5e7e` |
|  `18.20.1-dev`                      | April 9th    | `sha256:d754b4ac7941229753008026b8e4ae14bac29e0a7d3f2388b2ee23945fb7e24c` |
|  `20.12.1`                          | April 9th    | `sha256:13a239cc5bb1fba4cc90e7f3796ace78930915c61f8f3b5a9c9c25df8d4d12a2` |
|  `20.12.1-dev`                      | April 9th    | `sha256:2de522e612d199b6df72b706d371f0e3a206d5bbd5f8f721c006fa4af5c67c1f` |
|  `18.20.1`                          | April 9th    | `sha256:ce2b68aaeccef49e3c7ee87d031ff52010c376bf99424d9d08251a503354adbc` |
|  `21.7.2-dev`                       | April 9th    | `sha256:12fde7eb020635684cd9e9e550e4826656c1006f5b549210048a79a8c6c9c25b` |
|  `21.7.2`                           | April 9th    | `sha256:f17c4a90e196a4fa7047ae64c1629e3577ebd45470029a1970a9c1a5a86aa529` |
|  `20.12.0`                          | April 3rd    | `sha256:b0b755db7dd968c07d9a75d51b4b3764679bb1183a629314837cc143b2b486bb` |
|  `21.7.1-dev`                       | April 3rd    | `sha256:1dd2ea1fc6f4d70d6560c3cd869fa7f4168556f0b4f22535998c690a2bea5767` |
|  `21.7.1`                           | April 3rd    | `sha256:fbd0d7df25026770d73c3260f9f84592f1aabc592bca01b9714b2461f7e09a42` |
|  `20.12.0-dev`                      | April 3rd    | `sha256:47dc806dbacd5f8c0dc9541cde1fdfbedead308f4a9bbb69d448b8cbaad2c072` |
|  `18.20.0`                          | April 3rd    | `sha256:8aea9f756f30e3e962b1823c9b1093740c67cf8c2dcb5b855b3516e3a7f55bf4` |
|  `18.20.0-dev`                      | April 3rd    | `sha256:1d690ca26b47f51ffc42346a74229e59d6b862eca58e2e4bf4de75b78a1cd6c1` |
|  `16.19.1-dev` `16.19-dev`          | April 13th   | `sha256:bba7820a61df3f1a8560ed8e58cc472b63bde7211a28c53408ddc037de324b39` |
|  `16.19.1` `16.19`                  | April 13th   | `sha256:3cb3f6b898f8cd15aea39688a54a20035e0f62fed358799fcd162283f535bb54` |

