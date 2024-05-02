---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/bazel/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/bazel/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/bazel/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/bazel/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 1st      | `sha256:0da02aa68b2f7b88e19f38fd60f74ed9ce42f3b50a5b5909a66d90c47771e9f1` |
|  `latest`     | May 1st      | `sha256:3d8fe4aae984c4f40878e1e68dfa21a7b0059e9f624c0361bd364c5aa029e5f5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `6-dev` `6.5-dev` `6.5.0-dev`              | May 1st      | `sha256:ec84bc4754db2561dba69859b20f1fcf38719d0a65e7960d039ed9f4cc1c8c67` |
|  `7.1` `7.1.1` `7` `latest`                 | May 1st      | `sha256:a2d6075fed60617be5e509e1f97ef18ce4a1519c557d63058b2afc1f20b4dbc5` |
|  `5.4-dev` `5.4.1-dev` `5-dev`              | May 1st      | `sha256:7ee92dbfb3938810eaadf247423075a5883f4043f6cb088a4788b3115dce9b75` |
|  `7.1.1-dev` `latest-dev` `7-dev` `7.1-dev` | May 1st      | `sha256:6d4ce09fa97129870caa2f4554c6d86eff8c89f2193ec202c4866e446fca5084` |
|  `5` `5.4` `5.4.1`                          | May 1st      | `sha256:33989126f52189cbc7936516de108036f7b25469e6e670cb7c4bc767e15ff9bc` |
|  `6.5.0` `6.5` `6`                          | May 1st      | `sha256:4e6500fec3e25059a6b528d824fd6d5b876659a14224d72efc09cf3f20e25c5d` |
|  `6.1.1`                                    | April 28th   | `sha256:e779a5ec7dfce8190755a7c683f3f8fed331ac6909ec52270d35362fba8df214` |

