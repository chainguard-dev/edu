---
title: "gatekeeper Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gatekeeper Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
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
|  `latest`     | July 8th     | `sha256:428c2d6fd930044eb5a12e08c0521f398fb1c2acc0ef76f16ddf145aa38eb6a4` |
|  `latest-dev` | July 8th     | `sha256:35b6b56dfbd15fed0fa30d1c925b1f7e321dc8f84131b5ff0a3ab474029cdc0b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `3-dev` `3.16-dev` `3.16.3-dev` | July 8th     | `sha256:c78899c454e9e1ee616c8a4ddf51f942627e03df2c77ddd4dc1263d72c4aa5e3` |
|  `3.15` `3.15.1`                              | July 8th     | `sha256:32fbd6f2446b03e8710c4b9a7c32f902342177d0e610228ed9b6f0d6390e0e98` |
|  `3.16.3` `3` `latest` `3.16`                 | July 8th     | `sha256:eae8871b1672efccdf39f933144da0b7fca0bac688f23616f6415e1181fc00cc` |
|  `3.15-dev` `3.15.1-dev`                      | July 8th     | `sha256:9eaf96ea2f91dad9d56f1c3a103b279962674efe413ba8cce4a6cc3855572147` |

