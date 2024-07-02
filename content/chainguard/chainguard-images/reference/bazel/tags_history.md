---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-02 00:32:13
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
|  `5.4` `5` `5.4.1`                          | July 1st     | `sha256:3d1dfc24861ba8805014e5aba75964bccb3ac767d51e3f72d4443c77a57aaa42` |
|  `6.5` `6.5.0` `6`                          | July 1st     | `sha256:78ce6bb8126a71ebb3373e60759425be092ac62fae5e921c655e18e40659edaf` |
|  `6.5.0-dev` `6-dev` `6.5-dev`              | July 1st     | `sha256:e11401422aa4d8f0540f321ac3612407ca31d30a043eec072a3d3da8ae7ed0eb` |
|  `7.2.1` `latest` `7.2` `7`                 | July 1st     | `sha256:9289b69c4379eca4bac361936db8acc72f1f874e0040fb49f476f13f43be2981` |
|  `5-dev` `5.4.1-dev` `5.4-dev`              | July 1st     | `sha256:c5b4a37c9064449f5479a97f8c28016386e0e8c9ebbe66c4e694ee4bad4254f2` |
|  `7.2-dev` `latest-dev` `7-dev` `7.2.1-dev` | July 1st     | `sha256:139e70817cadbf06423a9264ddb52b9e3a6c3dcedffd4373efc7b77804c303c2` |

