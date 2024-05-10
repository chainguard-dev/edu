---
title: "docker-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the docker-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-10 00:43:45
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/docker-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/docker-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/docker-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/docker-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 2nd      | `sha256:01f7535ee76593a072be6aa5a1c8284da8c9ee1be73a81119daabed93351c4b4` |
|  `latest-dev` | May 2nd      | `sha256:1578b9db69cba76cfc204775a7420d8408b13e9d70545bf75d095868ab13007a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `24-dev` `latest-dev` `24.0-dev` `24.0.6-dev` | May 9th      | `sha256:fcc5b23d8bc281cc2e2d84c30c6b42f00edb5c3b66a69ad0a075ced22a2bbdf1` |
|  `24.0` `24.0.6` `latest` `24`                 | May 9th      | `sha256:78871446f31cf55ea33fac33195f6160c43133f39b6faf759acdf5f0787eb46d` |

