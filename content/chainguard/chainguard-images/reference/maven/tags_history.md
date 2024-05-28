---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-28 00:45:11
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
|  `latest` `openjdk-21`         | May 23rd     | `sha256:d403d817191244b55bf8f5a111db8e1378e62bcfde5f648f0892becacce6b66b` |
|  `latest-dev` `openjdk-21-dev` | May 23rd     | `sha256:d06ce216c01a65c65c2883b39206800cc652db04b907fd8b2a3dbc6bf8c70f70` |
|  `openjdk-17`                  | May 23rd     | `sha256:dabacdce1f56624bc2a00b6d0843ada9748ac07c7992e683c18254f10f22c569` |
|  `openjdk-11`                  | May 23rd     | `sha256:5da8e1cbd88f17c75e391d76e7e892dfeb019fcc561dc8792373fba993c34e59` |
|  `openjdk-11-dev`              | May 23rd     | `sha256:b50dae041101f9730ed47635f2add6b52d77c98a0cff24c526a17edc47686e16` |
|  `openjdk-17-dev`              | May 23rd     | `sha256:a6848e8f13da039d402771130030895bed0397f5fc9b15d68647c85e4de7215e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-21-3` `latest` `openjdk-21` `openjdk-21-3.9.7` `openjdk-21-3.9`                     | May 27th     | `sha256:5e71a873104a27d2d1bbe3481ceb5b1077c2b47b8f4b252e63cedc965f07e437` |
|  `openjdk-17` `openjdk-17-3` `openjdk-17-3.9.7` `openjdk-17-3.9`                              | May 27th     | `sha256:d84b760735810220f5554b9184ded749703574b5fc7e22b12326da3fe4e644e3` |
|  `openjdk-21-3-dev` `openjdk-21-3.9-dev` `latest-dev` `openjdk-21-3.9.7-dev` `openjdk-21-dev` | May 27th     | `sha256:5c99c97465d6a590c5d642829c1efaa87a7beb5dae3945bfcbbaca4ef970820e` |
|  `openjdk-17-3.9-dev` `openjdk-17-dev` `openjdk-17-3-dev` `openjdk-17-3.9.7-dev`              | May 27th     | `sha256:dc59ccc46145071ed007696aa0f5972b2b52febd6d04bb4f7ae14e3028ef88f5` |
|  `openjdk-11-3.9` `openjdk-11-3` `openjdk-11-3.9.7` `openjdk-11`                              | May 27th     | `sha256:4b522f52859fe7264be2dc976668ec77ca19e6bd13c345c3fcb80fca0962f240` |
|  `openjdk-11-dev` `openjdk-11-3.9.7-dev` `openjdk-11-3.9-dev` `openjdk-11-3-dev`              | May 27th     | `sha256:1587b09c04b588570070b202fdbd93b5f56835fc1156a53b1f3c0c31dd68ee47` |
|  `openjdk-21-3.9.6-dev`                                                                       | May 24th     | `sha256:41a304153886d639b5a4bd7252ebb424b45f5a2643621e01e52e235517d53677` |
|  `openjdk-17-3.9.6-dev`                                                                       | May 24th     | `sha256:cf79812c268bed86ddd82b10daad0d00ff26dab42683748f999b06c33f8b79eb` |
|  `openjdk-17-3.9.6`                                                                           | May 24th     | `sha256:f66fede4dc6e40733a5fe4ee3aa305d1661d8c4489cc0e284e094ba7d047516d` |
|  `openjdk-11-3.9.6-dev`                                                                       | May 24th     | `sha256:2088c7722de52417f78eefa527cf0f98bbbcfeb55255d884fc92ff134fefee49` |
|  `openjdk-11-3.9.6`                                                                           | May 24th     | `sha256:5d4d3884b01eaadddee1df3da6bec97a65d8cb5da746fd15eb0c180f004f82a0` |
|  `openjdk-21-3.9.6`                                                                           | May 24th     | `sha256:8d06f826321c7c588b896feaeb89cdda13d3d4793f60fb28ec38405b7a522b45` |
|  `openjdk-17-3.9.1`                                                                           | May 13th     | `sha256:0e4eaeb21b03f72e24767d4696b49935cd6b8838852d89e5243ba19fee27afc8` |
|  `openjdk-11-3.9.1`                                                                           | May 13th     | `sha256:617690269a5361add65e7ef9ed24d5daf94300c5728c41d796a92b680d7d5b41` |

