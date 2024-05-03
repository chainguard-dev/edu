---
title: "prometheus Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the prometheus Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
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
|  `latest-dev` | May 2nd      | `sha256:da8389cf9b615e0b3d4594dae49070e798633801235e23eaf54eb89014380ebd` |
|  `latest`     | May 2nd      | `sha256:8427f4f8f8b5ead044b55bc395f48c92f07f83f0afe2efe3dea3eba1a4cb7202` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.51` `2.51.2` `latest` `2`                 | May 2nd      | `sha256:895c9858da4fadfdef7194a922a505b9009218f3f25a14c6b342dddd0d748c1d` |
|  `2-dev` `2.51.2-dev` `latest-dev` `2.51-dev` | May 2nd      | `sha256:71dfda0a4ae0bc84381c98fa99068c11221850cfd02782431db05119a76a6e12` |
|  `2.51.1-dev`                                 | April 11th   | `sha256:ac5fad3af28009ea6ac0cd0c10437929922841c1e2366bcede317b404c40ad23` |
|  `2.51.1`                                     | April 3rd    | `sha256:fb4e4e90fa0c9fb812361eb8d9b4cce308b0ba8718b087ad7ad2fdc0b9db1cb3` |

