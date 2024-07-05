---
title: "vault Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vault Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/vault/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/vault/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/vault/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/vault/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | July 3rd     | `sha256:890366f5c7fd6a1482873ba65d6dc2d0eff52201b78b78a917fd847ef55ac5f2` |
|  `latest-dev` | July 3rd     | `sha256:031759c9eba0bdec8eb3eff73493a3cb309d92b7b97e3071b6c7686c2b735b3e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.15.9-dev` `1.15-dev`                      | July 3rd     | `sha256:7f12a588ea777548bf81e757bc6e0e0bc953d1f9b2cc7cf1457a6aba9ee31226` |
|  `1.17-dev` `1-dev` `latest-dev` `1.17.1-dev` | July 3rd     | `sha256:094b83d34dc5b3f9228604fca5a804bb6c83a80c752cc1b12cffec14e2c8a746` |
|  `1.16-dev` `1.16.3-dev`                      | July 3rd     | `sha256:0fef2dbfa01bf8dc4eb7d8a3c2653a593e2811a0daabd6febb3290fd94c221ab` |
|  `1.15.9` `1.15`                              | July 3rd     | `sha256:4912910ed790cc3e24f681b950310b54c07d967f3f4aeb708b64525276e676a7` |
|  `1.17.1` `1` `latest` `1.17`                 | July 3rd     | `sha256:1abfd38c2684c12a97f7e7e1e00fa8612b4ebfa1cb19c0fc2d060cff5115146d` |
|  `1.16.3` `1.16`                              | July 3rd     | `sha256:64bc11df3b072eb40e64bbee715ee57cef447ccba7c3be1c8af84eb501ff2fc2` |

