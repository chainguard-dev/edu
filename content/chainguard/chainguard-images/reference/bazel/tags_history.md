---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-08 00:34:55
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
|  `latest-dev` | July 5th     | `sha256:1aa97020493608c6c517ed57dbfd13bd3fdf3cfe7399b3185ae5c4a5890fabb0` |
|  `latest`     | July 5th     | `sha256:ad7f8c5a724a3732dbebffc15b7bc35c7691b5ceba0ff11ea4a95566fb43011b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `7` `7.2.1` `7.2` `latest`                 | July 6th     | `sha256:c0927e8dba65adf4a1f9a68928c20363b2d47dce41b69a3cac134b0bf8ab3f79` |
|  `5` `5.4` `5.4.1`                          | July 6th     | `sha256:30fed39e74088d4d7bd9e5bdacb190c51adb0b942da194c2ac761dc429f0678a` |
|  `6.5-dev` `6-dev` `6.5.0-dev`              | July 6th     | `sha256:b9f4ccd9580f9f601ffa7f2c8483cf22c36427423f73200bfb812d1b1677cb3c` |
|  `6.5` `6.5.0` `6`                          | July 6th     | `sha256:a13c79075adfb0f14aca5b99ef554ac79552dd6888a703a08193cf869bff752d` |
|  `latest-dev` `7.2-dev` `7-dev` `7.2.1-dev` | July 6th     | `sha256:8c314ec2727c0bbdd471bb6f12ad68da0cd279a261f959bb7e0860ae16d8ffe3` |
|  `5-dev` `5.4.1-dev` `5.4-dev`              | July 6th     | `sha256:8e174ab1ef8ccd2b462f5f98686fbb191501e265946561a07132aee1ddd16b71` |

