---
title: "velero Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the velero Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-10 00:43:45
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/velero/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/velero/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/velero/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/velero/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 8th      | `sha256:7e3a2513174e3c701850c6f7746e2ff991bd87fcea4404897c9cc492310bbc43` |
|  `latest-dev` | May 8th      | `sha256:0648d1cbe45ea51bf39b27db524caede7fb2f3174200bb76f4934261a472a861` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.13.2-dev` `1.13-dev` `1-dev` `latest-dev` | May 8th      | `sha256:b8ce6863d328e6c32e2e5152fc25c87bd821719945da2639e46ae348299316d4` |
|  `1` `latest` `1.13.2` `1.13`                 | May 8th      | `sha256:ec3569ae96d27b9dc53163d747012d4314adbc3f61ff38881e4399e83132b114` |
|  `1.13.1`                                     | April 11th   | `sha256:ecaaa35afc398d0d51919ddc02d92a4468412db2167d45ff303b0a3192d01650` |
|  `1.13.1-dev`                                 | April 11th   | `sha256:3915071decc82caab74ed7639ce8e07d7eea7b46d4464f8bdebd37583fe40dcb` |

