---
title: "harbor-core Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the harbor-core Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-25 00:42:19
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/harbor-core/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/harbor-core/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/harbor-core/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/harbor-core/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 24th    | `sha256:5f00f95d7f9579d6cad67a79f4a42185a680440d09f6050e457eb2c92dbfc47d` |
|  `latest`     | June 19th    | `sha256:98a98fcabd21160669438ed76e3071c1e598bc03afb6e399b47abc04a801cf54` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.10.2-dev` `2.10-dev`                      | June 24th    | `sha256:ff2eb81169736d094c3d105f67c38d3bf9da5646f38d826b7633c1dafe54e696` |
|  `2.11.0-dev` `2-dev` `latest-dev` `2.11-dev` | June 24th    | `sha256:bb1797aeee6089869bfd1e4319f9fe7edc4e6a3e3873c3621c9d73a5f4c075ee` |
|  `2.9.4-dev` `2.9-dev`                        | June 24th    | `sha256:cc228a796b1aa43179e131e88ff4acd583707912913120db626b2f2760b075e8` |
|  `2.8-dev` `2.8.6-dev`                        | June 24th    | `sha256:c82e562aa698d99ea7ec8a959548c4f73897ec086cdd0cb1401b1fdf9646e6fe` |
|  `2.9.4` `2.9`                                | June 20th    | `sha256:b509d11af6bf91ed957e3c38e7e5a8574341edc280b005e248d7076b0668761f` |
|  `2.10.2` `2.10`                              | June 20th    | `sha256:c03adb8dd3ff0047e87439dccc32c82e82e9a66d228a14c3737825cf63164f93` |
|  `2.8.6` `2.8`                                | June 20th    | `sha256:9f98d04966ae5c115c1068ae1ce150204b726dd0cc16d115a7004a79aec73c3a` |
|  `2.11.0` `2` `2.11` `latest`                 | June 20th    | `sha256:bfba4a62803072eb93f55434534e6fedf5c0ff779452dfd51faaeb8a5d8fed96` |

