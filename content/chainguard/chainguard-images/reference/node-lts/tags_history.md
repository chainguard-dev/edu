---
title: "node-lts Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node-lts Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/node-lts/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/node-lts/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/node-lts/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/node-lts/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                  | Last Changed | Digest                                                                    |
|--------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `next-dev` | July 8th     | `sha256:e53b75a6fbf20bb4f8b94dd655d7f5acca5468b51282d9e9c484e1f8c9b31167` |
|  `latest`                | July 8th     | `sha256:afddf0f03f64d5294da6f18a7ea8987dc8ddc7613abeacde7130f003ecbc0eb7` |
|  `next`                  | July 8th     | `sha256:b9eb37fe24e43b7912100ee96acb5655068c0de5e8625b42bb833e2df753ede8` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                     | Last Changed | Digest                                                                    |
|-------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `next-dev` `20.15-dev` `latest-dev` `20-dev` `20.15.0-dev` | July 8th     | `sha256:a5338dfa62898eb0cc02795e7055e14b3643c4e8a2c917e17e1355c1117d2173` |
|  `latest` `20` `20.15.0` `20.15`                            | July 8th     | `sha256:672e7913414d36a3327b8677896f0b18e89f3a34261b68186aec663df6591023` |
|  `next`                                                     | July 8th     | `sha256:8b42142491c659a80648a5491e827f91e1ef842a22c57a25651af1c4a25a8742` |

