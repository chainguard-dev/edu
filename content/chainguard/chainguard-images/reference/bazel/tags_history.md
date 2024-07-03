---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-03 00:33:11
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/bazel/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/bazel/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/bazel/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/bazel/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | July 1st     | `sha256:032cba9fa97ebae6ebc9db69912a47354f5ea77ebc6ea4701a5e7cf90012e9d1` |
|  `latest-dev` | July 1st     | `sha256:a026e63502dbe1dc55be2842c16a26fc349ee400d3a49421b1fdab8910796a00` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `6.5` `6.5.0` `6`                          | July 2nd     | `sha256:8a3ee777bfcc2d8f900149d840bed3d7260748b7058165be7b7a9079bbfb15c0` |
|  `6.5.0-dev` `6.5-dev` `6-dev`              | July 2nd     | `sha256:c1d84ae90dae3e05a27bdf80a998cd7e122fc46a6d39163ea873dceb555c64e8` |
|  `5.4.1` `5` `5.4`                          | July 2nd     | `sha256:5de459a8947b9991f6bc36c80babdb8d54454569f007893d4117fa9d3bfb79cd` |
|  `7.2-dev` `7.2.1-dev` `7-dev` `latest-dev` | July 2nd     | `sha256:26dc3064a3a8a2d37dbe9efb87e2cf00413a3e7aaf970dfaf5b768751e4ff24a` |
|  `5.4-dev` `5-dev` `5.4.1-dev`              | July 2nd     | `sha256:9410b4f9efc4b4eb2ac3b062a958ae27b7eb070c17facd909c0a746772e2dcf2` |
|  `7.2.1` `latest` `7.2` `7`                 | July 2nd     | `sha256:dc6c4d8beb0e794958cfaca1ac5b51172ddac1e53c6e5dfa7c205936a19d5fef` |

