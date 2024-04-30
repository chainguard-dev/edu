---
title: "helm Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the helm Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-30 00:52:22
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
|  `latest-dev` | April 29th   | `sha256:03308104af228ed4b5d00c2ed4e17d8e56bdb475cc6443b88b240ec965b51714` |
|  `latest`     | April 21st   | `sha256:f0c3372f6d5f7e35f635661d75b6e6259e26a34817c984eb4ccf6806c78f4385` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                          | Last Changed | Digest                                                                    |
|----------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev`                    | April 29th   | `sha256:a32f30e8530b54e6f06b8ed90225fe91ed2dd0a43bf4bfd5565199037bdaf1aa` |
|  `3-dev` `3.14.4-dev` `3.14-dev` | April 29th   | `sha256:32656d4c33599fd1340c28b3f0ae353276afa67be130da63ae8095355225489c` |
|  `3.14.4` `latest` `3` `3.14`    | April 21st   | `sha256:5c60f522f56cf99a20c82de3d020c89a7aa89a71a3c3d4d4ccb2a176d6af58f4` |
|  `3.14.3-dev`                    | April 9th    | `sha256:16447f5c4665f8cc9a60db890de8f689b9a055921b95412921900e3e255b44c2` |
|  `3.14.3`                        | April 4th    | `sha256:c57cd32451be1e94046f2359a2edaac2b84e4ecd52b8af40d74c623485302b1a` |

