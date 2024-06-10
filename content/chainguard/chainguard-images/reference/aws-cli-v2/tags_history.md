---
title: "aws-cli-v2 Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the aws-cli-v2 Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-10 00:50:47
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
|  `latest-dev` | June 9th     | `sha256:86b2ff2dc3261dca7c99764982f1c3e2fa6953ab104e1762c4ee29eaa6085961` |
|  `latest`     | June 6th     | `sha256:7fc12b9f2243ef636ba8f40040336a98dae5ec67c18f6135317fcae0ea5e8e45` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.16.2-dev` `2.16-dev` `2-dev` `latest-dev` | June 8th     | `sha256:dc7d193c782db861219320181f3972f35b113195e353f7aac12329498d66e397` |
|  `2.16` `latest` `2` `2.16.2`                 | June 6th     | `sha256:1ec085e46420222df4d66afae324a0b631ab462686641c453f04ff76ea08e50a` |
|  `2.16.1-dev`                                 | June 5th     | `sha256:1a268b1892b111712ac50be821134284add9b009ab852e9586006a27a05a05eb` |
|  `2.16.1`                                     | June 5th     | `sha256:9087fe20f18444cc690949de440af054645dd69d73406786bdbecf66fc76412e` |
|  `2.16.0-dev`                                 | June 5th     | `sha256:9d182b67d7b6437865e2bd7befee9cbfad06cab962e18784250d6b13fed6b548` |
|  `2.16.0`                                     | June 4th     | `sha256:a8b620e18ef83e530ff8c7bfd4c733e2904f1034d42fc3e09b411e97ad04ba8d` |

