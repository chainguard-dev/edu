---
title: "rekor-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the rekor-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-07 00:51:54
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/rekor-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/rekor-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/rekor-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/rekor-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 1st     | `sha256:ed9a33878e70653470cef97e2899d7843591cc0146a25b91096f07a255394664` |
|  `latest`     | February 27th | `sha256:911e8548d882f4bdd468d91d1cc260437ffe88a9da5fce84fe1d8c3bef8f8f56` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `1` `1.3.5` `1.3`                 | March 6th    | `sha256:161a44f1feea7e6c394d54df7a41aa5d31e05600876d2a0f03c0f71aa393554b` |
|  `latest-dev` `1.3.5-dev` `1-dev` `1.3-dev` | March 6th    | `sha256:eeedf1590dac03f99d12bee36cdad505ccd5cc023f3f0075f402c2fff3e11e4b` |

