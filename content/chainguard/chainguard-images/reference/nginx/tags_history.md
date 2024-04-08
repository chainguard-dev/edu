---
title: "nginx Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nginx Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-08 00:38:35
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
|  `latest-dev` | April 5th    | `sha256:59fe7420c51202120085a82e27f37b5df56b186bf8641165625b804980a6eaaa` |
|  `latest`     | March 28th   | `sha256:63dad1734b3df67923f7cb15c1d7c6761a2a0b25f61a1760920c6806eac47846` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.25.4-dev` `1.25-dev` `latest-dev` `1-dev` | April 5th    | `sha256:995ab115537a93acde8f4cb45482eb924edc8fa812ed636fa06f1e7160aecacb` |
|  `1.24-dev` `1.24.0-dev`                      | April 5th    | `sha256:c6ed7770b72ad77ab43a9294ec728a2d02aa6d1fe1d489e8f5bab57b9d710f2c` |
|  `stable` `1.24` `1.24.0`                     | March 28th   | `sha256:317307e2dfb783db56b11440c54e3a3283391a4453693ced5227b26826c0cf2d` |
|  `1` `1.25` `latest` `mainline` `1.25.4`      | March 28th   | `sha256:28c7121d3c19d361f3639ab33891246dab9e8c21cc007b10826fb354e4f56732` |

