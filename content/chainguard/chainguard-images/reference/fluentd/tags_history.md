---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-15 03:08:24
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
|  `latest-dev`        | April 12th   | `sha256:076b4ecc9b6861c48e3c2a57a1abce1a2e033ff3f7b497e075b61a7135281c94` |
|  `latest`            | April 12th   | `sha256:6f6c5f9bcee08acd31b0fff0802282b8783dc012f99cd024f544f69401b1e066` |
|  `latest-splunk-dev` | April 12th   | `sha256:c7ab1dd436dd7a68cc679e8c0dc1e7da9420949bf3fc4ff51e0dc3386606cd25` |
|  `latest-splunk`     | April 12th   | `sha256:de6d0ce071208ea0e1ad88a2ad34543e8b37a9e0ac6bb56ea41cb207b76f63c8` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16.5-r0-splunk-dev` `1-splunk-dev` `1.16.5-splunk-dev` `1.16-splunk-dev` | April 12th   | `sha256:da7571ceb143d1f49771061fcef0cb80679d9197108c1c83cdf20e33fec1654f` |
|  `1-splunk` `1.16.5-r0-splunk` `1.16-splunk` `1.16.5-splunk`                 | April 12th   | `sha256:24188b9c48b3aecd4a1b7b50d104e07abca97ed974cfce24262f33be2dbb41ad` |
|  `1` `1.16` `1.16.5` `latest`                                                | April 12th   | `sha256:7ddece817f48a0762fd9dcf50a20f0288b898f7ab536a2a4d7119eb0b06907b5` |
|  `1.16.5-dev` `1-dev` `1.16-dev` `latest-dev`                                | April 12th   | `sha256:057c36b08eaee2534068b0f733bdb3a242a29bb4b9015d0f4829029850e32cb7` |
|  `1.16.4-splunk-dev` `1.16.4-r0-splunk-dev`                                  | March 27th   | `sha256:3b27787033b3648c3de96fcd0654098ce79a13f43b2ad6d7dc4f80f2d2db32ba` |
|  `1.16.4-dev`                                                                | March 27th   | `sha256:11600998fec349115f2dce10d0676de2604ee2cfe9e5d9af79d99dd0d19a1a1a` |
|  `1.16.4-splunk` `1.16.4-r0-splunk`                                          | March 22nd   | `sha256:c18d359ef44a76b99ed6695ce4b231bc621b56f19d8659c49ae9f46218fb18ad` |
|  `1.16.4`                                                                    | March 22nd   | `sha256:1eb2f9c7c9b9a0fc95f8e2eb516614490790b30dbb8c1b5fc78699386cb7851a` |

