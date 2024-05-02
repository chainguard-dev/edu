---
title: "zot Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the zot Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/zot/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/zot/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/zot/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/zot/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 1st      | `sha256:7aa085b53023f1f935acdb4ac2f16cb0c45cbfdd035ba18fce1c807215db963a` |
|  `latest-dev` | May 1st      | `sha256:16fe3e8f9be1868e494051cdb37fcb2f7c54a2bf28f3a1c7d4e034305c47a4c7` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2` `latest` `2.0.4` `2.0`                 | May 1st      | `sha256:11e70c0d9826e71dcb83aa943f05ffe1351fcb7e0b5b60c03dbed35c56dc42c1` |
|  `2.0.4-dev` `latest-dev` `2.0-dev` `2-dev` | May 1st      | `sha256:4b7f3e6192850a40280065e24f7f21b6f6dd575e8ea8d86d8a6c695de176997e` |
|  `2.0.3-dev`                                | April 23rd   | `sha256:a30bea8e9b9ff689b0eb8ce6d02fcce68e82ab59155ee677f5e7e1df34aa1dbe` |
|  `2.0.3`                                    | April 23rd   | `sha256:f3d38b482240c62289f74454aab9ae806c4528fec1eb20785d5d26b04de2b709` |

