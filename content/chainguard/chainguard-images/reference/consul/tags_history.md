---
title: "consul Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the consul Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-23 00:45:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/consul/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/consul/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/consul/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/consul/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 22nd     | `sha256:6cef3c8d2752155d3a821dde3e5dfdfd5373652d81728d720049dfa926b33374` |
|  `latest`     | May 22nd     | `sha256:7020fa79ef4e2b4f97de00590a97c482fc4aed27f8e1b8fda3e2a39f5c114584` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16` `1.16.7`                              | May 22nd     | `sha256:09378a8e4b66bf3ac12f22a049d4149931a878125e4ee1b6e05c09ba1a148a4c` |
|  `1.15.11` `1.15`                             | May 22nd     | `sha256:f16df87c788f5b5da80682e04497210bf1be545d387845ecd1f9e69b3fed09b9` |
|  `latest` `1` `1.17.4` `1.17`                 | May 22nd     | `sha256:80038c83a00243dddfc9699fb866749ca94b94362a21d201eec02aa99b52a95c` |
|  `1.15.11-dev` `1.15-dev`                     | May 22nd     | `sha256:689b10928eeb88afcfd47f28ecc71a172d20a9ade356e9adb5d40f5625002de2` |
|  `1.16.7-dev` `1.16-dev`                      | May 22nd     | `sha256:91306d9c670e6c48d1254a9bb1abc748edce2e0b90b4e0753798a92c08eae89a` |
|  `latest-dev` `1-dev` `1.17-dev` `1.17.4-dev` | May 22nd     | `sha256:316d44a1440b96b99289dc59d6d96d183882a8fa6ed521dee51727d4d4fcbb5a` |

