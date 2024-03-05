---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-05 17:06:05
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/fluentd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/fluentd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/fluentd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/fluentd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)              | Last Changed  | Digest                                                                    |
|----------------------|---------------|---------------------------------------------------------------------------|
|  `latest-splunk-dev` | March 1st     | `sha256:8c04a0af71503729bf51fac1c312fd9fed7fab06074ca5a162b382996c9b84af` |
|  `latest-dev`        | March 1st     | `sha256:74bce95322dfad1b9902ab513c3065ca05151c2debde10376eda1a26ff8080a9` |
|  `latest`            | February 27th | `sha256:f8455480ff0e41afdb695620582e2b2e659391e3cf5104e58da2dee2af2ae51a` |
|  `latest-splunk`     | February 27th | `sha256:badd764462955f2abc1d612d98b2b8b4b5bea9234bbb43d1b8337390806c8379` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed  | Digest                                                                    |
|------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `1.16.3-r1-splunk-dev` `1.16-splunk-dev` `1.16.3-splunk-dev` `1-splunk-dev` | March 2nd     | `sha256:ae10c937fb804e5114bcda2f2b4123de1413a9806e6eb6999b47171ee696b59e` |
|  `1-dev` `1.16.3-dev` `1.16-dev` `latest-dev`                                | March 2nd     | `sha256:8106f3447d6aa61a4403c89115180abf93b8578685ff74415679d3fc047325c4` |
|  `1.16` `1` `latest` `1.16.3`                                                | February 26th | `sha256:06d2fe152a6cac95ab7e5e08a534ff49bdbb410740c2a50e36122f3d9e8d943a` |
|  `1-splunk` `1.16.3-splunk` `1.16-splunk` `1.16.3-r1-splunk`                 | February 26th | `sha256:2e84cd54817cf27317ed6c167620ea2a3f87998111394ed8a5b1bb645e9a8d19` |
|  `latest-splunk-dev`                                                         | February 9th  | `sha256:b2d2725bb9fbd7541c09a3b94952eb73751a93c5d99377eebd46ae7dbaeb6853` |
|  `latest-splunk`                                                             | February 6th  | `sha256:5ee46ea7aeb4d9d4b4aedbd36d90b5d0ef15e94518f9e221a69e23d9c486a3e2` |

