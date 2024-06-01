---
title: "falcoctl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the falcoctl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-01 00:50:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/falcoctl/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/falcoctl/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/falcoctl/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/falcoctl/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 31st     | `sha256:58ba08bf3b03dcf148b2184e8400c3c28a88ba6509881305e523acfb4c057269` |
|  `latest`     | May 31st     | `sha256:6b82283127f90c30fce609ed8a41c79eb93dec3cce8f88094da8f76bd8ef1998` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `0.8-dev` `0.8.0-dev` `0-dev` | May 30th     | `sha256:60bed289c309c0bf07b91e65bf8feb87358addc8bf0b897d2a9a781b9603260f` |
|  `0.8.0` `0` `latest` `0.8`                 | May 28th     | `sha256:b8b0fe834ce7f07fd7c26cac1349c71b3dff3649ddb6576e9fa6e7a2c3ce6e85` |
|  `0.7-dev` `0.7.3-dev`                      | May 24th     | `sha256:c576eb5fbc348c510085fe9c4abd79413f4aa99e7eb5f18803af2cfee24a8167` |
|  `0.7.3` `0.7`                              | May 23rd     | `sha256:27b0b4828bffa20ef6eba477eba8fcf2a7c60e29c5fc99df28126bc9e84e4659` |

