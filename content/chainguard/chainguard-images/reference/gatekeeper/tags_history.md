---
title: "gatekeeper Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gatekeeper Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-05 00:47:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gatekeeper/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gatekeeper/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/gatekeeper/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gatekeeper/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 4th    | `sha256:58bf24eb7d5b845bd60bd6242811fec36e7d0a37c837c2304ca2ed0742a0cafe` |
|  `latest`     | April 4th    | `sha256:51fccfc02c52eaaebd5d983ff53fa822777c715fe3874487bfa86222d29a8127` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.14.1-dev` `3-dev` `3.14-dev` `latest-dev` | April 4th    | `sha256:4278d949ea2b6ed249b7bb645a902640b2c48f2632864ac051db15d58fdbcf7b` |
|  `latest` `3.14` `3` `3.14.1`                 | April 4th    | `sha256:cf4f06161ae528be2620a6477d118bd11652caedb06a6851d7b721be693cc028` |
|  `3.13.4-dev` `3.13-dev`                      | April 4th    | `sha256:619d376b941a496cb340342252e1220f521e6b7730d185686e390ca610ca232e` |
|  `3.13.4` `3.13`                              | April 4th    | `sha256:e172ee396c6d9321b455d8664ff88c1d9ce7c017072e63e4758b2dad6f3bc04f` |
|  `3.12.0` `3.12`                              | April 4th    | `sha256:a948c59cccced4c98b267d3ca567805cdf2252728a40fe63440dfad43607868c` |
|  `3.12.0-dev` `3.12-dev`                      | April 4th    | `sha256:4a664625017b51b5ad4cd801a21dd5e314a7d2495cb7d38721d92c7eced0788f` |
|  `3.14.0-dev`                                 | March 12th   | `sha256:b4b3ef5c89c9f443b9f12a2199c3c4dffb1260770cb5c30f8d0f8dd33eca2eb1` |
|  `3.14.0`                                     | March 8th    | `sha256:60eb7d52e5c4c4d8c92191863c96dbd49b2da96da1b685bc3909cb518456e85c` |

