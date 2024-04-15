---
title: "node Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-15 03:08:24
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
|  `latest-dev` | April 11th   | `sha256:eedcb3c9d3a41f4115c491cc805db2a1a38be607e5cd5a9e4021e7a0f7dad500` |
|  `latest`     | April 11th   | `sha256:947fe21f6b43c0a6cf801fbb827bd9df4ddbee756796dd37cd5192bfd8bb0106` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `20-dev` `20.12-dev` `20.12.2-dev`            | April 11th   | `sha256:2cf5fefc40e4c0167aa7f3a35dbb5dd3d52b923c55fcf93f0d8529b03c13a15a` |
|  `21-dev` `21.7.3-dev` `latest-dev` `21.7-dev` | April 11th   | `sha256:6688e001ec7677fd108b78afba8f4b3042bbf89b57d6e5c5d6c62410803828ba` |
|  `18-dev` `18.20.2-dev` `18.20-dev`            | April 11th   | `sha256:b0ac555c388b356140f36b90abd2a9543c3bc633b25359a950641d4743037784` |
|  `18` `18.20` `18.20.2`                        | April 11th   | `sha256:062fe274614d8072af1678e2bbf9f0b1c0c47b73b554af37c5817821b701b76e` |
|  `20.12.2` `20.12` `20`                        | April 11th   | `sha256:c7b691a81b7263689f31e6147d2f9df8b8939432c196007d169608c1cf1cf196` |
|  `latest` `21.7` `21.7.3` `21`                 | April 11th   | `sha256:3d5a6a8c05d2fce544d6f81bcc4176345812ef5a359959f5ff70c2471c83690a` |
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
|  `20.11.1` `20.11`                             | March 18th   | `sha256:87168b3d8f399b63df72266a0361c60eb0d5da1ea51d74f3fa07ff920ff22d07` |
|  `18.19.1-dev` `18.19-dev`                     | March 18th   | `sha256:98fa6f702f2afea1602c7e92b6a19008d074ef37d23472c2f6c18a7a35bcaa98` |
|  `18.19` `18.19.1`                             | March 18th   | `sha256:42a1d04e0644a7e831a04b9fe00338ab4edcac320bd38237412f3a336e3e0e72` |
|  `20.11.1-dev` `20.11-dev`                     | March 18th   | `sha256:dc0ea464ab3ef846c06d086c7df940384ea12a0c54ae59443cc8248d0d220098` |
|  `16.19.1-dev` `16.19-dev`                     | April 13th   | `sha256:bba7820a61df3f1a8560ed8e58cc472b63bde7211a28c53408ddc037de324b39` |
|  `16.19.1` `16.19`                             | April 13th   | `sha256:3cb3f6b898f8cd15aea39688a54a20035e0f62fed358799fcd162283f535bb54` |
|  `16-dev-dev`                                  | March 19th   | `sha256:a9a5c098defe64c18db8c783553535a791d65301023ba2210cd74da5ee37a985` |

