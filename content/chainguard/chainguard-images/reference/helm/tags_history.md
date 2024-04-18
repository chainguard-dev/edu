---
title: "helm Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the helm Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-18 00:43:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/helm/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/helm/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/helm/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/helm/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | April 17th   | `sha256:39c5777433e44c4501ffb0e5e8f49443bfdd0fe928115a769d9d7d820a2dc7a5` |
|  `latest-dev` | April 17th   | `sha256:c1906469de8d7ffb6a65d272b65be5f465bf9bc3e2a30e5a22b389c521dd0827` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3-dev` `3.14.4-dev` `3.14-dev` `latest-dev` | April 17th   | `sha256:812f5c17e6d92310498535444be6e1db25c8683a6860180855baaa930f59ba61` |
|  `latest` `3.14` `3.14.4` `3`                 | April 17th   | `sha256:aa502942671d8a9149a6470c8539fc0b3f8c6d72e7734001e5ceb1fe68c19fa5` |
|  `3.14.3-dev`                                 | April 9th    | `sha256:16447f5c4665f8cc9a60db890de8f689b9a055921b95412921900e3e255b44c2` |
|  `3.14.3`                                     | April 4th    | `sha256:c57cd32451be1e94046f2359a2edaac2b84e4ecd52b8af40d74c623485302b1a` |

