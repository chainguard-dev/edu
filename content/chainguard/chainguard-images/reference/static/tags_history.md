---
title: "static Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the static Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-23 00:45:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/static/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/static/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/static/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/static/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)         | Last Changed | Digest                                                                    |
|-----------------|--------------|---------------------------------------------------------------------------|
|  `latest`       | May 22nd     | `sha256:288b818c1b3dd89776d176f07f5f671b118fe836c4d80ec2cc3299b596fe71b7` |
|  `latest-glibc` | May 21st     | `sha256:98158159f052dd78c2218c68d88d6a2f0371d8fe149fc88628c752bb49a2585c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                  | Last Changed | Digest                                                                    |
|--------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-glibc` `latest` | May 21st     | `sha256:cc0e32d9f09ba0902dd75cc050f41037c6abe6c1121a1c583f54d8ccd732d7a7` |

