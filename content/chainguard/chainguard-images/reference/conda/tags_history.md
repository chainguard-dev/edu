---
title: "conda Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the conda Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-03 00:46:08
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/conda/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/conda/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/conda/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/conda/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 2nd     | `sha256:2b74f5deb7074a41d00ea50b63d08ee2c5a9805c616a72978a1e6bbcfa7a6ce2` |
|  `latest`     | June 2nd     | `sha256:a3f22f5b106b781e98c2ca07f617b2d990850dc6c930f086e2d0e6dd6b102856` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `24.1-dev` `24.1.2-dev` `24-dev` | June 2nd     | `sha256:c1610f566fc72601d08e947d1898dec5da9940ef6b06efaacb182fc78aa361ac` |
|  `24.5-dev` `24.5.0-dev`                       | June 2nd     | `sha256:bcf8ae4f5ae8390a5df843f78facc7ad187eb3b073185a7fb6bacbea4fa40ad4` |
|  `24.1` `24` `latest` `24.1.2`                 | June 2nd     | `sha256:f826e527f18a782b0ff9507c0b1e2cd5a0b292ac26b99dd921b880f24de1ca2a` |
|  `24.5` `24.5.0`                               | June 2nd     | `sha256:c4a8a9a452181a9549c5bb865d2cb6005e4f33d0c01cfbfe8028f7ca654fb2b2` |
|  `24.1.1-dev`                                  | June 2nd     | `sha256:fd43e16cd76a8ee561d9e86e9600d0c2ecf1f31daeb06dcd8ca8614f1ca90114` |
|  `24.1.1`                                      | June 2nd     | `sha256:bb1dd8aaf34061f0322a1e7b69b0277014de9b36d18349f6763c7ee1795c409d` |
|  `24.4.0-dev` `24.4-dev`                       | May 8th      | `sha256:db25b7d5ccc48668c852b24b06922024347fbd1b5fbd4a3c2dbc184f81d5cfa6` |
|  `24.4` `24.4.0`                               | May 8th      | `sha256:12455aac60e4625f73e166b429c3f526ba9e018cc75b7a6339bde4d7b3618fe4` |

