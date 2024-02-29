---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-02-29 16:25:55
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
|  `latest`            | February 27th | `sha256:f8455480ff0e41afdb695620582e2b2e659391e3cf5104e58da2dee2af2ae51a` |
|  `latest-dev`        | February 27th | `sha256:e0192c496e77845268eaf9cd06075481f00b84a9cc3b7c90b285b86c086b8039` |
|  `latest-splunk-dev` | February 27th | `sha256:a0e5180341bbc6ac07e48186312076cf217b1e42dc256db5e1c7858944c8e529` |
|  `latest-splunk`     | February 27th | `sha256:badd764462955f2abc1d612d98b2b8b4b5bea9234bbb43d1b8337390806c8379` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **[Production Images](https://www.chainguard.dev/chainguard-images)**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed  | Digest                                                                    |
|------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `1.16` `1` `latest` `1.16.3`                                                | February 26th | `sha256:06d2fe152a6cac95ab7e5e08a534ff49bdbb410740c2a50e36122f3d9e8d943a` |
|  `1.16.3-r1-splunk-dev` `1.16-splunk-dev` `1-splunk-dev` `1.16.3-splunk-dev` | February 26th | `sha256:f5e52bb6b3129e35429390bd90d90c007b9efedee87a810d9606ff9eaeef9852` |
|  `1-splunk` `1.16.3-splunk` `1.16-splunk` `1.16.3-r1-splunk`                 | February 26th | `sha256:2e84cd54817cf27317ed6c167620ea2a3f87998111394ed8a5b1bb645e9a8d19` |
|  `latest-dev` `1.16-dev` `1.16.3-dev` `1-dev`                                | February 26th | `sha256:6d25ee1b169dbb401a2861d764b841f3db1294e03c0a9eda2ea2e2844281a29e` |
|  `latest-splunk-dev`                                                         | February 9th  | `sha256:b2d2725bb9fbd7541c09a3b94952eb73751a93c5d99377eebd46ae7dbaeb6853` |
|  `latest-splunk`                                                             | February 6th  | `sha256:5ee46ea7aeb4d9d4b4aedbd36d90b5d0ef15e94518f9e221a69e23d9c486a3e2` |

