---
title: "node Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
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
|  `next-dev` `latest-dev` | May 1st      | `sha256:1f66eaed294bea6f1cda5cc329f742d616391b546479539fe7174e72acc12b5c` |
|  `next`                  | May 1st      | `sha256:2dd0f5187526c076286f9116d594b645c1f9fe0b464900909cdc258e27b1fb62` |
|  `latest`                | May 1st      | `sha256:93f83da3f114560add234631601fddf98a36421bc87960f8d4f2be7fd108bb94` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                   | Last Changed | Digest                                                                    |
|-----------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `22.0.0-dev` `22-dev` `22.0-dev` `latest-dev` `next-dev` | May 1st      | `sha256:d11edfdc17e745aeadc8bfc6a7b917b9f2ddce18666b769fd7e68e7cc99485ad` |
|  `18-dev` `18.20-dev` `18.20.2-dev`                       | May 1st      | `sha256:8cc29346a55c4c951cd76114ca839e299470fcf3eb39877ec9bd07f112e7a2d5` |
|  `20.12-dev` `20-dev` `20.12.2-dev`                       | May 1st      | `sha256:d32c48e1c3a91017abd8e80926bf32248a363a1d0120bcef16dc222ea6a0dd95` |
|  `22.0.0` `22` `latest` `22.0`                            | May 1st      | `sha256:8ef20399b2bb8030975d7a5049e00c3adab86fcb79e1a7691a500d357b61c9b3` |
|  `18.20.2` `18.20` `18`                                   | May 1st      | `sha256:0702090077f5f89561aa8c05b8f8a0162c4416002d5ce10569653d4083fd5200` |
|  `next`                                                   | May 1st      | `sha256:39d87f05d3f5e8c543d24e628c3ce2f8f437999d006e185dccccd47edb89eee6` |
|  `20` `20.12.2` `20.12`                                   | May 1st      | `sha256:ffea539f3ebf2985b37e043ae6a96e3d436e65a5a84095b07c5dc8aa6ec03517` |
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

