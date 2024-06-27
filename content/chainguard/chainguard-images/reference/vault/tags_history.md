---
title: "vault Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vault Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-27 00:41:27
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
|  `latest-dev` | June 26th    | `sha256:7d0362e65ba414447e71051a8a73eb9e71f013bf2a0dd146e399406027026f81` |
|  `latest`     | June 21st    | `sha256:f3bc598b1e1428471861d75269e3e5058634d798adfca1088001fc6612ba5183` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.15-dev` `1.15.9-dev`                      | June 26th    | `sha256:b1a4ac829169848a02661f63236771cc61c78c6766ba1189ee1ec24bbec5cacd` |
|  `1.16.3-dev` `1.16-dev`                      | June 26th    | `sha256:a79f6396e3ae4834fbc64422f3c9d619a37ac265c3635e6faa8ae4d388dab95e` |
|  `1.17-dev` `1-dev` `latest-dev` `1.17.0-dev` | June 26th    | `sha256:a52979d3cff4c459cd83f570349bb0de82cdc232b11ff8f726fe2a37b13cb5e9` |
|  `1.17` `1` `1.17.0` `latest`                 | June 26th    | `sha256:190c41164227fbcc350457c034ebd16b93ecb44468b1bdd6f9f086dd19ae15f5` |
|  `1.15` `1.15.9`                              | June 25th    | `sha256:f71113d2e3c94cdf3a278cccf296387ddea9d933be57f71a77dd61c774a96079` |
|  `1.16` `1.16.3`                              | June 25th    | `sha256:913f54c94230a027e454601e3cd9befb61d34d5941ead77710b87593b6007d08` |
|  `1.15.8-dev`                                 | June 21st    | `sha256:2aa0772ef8f77ee9cd5c96e55674b1be3aad54752f56e51c8dd6844cf83a4161` |
|  `1.15.8`                                     | June 21st    | `sha256:b803e534c5a02cdd9827b3e8ddb59c5d98f18e73442a8c9e2b5c58ddf8e07d71` |

