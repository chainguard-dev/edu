---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-23 00:42:59
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
|  `latest-dev`        | April 22nd   | `sha256:28b942a82b36fc542221159083bc0b654e857dd7d9e77310e7b34f50aaa78a1d` |
|  `latest`            | April 22nd   | `sha256:1a795dc815537091079e5b22052929dd8ed7070c213c23b9678b6fdc40cfdbdb` |
|  `latest-splunk-dev` | April 22nd   | `sha256:9db3246be294eac71031d19859cd6114555cf1dc8b86780d8714a8d83de9328d` |
|  `latest-splunk`     | April 22nd   | `sha256:71379321f8e298805d430fe6b24402a9db7fd98650fcccfaa3928febe9e75c45` |


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

