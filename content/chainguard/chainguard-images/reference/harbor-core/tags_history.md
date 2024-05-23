---
title: "harbor-core Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the harbor-core Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-23 00:45:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/harbor-core/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/harbor-core/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/harbor-core/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/harbor-core/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 22nd     | `sha256:8e3fbe742315dbdcd050d9822d6f58dc4662470f22893c5030ffe48f3888656e` |
|  `latest`     | May 21st     | `sha256:3cf2bed0097bdd36aeaf31d5a80366c88002e788adc1c00b937016bea6e3953f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.8-dev` `2.8.6-dev`                        | May 22nd     | `sha256:ada851052aa8401ca140c680dc5ece7144053df21adb036a6066d47bd8129630` |
|  `2.9-dev` `2.9.4-dev`                        | May 22nd     | `sha256:8df56528ad0e4fb16d1e5225c447902229fb17a647428ad399c485d0fa706882` |
|  `2.10.2-dev` `2-dev` `2.10-dev` `latest-dev` | May 22nd     | `sha256:7cc80f777b231cdf5b0da12c5934bade3c296c5cbdc8fae055c7272faad639bf` |
|  `2` `2.10` `latest` `2.10.2`                 | May 21st     | `sha256:647bf60b938feba9a29798f475922e3fa16c3057e5d311b65675d32dda64d53b` |
|  `2.9` `2.9.4`                                | May 21st     | `sha256:4350a88e53a38f5f1eb28813a1383e163b9344db51ffbb111d2828e6a864f1a2` |
|  `2.8` `2.8.6`                                | May 21st     | `sha256:8cd2f8c3410d90d9f61449d4cb1aef3a2260c375a48dd16bd81fa253e35cce26` |

