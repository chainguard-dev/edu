---
title: "etcd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the etcd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-27 00:41:27
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/etcd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/etcd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/etcd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/etcd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 26th    | `sha256:1b90edc5b33ae62112a2e969f49976784501534ede5adfc8b54998ba957f104f` |
|  `latest`     | June 20th    | `sha256:271c4f299e7821de28ed533451795fb4dc07146def24928c4b463608f0280ed9` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3-dev` `latest-dev` `3.5.14-dev` `3.5-dev` | June 26th    | `sha256:47d77b5ab83d1ff4fefee75fd0c6f0c929a79695412008d0e66e2798f362ba02` |
|  `3.4-dev` `3.4.33-dev`                      | June 26th    | `sha256:60da0d214286d2c1374a9cf84afc56b19382873f6c81536456077508086048a4` |
|  `3` `latest` `3.5` `3.5.14`                 | June 20th    | `sha256:c9a0078e178d3c7f7618317e7163706cc353bba77347db7c89f2815b0fb8aeaf` |
|  `3.4.33` `3.4`                              | June 20th    | `sha256:cebbe61e873d0365ac55ab8a3b2f8200f9dae275b64d4310ae11f10943a66ff3` |

