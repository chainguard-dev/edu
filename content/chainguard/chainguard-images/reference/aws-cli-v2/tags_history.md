---
title: "aws-cli-v2 Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the aws-cli-v2 Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-07 00:46:50
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/aws-cli-v2/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/aws-cli-v2/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/aws-cli-v2/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/aws-cli-v2/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | June 6th     | `sha256:7fc12b9f2243ef636ba8f40040336a98dae5ec67c18f6135317fcae0ea5e8e45` |
|  `latest-dev` | June 6th     | `sha256:41e955b246db23f20a50815e1531a932c1922734c95c684dd312e07a9a789f57` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.16` `latest` `2` `2.16.2`                 | June 6th     | `sha256:1ec085e46420222df4d66afae324a0b631ab462686641c453f04ff76ea08e50a` |
|  `2.16-dev` `2-dev` `latest-dev` `2.16.2-dev` | June 6th     | `sha256:c245ed3cd0abcc94b8bad9e091d1d42c8bbdce0093c77f98836155ff64c89e93` |
|  `2.16.1-dev`                                 | June 5th     | `sha256:1a268b1892b111712ac50be821134284add9b009ab852e9586006a27a05a05eb` |
|  `2.16.1`                                     | June 5th     | `sha256:9087fe20f18444cc690949de440af054645dd69d73406786bdbecf66fc76412e` |
|  `2.16.0-dev`                                 | June 5th     | `sha256:9d182b67d7b6437865e2bd7befee9cbfad06cab962e18784250d6b13fed6b548` |
|  `2.16.0`                                     | June 4th     | `sha256:a8b620e18ef83e530ff8c7bfd4c733e2904f1034d42fc3e09b411e97ad04ba8d` |
|  `2.15-dev` `2.15.62-dev`                     | June 1st     | `sha256:44d3600bc22bad06e6d1adfc79e8f989e0c716f015ba6bac6f618c6190b2a48f` |
|  `2.15` `2.15.62`                             | June 1st     | `sha256:121a99b2e6a6a6ae4300090ed793eb5cfe9cd7ab38f6f1e15a2f62bec79a1b80` |
|  `2.15.61-dev`                                | May 31st     | `sha256:33d8840b1258ef127fd985c0d78e330328033927f1b8a3fc7ff7efba79675ecb` |
|  `2.15.61`                                    | May 31st     | `sha256:64dae9b16abf1903c3145176a723712d35717083847cdcf412cfc91b5f6e0ed6` |

