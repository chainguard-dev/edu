---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-12 00:54:01
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
|  `latest-dev`        | April 11th   | `sha256:1f28dc0e12e05a70b3f5f5369b5014415e946410b5eb364ade71dd3538d27d07` |
|  `latest`            | April 11th   | `sha256:4ba30d215a62a89b22cdccdc6039e13c7a2481c9d89327e44d851cd01673191d` |
|  `latest-splunk`     | April 11th   | `sha256:96c401edb4cc907cae184c5fcaf6c545af1483995025aae065576e5abebae3e9` |
|  `latest-splunk-dev` | April 11th   | `sha256:d0c0e813886453429eae93938692a1917344995b596b6aedd6cb794e4cdfb337` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16.5-splunk` `1.16.5-r0-splunk` `1-splunk` `1.16-splunk`                 | April 11th   | `sha256:65e559297782136832c9326c5b321fb8ff502b6e2925b3c9df1840eb76c28da6` |
|  `latest` `1.16.5` `1` `1.16`                                                | April 11th   | `sha256:7bd114905d9c61f34632ffd26f2cfd19aaacd74d10a1b5c64ce2d833708d40ec` |
|  `1-dev` `1.16-dev` `1.16.5-dev` `latest-dev`                                | April 11th   | `sha256:2cc3d4830a7413a29d915a19b7910be9c73953b291016a1b74353f7453c814d1` |
|  `1.16.5-splunk-dev` `1.16-splunk-dev` `1.16.5-r0-splunk-dev` `1-splunk-dev` | April 11th   | `sha256:4cbcc95478cd1aa798807d2b870fa2d0e1df304b332799ca638f3db618464e37` |
|  `1.16.4-splunk-dev` `1.16.4-r0-splunk-dev`                                  | March 27th   | `sha256:3b27787033b3648c3de96fcd0654098ce79a13f43b2ad6d7dc4f80f2d2db32ba` |
|  `1.16.4-dev`                                                                | March 27th   | `sha256:11600998fec349115f2dce10d0676de2604ee2cfe9e5d9af79d99dd0d19a1a1a` |
|  `1.16.4-splunk` `1.16.4-r0-splunk`                                          | March 22nd   | `sha256:c18d359ef44a76b99ed6695ce4b231bc621b56f19d8659c49ae9f46218fb18ad` |
|  `1.16.4`                                                                    | March 22nd   | `sha256:1eb2f9c7c9b9a0fc95f8e2eb516614490790b30dbb8c1b5fc78699386cb7851a` |
|  `1.16.3-r1-splunk-dev` `1.16.3-splunk-dev`                                  | March 14th   | `sha256:0fef6f7c2cd7b2050db62430cfcbda1321040a445611bd45912694c722feb2ba` |
|  `1.16.3-r1-splunk` `1.16.3-splunk`                                          | March 14th   | `sha256:7c8e444a1bd10fe1b2ff2420375ac5a307d06b9063555dc20522cc6725758e6c` |
|  `1.16.3`                                                                    | March 14th   | `sha256:a73b93df29394adca0c321d669efec4d21b1d50ab3e4f19728196a8023b66e2b` |
|  `1.16.3-dev`                                                                | March 14th   | `sha256:12cb8789fef98f45bd4be9de57f7e2974dd2109ae39dbbfe0fe00c7a2a8d447a` |

