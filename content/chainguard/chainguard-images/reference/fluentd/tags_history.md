---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-22 00:45:38
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/fluentd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/fluentd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/fluentd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/fluentd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)              | Last Changed | Digest                                                                    |
|----------------------|--------------|---------------------------------------------------------------------------|
|  `latest-splunk-dev` | April 21st   | `sha256:c59fa7ef41b01aafb68bcd7c0af067a1986ca70b85392bc1627e7ab86882ea33` |
|  `latest-dev`        | April 21st   | `sha256:7745643a77b269aa5b9bb70c2e09324d97463cf81348fe83054be977429fea71` |
|  `latest`            | April 12th   | `sha256:6f6c5f9bcee08acd31b0fff0802282b8783dc012f99cd024f544f69401b1e066` |
|  `latest-splunk`     | April 12th   | `sha256:de6d0ce071208ea0e1ad88a2ad34543e8b37a9e0ac6bb56ea41cb207b76f63c8` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `1.16.5-dev` `1.16-dev` `1-dev`                                | April 21st   | `sha256:5e645d12baa9aa7e86f10aa862ecd9f46bcf6663cd6e38f9664ff2473d9666c8` |
|  `1.16.5-r0-splunk` `1.16.5-splunk` `1.16-splunk` `1-splunk`                 | April 21st   | `sha256:663e31e023cecaf5a794404ef0fd46b53f59b4e55f77fe1704260de42506a540` |
|  `1.16.5` `1.16` `1` `latest`                                                | April 21st   | `sha256:0b0f0549bd8e19e9923388ffa2fd97bce35934f17adc03331e86434ecc36250b` |
|  `1-splunk-dev` `1.16-splunk-dev` `1.16.5-r0-splunk-dev` `1.16.5-splunk-dev` | April 21st   | `sha256:23d522ea0819d9acb80b9fbbfc756be4291010e98faccd7251f3e105e7be7177` |
|  `1.16.4-splunk-dev` `1.16.4-r0-splunk-dev`                                  | March 27th   | `sha256:3b27787033b3648c3de96fcd0654098ce79a13f43b2ad6d7dc4f80f2d2db32ba` |
|  `1.16.4-dev`                                                                | March 27th   | `sha256:11600998fec349115f2dce10d0676de2604ee2cfe9e5d9af79d99dd0d19a1a1a` |
|  `1.16.4-splunk` `1.16.4-r0-splunk`                                          | March 22nd   | `sha256:c18d359ef44a76b99ed6695ce4b231bc621b56f19d8659c49ae9f46218fb18ad` |
|  `1.16.4`                                                                    | March 22nd   | `sha256:1eb2f9c7c9b9a0fc95f8e2eb516614490790b30dbb8c1b5fc78699386cb7851a` |

