---
title: "node-lts Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node-lts Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-31 00:48:45
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/node-lts/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/node-lts/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/node-lts/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/node-lts/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                  | Last Changed | Digest                                                                    |
|--------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `next-dev` | May 23rd     | `sha256:49163a9f8b52f3ad9e842a16ccf0d7fa673571a272762f6483e38b90ba83985f` |
|  `latest`                | May 23rd     | `sha256:64578d895b168f20737413ac56a14cefd63663691611f8af5020e8bc8de53f82` |
|  `next`                  | May 23rd     | `sha256:5ac985f05bec5f0249309347e4b61a44f306ddef2682342f14fbdfafb9a3fed3` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                     | Last Changed | Digest                                                                    |
|-------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `next`                                                     | May 30th     | `sha256:3db662491a4eaf16aa6ad123dd697ad69d30c13f7c863025cb2160dcc8221a4f` |
|  `20-dev` `next-dev` `latest-dev` `20.14-dev` `20.14.0-dev` | May 30th     | `sha256:6af873938e8171589d8e1c0009311ab12789bb8ac32bb6e54c1aef3fc1644835` |
|  `20.14` `latest` `20.14.0` `20`                            | May 30th     | `sha256:25366d35072bf38af0107587b4a9d1d1e684bfb6b3b44719f29d2d12eb9d7bd1` |
|  `20.13-dev` `20.13.1-dev`                                  | May 28th     | `sha256:e8d44ddf859b463a39a89dc23310120f3b676f790a02395e6d029daa10adc5b8` |
|  `20.13.1` `20.13`                                          | May 24th     | `sha256:cdcb55f5afb9fd31acaa01e957aa6eff12aa9fdca6aaff0cd5fd748611c56cc0` |
|  `20.13.0-dev`                                              | May 8th      | `sha256:2360a32e40e19b859f6d47a78ff722b6e3533260547e961a24aae47ad2603aa1` |
|  `20.13.0`                                                  | May 7th      | `sha256:9e605246896ec5e57b3ca2c840df46d2736a52d8093823a237437374d1c1c788` |
|  `20.12-dev` `20.12.2-dev`                                  | May 2nd      | `sha256:e8836f7cb1c3a413655996eb25cda5e87fe8950b6af44ff77a39f0ca39b32bd0` |
|  `20.12` `20.12.2`                                          | May 2nd      | `sha256:a55a71363129778395bcc88cc8c2fe6a0f26affb1d7ee94862bef5c6e1f1c873` |

