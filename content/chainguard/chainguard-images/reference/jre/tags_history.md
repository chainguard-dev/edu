---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-05 17:06:05
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jre/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jre/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jre/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jre/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 1st    | `sha256:39aa73192e19bd0401636036d730ce733152e4c054bec2e8aed1c54cd06a35ec` |
|  `latest`     | March 1st    | `sha256:9df1cccf21e9d227a04f5a80c5a55ed86863adae807214a8f400fa82d3074365` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-8.392.08` `openjdk-8` `openjdk-8.392`                                    | March 3rd    | `sha256:6bc3681f2b3b2ffc906b92aeaa44920c891db56df94396e4bff8749a6148cfdb` |
|  `openjdk-8-dev` `openjdk-8.392-dev` `openjdk-8.392.08-dev`                        | March 3rd    | `sha256:c6c7487f187c13f6908c45aa57a02dcf6e753fa0e9d9f34e3c572684a2a5bf67` |
|  `openjdk-15-dev` `openjdk-15.0-dev` `openjdk-15.0.10-dev` `openjdk-15.0.10.5-dev` | March 2nd    | `sha256:9e1ab0f02fa90b11dd700675c7981191fc102cb15331d97a297ffa6d26967aea` |
|  `openjdk-16.0.2-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0-dev` `openjdk-16-dev`   | March 2nd    | `sha256:6b50e0804a46bc3cfa4f90f34ecf56b4dfaf17d8cebe7f44e5177f2439be081f` |
|  `openjdk-14-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0-dev` `openjdk-14.0.2-dev`  | March 2nd    | `sha256:6f8d5d6d2a05abf81ddc676d78ed7584fdd8f7a2b1cc4e941367488b91db72a9` |
|  `openjdk-17-dev` `openjdk-17.0.10-dev` `openjdk-17.0-dev`                         | March 2nd    | `sha256:dda2fe500d2021d26ebf7048fd35e667b149af40ce0335fb0f4ddf6be3a5edc0` |
|  `openjdk-11.0-dev` `openjdk-11.0.22-dev` `openjdk-11-dev`                         | March 2nd    | `sha256:19120e05171d9dffd380bf92dc0056708716155846561cec0d7808c2094e0330` |
|  `openjdk-21-dev` `latest-dev` `openjdk-21.0.2-dev` `openjdk-21.0-dev`             | March 2nd    | `sha256:3fbca1dc1251ff2fef92920cb70c4979cb7ea9122dc8225913c60ee5081163a0` |
|  `openjdk-11.0` `openjdk-11` `openjdk-11.0.22`                                     | March 1st    | `sha256:f722cf6f523d4ae2825d89fc7680cbd577d28cbddfb13eb6837a011e06eb1fd4` |
|  `openjdk-14.0.2` `openjdk-14` `openjdk-14.0` `openjdk-14.0.2.12`                  | March 1st    | `sha256:149d96e002fecec26ea967a4043abbdcf97b84a72a19b25e37a89ea23db22d9e` |
|  `openjdk-16` `openjdk-16.0` `openjdk-16.0.2` `openjdk-16.0.2.7`                   | March 1st    | `sha256:5bd215db8aee9c1eec4761f36c58121c7ad35be7f54e8bc4f55f55a0349fa523` |
|  `openjdk-15` `openjdk-15.0` `openjdk-15.0.10.5` `openjdk-15.0.10`                 | March 1st    | `sha256:a8658f5a932741d62de0416acdd8c042b5a044fe7bbcdaeba8c2a8314457008a` |
|  `openjdk-21` `latest` `openjdk-21.0.2` `openjdk-21.0`                             | March 1st    | `sha256:9f0b6ad9cda23e8352421b1e3f322091648a69d231f0c1bca0b3f46c87057bea` |
|  `openjdk-17.0.10` `openjdk-17` `openjdk-17.0`                                     | March 1st    | `sha256:4b0683a490fa71cf39b9285e7e0ba73fd1e0b407fbf9354791d34a58a098bdb4` |

