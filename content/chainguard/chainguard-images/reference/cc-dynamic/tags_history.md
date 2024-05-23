---
title: "cc-dynamic Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cc-dynamic Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-23 00:45:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cc-dynamic/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cc-dynamic/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cc-dynamic/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cc-dynamic/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 22nd     | `sha256:71b5c998075cc9dd617ea36eb0423e7042a88aee293fc986985e040203966202` |
|  `latest`     | May 21st     | `sha256:2eedccf87cc088ab95f6000c9eac7c75d7de26dd146cb01a175331293f25ec2b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `13-dev` `13.2.0-dev` `13.2-dev` `latest-dev` | May 22nd     | `sha256:91d082914172ad441dde4f0f10eaba9ebb0468bfd350379a987bf92e5c35dfa1` |
|  `latest` `13.2.0` `13.2` `13`                 | May 21st     | `sha256:ee823648431c3e83b39bd7b50599a333d26b2203e644c2366b9787e10b72c38e` |

