---
title: "falcoctl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the falcoctl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-25 00:49:44
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
|  `latest`     | March 22nd   | `sha256:795af093b8391304ecb47aca5f3c06cde8fba337276e68973d0738223269b9cc` |
|  `latest-dev` | March 22nd   | `sha256:55d138e8d6dadb7b806276ebb11687a8f1cc9badec4467b93736f0b07e1cfc04` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0` `0.7` `0.7.3` `latest`                 | March 22nd   | `sha256:a85feac4d04221513a6f09a0c54f497c325911366d2ff520583e865b3ec8a0c7` |
|  `0-dev` `0.7-dev` `latest-dev` `0.7.3-dev` | March 22nd   | `sha256:c5777dd9c8546264c42600e6a9b759eddc9c5acc46cc7e5c55c20d7787154f96` |

