---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-02-29 16:25:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/maven/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/maven/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/maven/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/maven/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                        | Last Changed  | Digest                                                                    |
|--------------------------------|---------------|---------------------------------------------------------------------------|
|  `openjdk-17-dev` `latest-dev` | February 27th | `sha256:6275ac420c07599dc341253064c15198113ce6cb5cb494a3d83548649f7531ad` |
|  `latest` `openjdk-17`         | February 27th | `sha256:0fa50a3fe008d4eaad218d23d8cfa156228e28364b9c212b553e7514a99d6653` |
|  `openjdk-11`                  | February 27th | `sha256:288ce27ed7e18ad674181646be5e0458a81c805cc2ee6aebc73334879619a5b2` |
|  `openjdk-21-dev`              | February 27th | `sha256:a671cc0d846cca0ff2dfd219038242efb827b82562cec4529db4b7fa1f4e832f` |
|  `openjdk-21`                  | February 27th | `sha256:c94f10c521bc6a41515d88cd57186ca6e2e0a44f80c4f13dec62a4c592b2c196` |
|  `openjdk-11-dev`              | February 27th | `sha256:2f1ba2d67f6d68da7646af0fe6292de13c97723510012a672d0ff72c314974a2` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **[Production Images](https://www.chainguard.dev/chainguard-images)**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed  | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `openjdk-11-dev` `openjdk-11-3-dev` `openjdk-11-3.9-dev` `openjdk-11-3.9.6-dev`              | February 26th | `sha256:206235ad1afb64238f88107372608efbff020d9e49cd4a8a29212945f909bd82` |
|  `openjdk-17-dev` `openjdk-17-3-dev` `openjdk-17-3.9-dev` `openjdk-17-3.9.6-dev` `latest-dev` | February 26th | `sha256:c2f24623e209c25516c8c92aaf8eeffecd5b587a388c0788612ea74255a120f8` |
|  `openjdk-21-3-dev` `openjdk-21-3.9-dev` `openjdk-21-3.9.6-dev` `openjdk-21-dev`              | February 26th | `sha256:b6145be7aee79ae7adf2914dabe75097675c28e11adb6310f806a39d51f3fa31` |
|  `openjdk-21` `openjdk-21-3.9.6` `openjdk-21-3` `openjdk-21-3.9`                              | February 26th | `sha256:d48b12f0af806975f34f03e9d61413c0e14f4bd717106d8684c2b924b8844d09` |
|  `latest` `openjdk-17-3` `openjdk-17-3.9` `openjdk-17` `openjdk-17-3.9.6`                     | February 26th | `sha256:59dbea0fee052646c3dccaabbc3d46d8023c75c78f0f9cf56c25f454a7de4011` |
|  `openjdk-11-3.9.6` `openjdk-11-3.9` `openjdk-11` `openjdk-11-3`                              | February 26th | `sha256:5bbcfdedf0687eea91b7afd1fad1c9fe8d815f724a8f83610edc19f5563ae2e5` |

