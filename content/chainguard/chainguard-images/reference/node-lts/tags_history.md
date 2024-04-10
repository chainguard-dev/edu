---
title: "node-lts Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node-lts Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-10 00:53:55
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
|  `latest-dev` | April 9th    | `sha256:aa8a58f9fa839cc464f0b6457ae21659449bcd52dd27755baa948efb800c6a24` |
|  `latest`     | April 9th    | `sha256:8275f3ab0dc0af41913318920486f5169da661052da550277c9750615ae4407c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                          | Last Changed | Digest                                                                    |
|--------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `20` `20.12` `latest` `20.12.1`                 | April 9th    | `sha256:7d95ea2daa4623b270d640e2a7e9f7aeb353993313b277bd44f29a67bce1655f` |
|  `20.12.1-dev` `20-dev` `20.12-dev` `latest-dev` | April 9th    | `sha256:d289a7c7a304ddbed4b56ad9d455d5927e43fdb587c451e75bd652ee876feed2` |
|  `20.12.0-dev`                                   | April 3rd    | `sha256:83afbbb59e0c66fe10e503df0da53673df4724b013dcf10bdc996d6898a8608c` |
|  `20.12.0`                                       | April 3rd    | `sha256:0f9217ed827198cbb8c09503e28fb93acbe24a2f1af31c45e5cdcb31fe0f5347` |
|  `20.11` `20.11.1`                               | March 18th   | `sha256:c972cb33201cd945b4372c2369152967ee1f7493c906f098f8dd0112c481d1dd` |
|  `20.11-dev` `20.11.1-dev`                       | March 18th   | `sha256:9042c740b80df22bf549889ec2abe12170f3e4b836ecb2498ca67191d9e09be8` |

