---
title: "aws-cli-v2 Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the aws-cli-v2 Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-03 00:46:08
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/aws-cli-v2/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/aws-cli-v2/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/aws-cli-v2/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/aws-cli-v2/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | June 1st     | `sha256:088974e27605c95ebba86037624d96a4879482e2d5a3521c4b6e7eed480cc111` |
|  `latest-dev` | June 1st     | `sha256:e308ff192ddd2d1db2d45c40a3c5e67999bb2edf9e548f551093003b5e29dfc0` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `2.15-dev` `2.15.62-dev` `2-dev` | June 1st     | `sha256:44d3600bc22bad06e6d1adfc79e8f989e0c716f015ba6bac6f618c6190b2a48f` |
|  `latest` `2.15` `2.15.62` `2`                 | June 1st     | `sha256:121a99b2e6a6a6ae4300090ed793eb5cfe9cd7ab38f6f1e15a2f62bec79a1b80` |
|  `2.15.61-dev`                                 | May 31st     | `sha256:33d8840b1258ef127fd985c0d78e330328033927f1b8a3fc7ff7efba79675ecb` |
|  `2.15.61`                                     | May 31st     | `sha256:64dae9b16abf1903c3145176a723712d35717083847cdcf412cfc91b5f6e0ed6` |
|  `2.15.60-dev`                                 | May 30th     | `sha256:bb5922694132830c3391e98f38e7729942fe67788537d4b39f8c504a9f030a86` |
|  `2.15.60`                                     | May 29th     | `sha256:7b7c3d2294c29017daac519f3eafc9dc99ff117b4304247bd859b98a2b239ba3` |
|  `2.15.59`                                     | May 28th     | `sha256:c0238f37712f9b6b67a4e7777f465509eb59b7b5cfb8eaa96c8f2eb2af9416c4` |
|  `2.15.59-dev`                                 | May 28th     | `sha256:72198313320b195f16700182da174283516ed0a9864b0fd3ac5edec7b670bf31` |
|  `2.15.58-dev`                                 | May 24th     | `sha256:6d7aa70f4d31db0286de1b742e50ccabcb2ceea0e06b51bc1ec83c06ce0ef92d` |
|  `2.15.58`                                     | May 24th     | `sha256:405c8613e1446a9a6548b46bb581e91375ed2f0e7504d2e45fdd852eb7003e09` |
|  `2.15.57-dev`                                 | May 24th     | `sha256:d9b4a52765b32d729560da2f4300a10988e3752c0621a0440f3358dca73b2f6d` |
|  `2.15.57`                                     | May 24th     | `sha256:4dbc23ff91aee9c5cb520d871b235832b8f34a91f0a37d889ddd5a1289c4cd9c` |
|  `2.15.56-dev`                                 | May 23rd     | `sha256:c2ac4567de560dfb1ba492ee46278b371df34423ca2f9cedd17538f53d2a818c` |
|  `2.15.56`                                     | May 23rd     | `sha256:3e276a25b9f60eadb87f0ae95e6e1ca70b597e451d5084b072b9cfa0f59d1269` |
|  `2.15.55-dev`                                 | May 22nd     | `sha256:747c9487af49afdaa87bfcdcab3952183ab922b9c3ea7932399a3de0171b74a3` |
|  `2.15.55`                                     | May 22nd     | `sha256:7be4e542cde4fc6622213755fdde51492dd3940b5ac2cd6b04fa182e225360d0` |
|  `2.15.54-dev`                                 | May 21st     | `sha256:e124c842c7a4516a79586c0ac6928eb97a398189cebbba12dad2a85399eb8ea9` |
|  `2.15.54`                                     | May 21st     | `sha256:81575c2036689226e08f13289b47a088e2730f36b177099ef0a202aec80427aa` |
|  `2.15.53-dev`                                 | May 19th     | `sha256:d54a117d377795889dfae337fb7624d85849c856c14670e9d938ba2488f24a28` |
|  `2.15.53`                                     | May 17th     | `sha256:b1199ac36d8711e3f829d85fefb60bcffc3dca270eb8ed58332663716426efce` |
|  `2.15.52-dev`                                 | May 17th     | `sha256:0befa9a26dc4256c0dbcc515ee0e775ef0748095322411f3eb9c0b5ca7799648` |
|  `2.15.52`                                     | May 17th     | `sha256:0d35c9d3419bf34fb08de7ac7d6227d483438df2063b94b9234c7a5b02210fa3` |
|  `2.15.49-dev`                                 | May 16th     | `sha256:66e5270a5479d04f0f49cd309000b8488a12efb684486a9d45ead3592f998000` |
|  `2.15.49`                                     | May 15th     | `sha256:7234616fe4796cb16d35917cc8b10aec9af4fe948b5518920e3e10b8d3016aa2` |
|  `2.15.48-dev`                                 | May 14th     | `sha256:ec5f1c4717f4fa7b384246ee5252b41a2be0151cae954fdb9a19229da7cc7174` |
|  `2.15.48`                                     | May 10th     | `sha256:1c6af0016a8c72b9c5bc277023cbf75e16395ef35ce6a7ae953069a5eee2c047` |
|  `2.15.47`                                     | May 10th     | `sha256:c7d59a28e2a3c72dba7ab92f6d35dc3b8252c821648e1e2f4c72edebea4a19e2` |
|  `2.15.47-dev`                                 | May 10th     | `sha256:ed7384ea15985b49dfecbe0546883eba1de0c1fddde78341df82d28fdc33c36e` |
|  `2.15.46`                                     | May 8th      | `sha256:9cadf3551e3959ba97d155a8e22c2a64aef05a2f3c6bae67cf0e23cd9159d548` |
|  `2.15.46-dev`                                 | May 8th      | `sha256:80aac69e9f2be6b326ec5855dfa6d1837504c45bad4a0dc80a11664b33dccc8d` |
|  `2.15.45`                                     | May 7th      | `sha256:e3af0913ae22e3f6854fb984b222bc3d821fbed7aee2c550b1031b805df8ad63` |
|  `2.15.45-dev`                                 | May 7th      | `sha256:5ef09f8955b341d2bbb48b381af8345d217523d1827534d6eb34d055f63b1797` |
|  `2.15.44`                                     | May 3rd      | `sha256:0a8cbb77853b7846daaa14a13c3d44e3a0ed56503aa754a3abd02fff1073c897` |
|  `2.15.44-dev`                                 | May 3rd      | `sha256:245461a82d4e60eed173d6c02b408278c96578ae274ae5f0254942a12861fa18` |

