---
title: "cert-manager-cmctl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cert-manager-cmctl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-06 00:48:16
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cert-manager-cmctl/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cert-manager-cmctl/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cert-manager-cmctl/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cert-manager-cmctl/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 5th     | `sha256:c9ad5f6072f23b7327b32b5ecfd4762af84013bef170621f4b267e5282dc271b` |
|  `latest`     | June 5th     | `sha256:84f8fcd8a51836ee47e91dac0eb9483ed205fdeb1c16abf50fd1c7f3893bd1d5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.13-dev` `1.13.6-dev`                      | June 5th     | `sha256:a461841db5181bbb1de16fcb811806a3280c3138570ed0c04fe58dc7947be561` |
|  `1.12-dev` `1.12.10-dev`                     | June 5th     | `sha256:e51581edc336bf52163159cdf091f826f93ad9dd1beab2406e72436a8de3a458` |
|  `1.13` `1.13.6`                              | June 5th     | `sha256:052ca2fa5ba4bf56e7a61af286f82c5e0e1a543ee9965cf2f191c4cbfaf2fd2e` |
|  `1.12` `1.12.10`                             | June 5th     | `sha256:025d980346655202bbb8f9db216ba83299e00c506e4c3d8edd683aced7988a3f` |
|  `1.14-dev` `latest-dev` `1-dev` `1.14.5-dev` | June 5th     | `sha256:00b3ad6c1ac280b3ab6a627fd2614a6d13cca4c1e637755fefe2a4c03e6c6c70` |
|  `1` `1.14.5` `1.14` `latest`                 | June 5th     | `sha256:2768c85eef369b70d09f50914fe128a9146a290770346ff15ed663fd251c0800` |

