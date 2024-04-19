---
title: "prometheus Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the prometheus Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-19 00:39:27
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/prometheus/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/prometheus/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/prometheus/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/prometheus/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | April 15th   | `sha256:2f5cf2f15df52fa2e4bcd8ac529778eb73996aad41c60152a67c06f9f014bcca` |
|  `latest-dev` | April 15th   | `sha256:7bf2e4d07a37127b625e8e8a5747617497d011f8fc2d05b6190d9c389b288fb3` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2` `2.51` `latest` `2.51.2`                 | April 15th   | `sha256:1db7ea386ed4985ec5ed37828eac3c00c9b7963cc14a400767de477dabe88d7f` |
|  `2.51.2-dev` `2.51-dev` `latest-dev` `2-dev` | April 15th   | `sha256:375b110ef0056e8f5fa1ffefc52c33cf319c714ca94217ceccab7837bb1102f4` |
|  `2.51.1-dev`                                 | April 11th   | `sha256:ac5fad3af28009ea6ac0cd0c10437929922841c1e2366bcede317b404c40ad23` |
|  `2.51.1`                                     | April 3rd    | `sha256:fb4e4e90fa0c9fb812361eb8d9b4cce308b0ba8718b087ad7ad2fdc0b9db1cb3` |
|  `2.51.0-dev`                                 | March 28th   | `sha256:5307251a115475ae97e9de0d9eadc9db0d5d57a74f7dcd5e5128babaab1c3afb` |
|  `2.51.0`                                     | March 28th   | `sha256:35656141080195fb66243438845b8e03b3034901c81323bb59e13754e137d2f1` |

