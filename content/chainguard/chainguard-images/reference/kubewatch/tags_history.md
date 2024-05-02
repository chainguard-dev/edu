---
title: "kubewatch Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubewatch Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubewatch/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubewatch/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/kubewatch/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubewatch/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 1st      | `sha256:f820d8719e5d934fd5356ea1d7c766cdeb17a7e0cfa8b724357fc33d7f0e5cb2` |
|  `latest-dev` | May 1st      | `sha256:571dbd7dc5d3c324194bf687fe25aba54d0cb0084308ad440f15a9d2fc51a575` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.6-dev` `latest-dev` `2.6.0-dev` `2-dev` | May 1st      | `sha256:7de1803382dabb7965aee04c98532d3a37ae7c7817e2735a66c302b5cdde07e9` |
|  `2` `2.6` `latest` `2.6.0`                 | May 1st      | `sha256:5ea1697703226e5c5ee47b4c7e3f2e9ff88674eb2f86a08dad26379def902f55` |
|  `2.5.0-dev` `2.5-dev`                      | April 30th   | `sha256:2b2b1ad2fcf6aa504ce03ca74c9dd7c52145617bd0acd9774d9fd495dd135e03` |
|  `2.5.0` `2.5`                              | April 24th   | `sha256:6345d0bcd6c021e082664a5bb63e255852fd318a6b8132f94407c7d3c8466425` |

