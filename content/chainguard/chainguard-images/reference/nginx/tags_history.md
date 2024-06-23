---
title: "nginx Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nginx Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-23 00:43:06
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/nginx/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/nginx/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/nginx/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/nginx/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | June 22nd    | `sha256:f0c926140831cde8a20bccd27cfe224c4d495fee3be66a2054b95f277283491c` |
|  `latest-dev` | June 22nd    | `sha256:5e6eaa41c4d3207e76bdf1163132eb9d43da19a5c95beeb2eb316d3f298ed46c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1-dev` `1.27.0-dev` `1.27-dev` `latest-dev` | June 21st    | `sha256:92fabf54ceb078e50eee884835fe930c8b8b3891d5840d4d0d551a6743505114` |
|  `1.27.0` `1` `1.27` `latest` `mainline`      | June 21st    | `sha256:15e7aafe5a7a267aef3db93b1e20f5a63d49a3c387a2be7a2bb194fe7e4f0c4b` |
|  `stable` `1.26.1` `1.26`                     | June 21st    | `sha256:794244f14deebdda98d6a1d7aa03eb9344dfa2fdc71debf52e44692f13330f29` |
|  `1.26.1-dev` `1.26-dev`                      | June 21st    | `sha256:b2eba76b29246505ae01f2c40b5276e5cbe0b669e64b4718f60dc13367df391f` |

