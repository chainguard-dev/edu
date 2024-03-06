---
title: "go Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the go Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-06 00:47:02
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/go/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/go/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/go/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/go/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | March 5th    | `sha256:a0973622ed0bb3e5a9d5c990598bfb79102b55b155120737a0c30e52d2514be6` |
|  `latest-dev` | March 5th    | `sha256:5959c19f9d1b84c6b51c3afd6b7ffd17df423420958c0bc0e8120887e835c430` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.22.1-dev` `1.22-dev` `1-dev` `latest-dev` | March 5th    | `sha256:b8fe38817f0dd9a0b8aa3ed1f6cefe63fbc25ea51b46e0ecbfe67f2ad4a1104f` |
|  `latest` `1.22` `1.22.1` `1`                 | March 5th    | `sha256:3a6918dc95c61b5ba9d3b735b21047d4a1dc55e80c16f6ec15e390c95700172a` |
|  `1.21.8` `1.21`                              | March 5th    | `sha256:b28206d787234e27aad3634e43350eda05d18641d52182d2b406e06a8044302e` |
|  `1.21.8-dev` `1.21-dev`                      | March 5th    | `sha256:87b86f1b7656f36cdd805557dee195b4acbde864a3e94c8582c9f129349414c0` |
|  `1.19-dev` `1.19.13-dev`                     | March 2nd    | `sha256:448b0f63869614e26ebe9cee47dc3674875169f9b202a391f4e116b191e1f422` |
|  `1.20.14` `1.20`                             | March 2nd    | `sha256:d0bd72167ba2c2dca757656e217dccdd25dff48d9cd485a32aaaf6da3d3795e6` |
|  `1.19` `1.19.13`                             | March 2nd    | `sha256:1e6d927948af40c39de099bdb531dc9979ee5bfdfefcf5f51fe8ee6f31f9f3b5` |
|  `1.21.7-dev`                                 | March 2nd    | `sha256:cac3921ec9326b36a84a6c254fa511e78862e75b645511e7f3b2cb74f0ea3a1c` |
|  `1.22.0`                                     | March 2nd    | `sha256:45ec7a1554f871b4996710cb1ba30bddc4800167cff2cb3019811fc0c1bcb190` |
|  `1.20.14-dev` `1.20-dev`                     | March 2nd    | `sha256:6c8027a017d2b55efec5c3176e75274a9ecf0ce7bff051092db8dde403bb4ae0` |
|  `1.18.10` `1.18`                             | March 2nd    | `sha256:a1cf4a0402e813182b6c56ffade19324e0d23baf4944091048b973e3df87e442` |
|  `1.21.7`                                     | March 2nd    | `sha256:4cd3941d250a7d12b704414359e1eff51e681059e5e2233cabe2dbcc92d599a8` |
|  `1.18.10-dev` `1.18-dev`                     | March 2nd    | `sha256:90b699e31af3133d07c9ed7835f9a43719894a31328cd0074046e7cb80899956` |
|  `1.17.13-dev` `1.17-dev`                     | March 2nd    | `sha256:28de74c0d9ffd3249d525896716c79c502682b3c36a3cfb36898ddbf86eca7f5` |
|  `1.17` `1.17.13`                             | March 2nd    | `sha256:ca7d098fc26dfe7cf47a6581cff5621b77221d3040f4da6cdb116b9f5953d995` |
|  `1.22.0-dev`                                 | March 2nd    | `sha256:c9d4cdce29448d393fb9f4ded60bd34b7bad3eebf06e3458bad6737ae4cbb263` |
|  `1.20.13`                                    | February 6th | `sha256:887b1a0422d708cc2a07790c0db892d0c3dafe79965db097237a1641d121d2b8` |
|  `1.21.6-dev`                                 | February 6th | `sha256:c3780b612d08c0d1f29083d8879af21f51996c8f092760e2ffd87e1d7a8bdedb` |
|  `1.21.6`                                     | February 6th | `sha256:662c24a008e188f31732094110aafcc69ce8d950718f000b1f3f95e7b8565eb4` |
|  `1.20.13-dev`                                | February 6th | `sha256:f079dbf6550548240ca96175a9b266b9e3d4954a5c1b5b1dda1ac140d37938c6` |

