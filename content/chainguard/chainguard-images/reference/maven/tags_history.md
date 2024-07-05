---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
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
|  `openjdk-21-dev` `latest-dev` | July 3rd     | `sha256:4f77794d43edb89da8211befccdb29554b3610f5fa5e7d070b6c0fc037ebed02` |
|  `openjdk-11-dev`              | July 3rd     | `sha256:dfe3dcb59acfec3c14f2cae7a2e547cfbbe685b91b05b7cebc2b34ea70102679` |
|  `openjdk-17-dev`              | July 3rd     | `sha256:0b7cc9259b02fdabd14282630bf1fedb5aaa3f4b8a8e8d45c31e70e0ee6e6778` |
|  `openjdk-21` `latest`         | July 3rd     | `sha256:597d7484f4dd165b177cffad41ee3299bcb363c4308ee912944c42612eb70247` |
|  `openjdk-11`                  | July 3rd     | `sha256:e846d3cbf09b9ab80ccf0c127cbff245dfa9d20ad223acf047aefc78bf60b3f9` |
|  `openjdk-17`                  | July 3rd     | `sha256:4445de497f6b7e00dcf6e3662c984a1cffc30401b1990a98a0ada39f0d403c0f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-17` `openjdk-17-3.9.8` `openjdk-17-3.9` `openjdk-17-3`                              | July 4th     | `sha256:67fe1e27d9ed0d87ce9e4c451e07788ff7afe2d45b6324646add4f63e3608912` |
|  `openjdk-21-3.9.8` `latest` `openjdk-21-3.9` `openjdk-21-3` `openjdk-21`                     | July 4th     | `sha256:7766231b49dcac82ab5938c02d885be224434dfae47f329495a7cd65e49a7b83` |
|  `openjdk-11` `openjdk-11-3.9.8` `openjdk-11-3.9` `openjdk-11-3`                              | July 4th     | `sha256:c56c95d637187ba54e08afacd10861dd784f6aa30f653b9069ff427edce42fcc` |
|  `openjdk-11-3.9-dev` `openjdk-11-3.9.8-dev` `openjdk-11-dev` `openjdk-11-3-dev`              | July 4th     | `sha256:3bc63f0590bf5200b72c62ecf9420431a0d4df70afc0d12ff3e76b8c2219e8a2` |
|  `openjdk-21-dev` `openjdk-21-3.9-dev` `openjdk-21-3.9.8-dev` `openjdk-21-3-dev` `latest-dev` | July 4th     | `sha256:2d5b5833bac92e3c462e4ceb7058975dd0659d2460d5347d5e9e47f6f16397a7` |
|  `openjdk-17-3.9-dev` `openjdk-17-dev` `openjdk-17-3-dev` `openjdk-17-3.9.8-dev`              | July 4th     | `sha256:288cd9d6461385f85528640938488555a069101205ee72cce717e87781af1176` |

