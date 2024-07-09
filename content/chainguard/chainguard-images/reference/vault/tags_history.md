---
title: "vault Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vault Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/vault/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/vault/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/vault/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/vault/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 8th     | `sha256:f574896dadff2ad9b1d32a14c59bfac59cdd04eb0de27f50901d5f0985935761` |
|  `latest`     | July 8th     | `sha256:b44d9d48ed9c8d5881c542162c828c0ab38535941cc8a2da0e328cfaa960bd39` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1-dev` `1.17.1-dev` `latest-dev` `1.17-dev` | July 8th     | `sha256:5461827d72a0c0437d707e7d7d60bbb790248b532a922e91c5948ad490ebeff7` |
|  `1.16.3` `1.16`                              | July 8th     | `sha256:f05ed6bf0cfb5c8073c1d803b7d85b4b8dd50933e6fb3fa95564ab67f59a22f0` |
|  `1.16-dev` `1.16.3-dev`                      | July 8th     | `sha256:508b52a860b8d3b4bf742a968e22fabee02bfb2339be1c448faad4b7f1f7f614` |
|  `1.17` `latest` `1.17.1` `1`                 | July 8th     | `sha256:88b905f9be5ce18eef6abc1d24ffbc22253c613f76e14d5859eb471eb1a24c02` |
|  `1.15` `1.15.9`                              | July 8th     | `sha256:71408b9767b33279a0df89dd2de752918410235159e485215c1b56f6e7b102ba` |
|  `1.15.9-dev` `1.15-dev`                      | July 8th     | `sha256:b625285663d85b5413763dcf49829378841295f23f64a1da6ee6bc7894253368` |

