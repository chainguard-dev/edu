---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-24 00:45:45
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
|  `openjdk-17-3.9` `openjdk-17-3.9.6` `openjdk-17` `openjdk-17-3`                              | May 23rd     | `sha256:3648dd4fadc0e7d172a41d716b24abed3467a22db5a8620ee70ef28a02dd48ba` |
|  `openjdk-17-3-dev` `openjdk-17-3.9.6-dev` `openjdk-17-3.9-dev` `openjdk-17-dev`              | May 23rd     | `sha256:829394033a32642ee23b27f4424401b213fc3c6eeb6c22be8d518ec15a84ee18` |
|  `openjdk-21-3.9-dev` `openjdk-21-3-dev` `latest-dev` `openjdk-21-dev` `openjdk-21-3.9.6-dev` | May 23rd     | `sha256:490d30a5ba19c16a727746c558ac9cd2b91d438fc27fc7047850694f8e45aaa1` |
|  `latest` `openjdk-21-3` `openjdk-21-3.9` `openjdk-21-3.9.6` `openjdk-21`                     | May 23rd     | `sha256:5404b9223f49fe8698cd1788ab2bfa015f6a55d33ce5858dfbe624659b4d039a` |
|  `openjdk-11-3.9-dev` `openjdk-11-dev` `openjdk-11-3.9.6-dev` `openjdk-11-3-dev`              | May 23rd     | `sha256:b248f77a662c061d84d2e801c235d2ecdf37200a51dc394e149e544d1d245112` |
|  `openjdk-11-3.9` `openjdk-11-3.9.6` `openjdk-11` `openjdk-11-3`                              | May 23rd     | `sha256:fd68a6c5a7e35fdb2ca563f7c8d5ac9e38cbbb9cde1326d8d730f198169b1c37` |
|  `openjdk-17-3.9.1`                                                                           | May 13th     | `sha256:0e4eaeb21b03f72e24767d4696b49935cd6b8838852d89e5243ba19fee27afc8` |
|  `openjdk-11-3.9.1`                                                                           | May 13th     | `sha256:617690269a5361add65e7ef9ed24d5daf94300c5728c41d796a92b680d7d5b41` |

