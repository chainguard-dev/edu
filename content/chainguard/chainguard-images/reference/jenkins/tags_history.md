---
title: "jenkins Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jenkins Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-03 00:33:11
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jenkins/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jenkins/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jenkins/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jenkins/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 1st     | `sha256:94d679bf549773b7cc794cdc031f671feb15a46d713d3c8a71922028d55d31d9` |
|  `latest`     | July 1st     | `sha256:13442b7a2b8e32b4b77f4014512cda4d8fdafe77a9412464ad037fac3de19911` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `2-dev` `latest-dev` `2.464-dev` | July 2nd     | `sha256:8aea6434ad10fd45b2c11e08b797556473f48f9ca079448f7a6b07a36c53f4f3` |
|  `2` `latest` `2.464`             | July 2nd     | `sha256:16301e92a19428d9b12be0ff11822c4a6fcdd9cae7ee4e60fed0f99fcdda018b` |

