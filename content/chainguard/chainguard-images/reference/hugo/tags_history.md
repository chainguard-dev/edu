---
title: "hugo Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the hugo Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-03 00:33:11
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/hugo/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/hugo/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/hugo/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/hugo/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 28th    | `sha256:a714472d502f30dcb5c933fae246920920998ce24843b9fc8a456593d028e90f` |
|  `latest`     | June 27th    | `sha256:620b53a0612c2890d65ccb5107d209775794f415f30d4f1bbd7cfa95336af503` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                         | Last Changed | Digest                                                                    |
|-------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `latest-dev` `0.128-dev` `0.128.1-dev` | July 2nd     | `sha256:f291e9d86cc562418385e05c604a69f98aa735ae86b907a6c7a0260584b36fd9` |
|  `0.128` `latest` `0` `0.128.1`                 | July 2nd     | `sha256:737274022834c398e0103f9d6d9a701982de851fc5ee2ab095820d18205e9a75` |
|  `0.128.0-dev`                                  | June 28th    | `sha256:9b4f814e8f4a3c94247cbd2b2a67388a25c50bc4adff731a1cdd788255e180e6` |
|  `0.128.0`                                      | June 27th    | `sha256:d2f65e2936f9cfd09bb7acb9dbbd605e361aa2093c9f3b0005398061aa5b2d86` |

