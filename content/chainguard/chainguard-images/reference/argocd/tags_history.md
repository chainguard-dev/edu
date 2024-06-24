---
title: "argocd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the argocd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-24 00:43:49
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/argocd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/argocd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/argocd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/argocd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 22nd    | `sha256:85ff129fd00f70820593613280ece717b1f7555389a9e8bca7a98ac66ecb69ec` |
|  `latest`     | June 20th    | `sha256:2419508878d181620f1b8d4e5ff07b35b5c1592146815900624ec5f6fa3e1cf1` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.8-dev` `2.8.18-dev`                        | June 23rd    | `sha256:b31c1351ffd99f59e023edf8b569e8fa39ed52d7d6fee38272430f48d3a8d215` |
|  `latest-dev` `2-dev` `2.10.12-dev` `2.10-dev` | June 23rd    | `sha256:f3b6be8c98591e77741832ca707db2e66e8a83aa08a6024a8ae9ec37fa44ac94` |
|  `2.9-dev` `2.9.17-dev`                        | June 23rd    | `sha256:2f84ea01b8144dbf1c4420f06baa253c0ff6eb1bb1452f3d97aca5dfcec4b533` |
|  `2.10.12` `2` `2.10` `latest`                 | June 20th    | `sha256:1ba55a7f42f802daf231d417263ba530c4191525746ce6cdb2a5bb393d59dca3` |
|  `2.8.18` `2.8`                                | June 20th    | `sha256:83cf4f6a04c977dea2cb1026560ffd6609c38015ab2318957481c1af0ecee724` |
|  `2.9.17` `2.9`                                | June 20th    | `sha256:85782215de24927bce530e444afbd15239fb5354b65fa632d285c710f6d30b89` |

