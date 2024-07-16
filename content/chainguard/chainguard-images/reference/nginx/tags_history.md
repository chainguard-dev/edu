---
title: "nginx Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nginx Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
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
|  `latest`     | July 8th     | `sha256:bf809d99103744036e922fe9b3c4c027c6019b46c9fc1bb561fb7d119760fbce` |
|  `latest-dev` | July 8th     | `sha256:785862950f3af7250e2b586d16ffcb30a4287304abcb70ec67f5a313116c3d02` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `1.27` `mainline` `1.27.0` `1`      | July 8th     | `sha256:9f772d70938b1c1bcdfab460c181789b228f969a51238e7aa212a537c7a649c1` |
|  `latest-dev` `1.27.0-dev` `1-dev` `1.27-dev` | July 8th     | `sha256:ebb440f1d6912b77140ab4e08d876f1b2f0a0c9df4bbd13e6a1a4bb7d6e621ca` |
|  `1.26.1-dev` `1.26-dev`                      | July 8th     | `sha256:146f837008c54f27857e5f3b5d05d7b4b23a6287ff53588dcc2da3172c0826cc` |
|  `1.26` `1.26.1` `stable`                     | July 8th     | `sha256:8d34adabb0e2ee0ce58c6f4887c9d9145eedb2174e9792efe1a5aa118b0b4b80` |

