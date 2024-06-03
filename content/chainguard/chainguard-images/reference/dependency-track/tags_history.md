---
title: "dependency-track Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the dependency-track Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-03 00:46:08
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/dependency-track/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/dependency-track/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/dependency-track/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/dependency-track/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | June 2nd     | `sha256:111746d6efba6d19e626693dfe5d594a73e68871be4ccff2f28a55d47e179253` |
|  `latest-dev` | June 2nd     | `sha256:0bcc0e06efe7200177b55a4a10602fe35914be0fa68ebce9e291aac5a2df2921` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `4-dev` `4.11-dev` `4.11.2-dev` `latest-dev` | June 1st     | `sha256:29907590c22c4eaf0e02d3ae4052583994a594765ee2174ac0ed8b4245f00dc3` |
|  `4` `4.11.2` `4.11` `latest`                 | June 1st     | `sha256:af506b41fd5c7a9dcdd345c9e20917915c8519f1e4df8cf5a6db7557d6f041ce` |
|  `4.11.1-dev`                                 | June 1st     | `sha256:1200497c39766a60880f52112ed4df6ca0ff7da07506e4cd18bd8892f5549c09` |
|  `4.11.1`                                     | May 30th     | `sha256:bae7712ee3ae0a86b801980a2bdf7c1562686f57e8bd4f114d88b95d3804c318` |
|  `4.11.0`                                     | May 17th     | `sha256:006f45332a04ecd3c06f0eb9154c83efcb2d1d52f8a234598131d18e52385659` |
|  `4.11.0-dev`                                 | May 17th     | `sha256:1898d230cb795e6c56906d31b870992fd25ce537fdcb432eb53331a9f49ff23e` |

