---
title: "wazero Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the wazero Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/wazero/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/wazero/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/wazero/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/wazero/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 1st      | `sha256:bac6590a918365e7d56d50962d83bab5747ce448ea74a49bf9089f312a17ec69` |
|  `latest`     | May 1st      | `sha256:15367959fffcbeabdb767a36cba81e7cbd69834a57034b109db0df648b2f56ba` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `1.7.1` `1` `1.7`                 | May 1st      | `sha256:1ec62134bbcff607b0d8a595247c33c99647e426972b4446bce568bbacbc9c2e` |
|  `1.7-dev` `latest-dev` `1-dev` `1.7.1-dev` | May 1st      | `sha256:5696d5001d95c9e18a64e4e6875f89f759ce63168f20ec416fd946f4a0912501` |
|  `1.7.0-dev`                                | April 11th   | `sha256:9b2efa0651ddb5d06207f230565fc32cd08dd489e98975891b719811083e790e` |
|  `1.7.0`                                    | April 3rd    | `sha256:0085750aebcf356339c8cf2c77d7ebab067aaae80414dd217c17ae52bb99233f` |

