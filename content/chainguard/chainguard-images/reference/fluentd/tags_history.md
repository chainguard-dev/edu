---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-24 00:45:45
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
|  `latest-dev`        | May 23rd     | `sha256:e4613899ffd122f558e9335c0989a1d5406b9d481aaa84644573653e24c9e752` |
|  `latest-splunk-dev` | May 23rd     | `sha256:c34640f12dfe1fe4c1cd9a6ca294abf6520fc2f0b067f1a3c8642fcf1eee6a91` |
|  `latest-splunk`     | May 23rd     | `sha256:0c2fa628e276ae5839a712b46c9a53dc34ebcd592ef6c62198b50d93c07c29a4` |
|  `latest`            | May 23rd     | `sha256:4d491071d7f99abe37cb1bdc3abcfab9b12339be0a19b316b3132bb100d6d513` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16.5-r1-splunk-dev` `1-splunk-dev` `1.16-splunk-dev` `1.16.5-splunk-dev` | May 23rd     | `sha256:32868d07b226f6e49f06f4eb3f1406868b14a6968aa70e1ff86543d2a49f188f` |
|  `1` `1.16` `1.16.5` `latest`                                                | May 23rd     | `sha256:cf00a81265bf1081541e1ea7184993391ee8a34e27f0a0a4c4a50a4aeff6ca8c` |
|  `1.16.5-splunk` `1-splunk` `1.16-splunk` `1.16.5-r1-splunk`                 | May 23rd     | `sha256:5f684b00fec9c5c72e2df9c06e321297c86aec5c6c3f990b9539f07c47171402` |
|  `latest-dev` `1-dev` `1.16-dev` `1.16.5-dev`                                | May 23rd     | `sha256:65d165cf3d9ded24141b1964521b2b90d3fb3d333db3f82c020deef650d16ba6` |
|  `1.16.5-r0-splunk`                                                          | May 23rd     | `sha256:741677b3870ced9463d436491c9168ba3861acc2f66fb6e4d469418bde6e670a` |
|  `1.16.5-r0-splunk-dev`                                                      | May 23rd     | `sha256:124507aed6595fc380269d13f107009ad72fe0fc20ad31dad9b531a7da1f157f` |

