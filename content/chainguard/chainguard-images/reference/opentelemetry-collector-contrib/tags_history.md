---
title: "opentelemetry-collector-contrib Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the opentelemetry-collector-contrib Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-01 00:50:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 31st     | `sha256:68dc24d3cb48e604efd7bb62392cc3163c6be423f15fce7dec722cef4c32f378` |
|  `latest`     | May 23rd     | `sha256:5f8523c72819465f99682cdd60f97cff6b31e48acbb5a339abb096985a5f5d66` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                         | Last Changed | Digest                                                                    |
|-------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `latest-dev` `0.101.0-dev` `0.101-dev` | May 30th     | `sha256:1a8c3692d6b83bbbba960e32a3a0325bd89d2f31c9f3fa668e3867f01f3f2e07` |
|  `0.101.0` `latest` `0` `0.101`                 | May 23rd     | `sha256:ea9eef8c5d94546aaa6c30ecf8b41782e25523bf051759c28dcc3b3280ea42fe` |
|  `0.100.0` `0.100`                              | May 21st     | `sha256:ff8c8205aa8cb49a94a00b3df9e44be7356c5865e1af5f7223b1b5f837a49e42` |
|  `0.100.0-dev` `0.100-dev`                      | May 21st     | `sha256:f5d29c22595bb2bed5cba8db1a02f57c3ed6e40204892341720179ae7598a350` |
|  `0.99.0` `0.99`                                | May 2nd      | `sha256:c6d911ffdff3af608e7bdb40ea9d3be28c82c81ac3f8f80941fa1ab2bb483b0e` |
|  `0.99-dev` `0.99.0-dev`                        | May 2nd      | `sha256:e0ac90336053b4f26edbe93462e978fc65dec7cd59fad0d045d702001385a955` |

