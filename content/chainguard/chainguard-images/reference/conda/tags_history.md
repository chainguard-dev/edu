---
title: "conda Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the conda Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-10 00:43:45
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
|  `latest-dev` | May 8th      | `sha256:e3b42318ed3ff904bcdb852323bb6521300b64fa1adbbee9564630d2741c5d11` |
|  `latest`     | May 8th      | `sha256:9a091c2b10684fa1bb426b31ca7f6681ec8651190a724f9e9b58fbcc54f022f7` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `24.4.0-dev` `24.4-dev`                       | May 8th      | `sha256:db25b7d5ccc48668c852b24b06922024347fbd1b5fbd4a3c2dbc184f81d5cfa6` |
|  `24-dev` `24.1.2-dev` `latest-dev` `24.1-dev` | May 8th      | `sha256:ede84f8ea1bb606dc8520362bdaafb96482d33625cddc3a2245a481b9621dbe5` |
|  `24.1.2` `24.1` `latest` `24`                 | May 8th      | `sha256:d97af25b7a57343929f8b7c2e4ec6c8bee82b00cac9738a8bbb898fdc424d206` |
|  `24.4` `24.4.0`                               | May 8th      | `sha256:12455aac60e4625f73e166b429c3f526ba9e018cc75b7a6339bde4d7b3618fe4` |
|  `24.1.1-dev`                                  | May 8th      | `sha256:8ac891512e678530a4a9774f27f1d32a451b0bb99addf22b22fccabd6c69083d` |
|  `24.1.1`                                      | May 8th      | `sha256:fd8d530dc760180d531b81ade987a3ba49bb03a95f681e5edc2e9aae3f6f2d42` |
|  `24.3-dev` `24.3.0-dev`                       | April 25th   | `sha256:65e9045a3417077a206733bcec75043a1e93822c967c7b576f8a90cd5998c827` |
|  `24.3` `24.3.0`                               | April 25th   | `sha256:bd669722f6234d0662bb2bfb7860c15ec9fd729f1cbdc474765848a2e591ddfb` |

