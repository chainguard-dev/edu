---
title: "cilium-agent Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cilium-agent Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
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
|  `latest`     | May 1st      | `sha256:6928cbbf2fdeb8e2441cb39b83e793a193326b8f3768693eba81e63c8e0d59cc` |
|  `latest-dev` | May 1st      | `sha256:f854b0eb8ec5962e2e473ce869504a497a26dce9ee9d29318c489e2c0a4b5f7f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `1` `1.15.4` `1.15`                 | May 1st      | `sha256:8a86f1dc4d5eb51d58d250080bc72db8f5bdc4fab7d8f236e36a2dfdbcf124cc` |
|  `1.15.4-dev` `1.15-dev` `latest-dev` `1-dev` | May 1st      | `sha256:c073884c458e1624201a1d151581f49e9db7fb946895ad7632b656d29f12d7c2` |
|  `1.14-dev` `1.14.9-dev`                      | May 1st      | `sha256:d3d2a6e185516b21fa76088edf0e5032fba020a0c05b532a82eefbf436f4f001` |
|  `1.14.9` `1.14`                              | May 1st      | `sha256:6aeeabe5c1b095a3f6ee7da3dfc02357e47fe958ab29a600e861a8fde2acb4fc` |
|  `1.15.3-dev`                                 | April 20th   | `sha256:49d0ba2bf91cb7edaea6825c1bc2d6d915e837a7913c006936b89570c51f0d04` |
|  `1.15.3`                                     | April 12th   | `sha256:ef366e247fd6178adde6f4cd2b062dce016b3abe6ffd7e4f99579d1a7e722ecd` |

