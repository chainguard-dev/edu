---
title: "velero-plugin-for-csi Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the velero-plugin-for-csi Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-10 00:53:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/velero-plugin-for-csi/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/velero-plugin-for-csi/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/velero-plugin-for-csi/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/velero-plugin-for-csi/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 9th    | `sha256:eae1b75fdcfcfcd70103b13c9ac206ebc55705a418642f230ff058a4a9f94333` |
|  `latest`     | April 4th    | `sha256:2af1c578a5d4e5f78b291e1308c5f951e661d5c8f3327095b8ef30d25238573a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `latest-dev` `0.7.0-dev` `0.7-dev` | April 9th    | `sha256:2952ef93a7590da679ec3526071efe42aafd105c8a656d42102002fc14761d4b` |
|  `latest` `0.7.0` `0.7` `0`                 | April 4th    | `sha256:b3825a66ca0e19002acd5f1919a75dcd4cd22add212af6c3caf92c1341dcf124` |

