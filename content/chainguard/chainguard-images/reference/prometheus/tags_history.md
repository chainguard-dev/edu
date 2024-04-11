---
title: "prometheus Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the prometheus Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-11 00:54:43
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/prometheus/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/prometheus/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/prometheus/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/prometheus/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 9th    | `sha256:b87c1b85a66079b143ac9718c86afd067fdc5355c7d75fbd7fc04223dbdf647e` |
|  `latest`     | April 4th    | `sha256:948d94be945a26e1a633b212e85158380fd2cead5449761d3e974e0560a4e842` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.51-dev` `latest-dev` `2-dev` `2.51.1-dev` | April 9th    | `sha256:2c727f6bbda85a0f56a696cb75a23fc6dd6caecfb7648ee0eb1b8c03fff971ef` |
|  `2.51` `2` `latest` `2.51.1`                 | April 3rd    | `sha256:fb4e4e90fa0c9fb812361eb8d9b4cce308b0ba8718b087ad7ad2fdc0b9db1cb3` |
|  `2.51.0-dev`                                 | March 28th   | `sha256:5307251a115475ae97e9de0d9eadc9db0d5d57a74f7dcd5e5128babaab1c3afb` |
|  `2.51.0`                                     | March 28th   | `sha256:35656141080195fb66243438845b8e03b3034901c81323bb59e13754e137d2f1` |
|  `2.50.1-dev` `2.50-dev`                      | March 18th   | `sha256:c4eae816f969baa1ba9752bf55e8357993d3ac3ddf0daa9349b423eb96c48a87` |
|  `2.50.1` `2.50`                              | March 18th   | `sha256:2429ff2c41627a0b47bc2e518b0f6efe26e3c94c286221e8e1b1e22e88ade7cc` |

