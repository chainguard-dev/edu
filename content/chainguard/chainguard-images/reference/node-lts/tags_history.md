---
title: "node-lts Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node-lts Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
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

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | April 11th   | `sha256:a70ad222f56e1f77050dd5da29fa0293e640f52fb8bf210a026fab16f4464218` |
|  `latest-dev` | April 11th   | `sha256:1faae84720ce765e6c83f421bbe2f7e8664fffb1ab7d592d91dcac8ee68ec498` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                          | Last Changed | Digest                                                                    |
|--------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `20.12.2` `20` `20.12` `latest`                 | April 11th   | `sha256:d9e6e09a1c893d0e5b9ad03577f1156eaa30e8a50a419f059f3522d3a221abd6` |
|  `20-dev` `latest-dev` `20.12.2-dev` `20.12-dev` | April 11th   | `sha256:99bdd1e476a6f6e4163d455e6b14fe88bc8e662419aba97d37ffb05209d0776c` |
|  `20.12.1-dev`                                   | April 9th    | `sha256:d289a7c7a304ddbed4b56ad9d455d5927e43fdb587c451e75bd652ee876feed2` |
|  `20.12.1`                                       | April 9th    | `sha256:7d95ea2daa4623b270d640e2a7e9f7aeb353993313b277bd44f29a67bce1655f` |
|  `20.12.0-dev`                                   | April 3rd    | `sha256:83afbbb59e0c66fe10e503df0da53673df4724b013dcf10bdc996d6898a8608c` |
|  `20.12.0`                                       | April 3rd    | `sha256:0f9217ed827198cbb8c09503e28fb93acbe24a2f1af31c45e5cdcb31fe0f5347` |
|  `20.11` `20.11.1`                               | March 18th   | `sha256:c972cb33201cd945b4372c2369152967ee1f7493c906f098f8dd0112c481d1dd` |
|  `20.11-dev` `20.11.1-dev`                       | March 18th   | `sha256:9042c740b80df22bf549889ec2abe12170f3e4b836ecb2498ca67191d9e09be8` |

