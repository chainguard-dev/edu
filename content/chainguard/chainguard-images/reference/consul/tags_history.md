---
title: "consul Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the consul Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/consul/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/consul/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/consul/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/consul/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 3rd     | `sha256:063b9a70561b2e0bb1b65a446e2aa82c4d008d5fe17a44f49b8b4d4b599f9d64` |
|  `latest`     | July 3rd     | `sha256:ac558b7e0b8382da95830a4c25962a39caea27a431bec48aad414ab137799776` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.15-dev` `1.15.11-dev`                     | July 3rd     | `sha256:62a6d03f21f5b7f739b3b3f365dadd8d8ef2108a7a6f18088eb09e8f1c5379ba` |
|  `1.16.7-dev` `1.16-dev`                      | July 3rd     | `sha256:70f60600df57944cc83ab59c53cc70a462ab90cf702dc89a824335266a0c3e34` |
|  `1.17-dev` `1.17.4-dev` `1-dev` `latest-dev` | July 3rd     | `sha256:f077cd653b525424e2698edf59e6216e350b8be4f29627648d5146cec9281ee1` |
|  `latest` `1.17.4` `1` `1.17`                 | July 3rd     | `sha256:74474c46b307f7d2feca4c89a9e92e4fa562e584734081023407f8d3959cd3c7` |
|  `1.15` `1.15.11`                             | July 3rd     | `sha256:056388e8d1046aa85581a09433f55786feeaa11413cade66e2c2ecf164770a62` |
|  `1.16.7` `1.16`                              | July 3rd     | `sha256:afbbfc46ba0970038a8e66648f9b485b9e13ea516125488cd9ad32b87810e3f1` |

