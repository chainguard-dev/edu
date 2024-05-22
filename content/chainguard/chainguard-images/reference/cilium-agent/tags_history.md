---
title: "cilium-agent Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cilium-agent Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-22 00:47:17
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cilium-agent/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cilium-agent/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cilium-agent/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cilium-agent/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 21st     | `sha256:7a215afa5ed997e6e9f3f6ff577c3f815f0d38f34a21aa3e3e2f0ac9a979b284` |
|  `latest-dev` | May 21st     | `sha256:09959ef2afc2f76d23c805f42436c5a77b8e7c224e349101da750022572450f2` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.15` `latest` `1` `1.15.5`                 | May 22nd     | `sha256:ae40fdb6c111c9e4d38166153ebae3c9505525effd0f00d34f015962fe596aa1` |
|  `1.14.9` `1.14`                              | May 22nd     | `sha256:258e103bd692829db18d609eb7a05eee432c8074eae1a45f14ac625cd7c2147c` |
|  `1.14-dev` `1.14.9-dev`                      | May 22nd     | `sha256:eb7e949ef8f6562c0fbf0c0581c874fa4907181acc3a75ce2f26150c1d24c9ee` |
|  `1.15-dev` `1.15.5-dev` `1-dev` `latest-dev` | May 21st     | `sha256:e7da1dc124228dc85cfd231fffd85a2a3a279225d316bfe7952d4c95f9de2d68` |
|  `1.15.4-dev`                                 | May 20th     | `sha256:6a9af2ff0ac24ea376d102b63d6029801daaf20a69075c803cd80ff4fc065b2e` |
|  `1.15.4`                                     | May 20th     | `sha256:10a7d2e2b6e95210f3a3fd1fe9c39a6f7c49f5f648b219e75ed82c0664d47ffc` |

