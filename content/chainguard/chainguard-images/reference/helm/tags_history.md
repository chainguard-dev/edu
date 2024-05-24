---
title: "helm Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the helm Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-24 00:45:45
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/helm/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/helm/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/helm/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/helm/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 23rd     | `sha256:41bbd999f702598a23ab1963295f11e018ca512c360d85a2b55fbdbdde900723` |
|  `latest`     | May 23rd     | `sha256:28ca85efed288af82b249a2f0c404e1f5fbc3b5b36e5bcb86d9f381dad6968a5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.15.1-dev` `3.15-dev` `3-dev` `latest-dev` | May 23rd     | `sha256:ca00ba4bdd1d54feaf152a7986f30a25a1d423f7aedced2604fd5f1b492a835c` |
|  `3.15` `3.15.1` `3` `latest`                 | May 23rd     | `sha256:959cc82ec8b0f6a91ffa7d4f093869ec4f364dc2ec49d45ab00da34ddffa2f0f` |
|  `3.15.0-dev`                                 | May 23rd     | `sha256:57141c2c7d62410f664f2738075a451c585c509bb631585cf1b648dddd5f15f3` |
|  `3.15.0`                                     | May 23rd     | `sha256:5d4a9bfb76c4d761feae968a8a509fc49d19a1fb113334ffa1c29c073503f84f` |
|  `3.14.4` `3.14`                              | May 15th     | `sha256:0c177fb85d6a7f3fc6f3de13db8322905b5ddeb2fdea2113a68b5bf5ddcb8bdb` |
|  `3.14-dev` `3.14.4-dev`                      | May 15th     | `sha256:b719b4a6efbece5213320216dc6004777a23a3f73b4cb8b16fe88178525d096f` |
|  `3.11.3-dev` `3.11-dev`                      | May 13th     | `sha256:d19f95e05b32385f5bad1aabd0d3da598752a530f9b0bb9abed33ed96c17bbae` |
|  `3.11.3` `3.11`                              | May 13th     | `sha256:0ea603774d017c1a29e5664a95cfa1eab62906d8f13b2a508a55bf331254a248` |

