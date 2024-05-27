---
title: "harbor-core Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the harbor-core Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-27 00:43:34
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
|  `latest`     | May 23rd     | `sha256:02d0fab25318eee6d5f992bfbf017a934209794361c87325527b2d234a3c8e68` |
|  `latest-dev` | May 23rd     | `sha256:453cc8e4458b65f216b501402048bffd5e30c955dd13ce0ea021b1755b2927d7` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `2.10.2-dev` `2-dev` `2.10-dev` | May 24th     | `sha256:f508d881e27340234690b70e31361b192b51d57b79e973581d49fdc46b7269fc` |
|  `2.9-dev` `2.9.4-dev`                        | May 24th     | `sha256:e406bf9d3af3afb8cb881ff954204b0f5caef3d85d75a9d717898cf90ea5e74f` |
|  `2.8.6-dev` `2.8-dev`                        | May 24th     | `sha256:3405f2e4a432d345bbc532c2b4a0dabf8d2e0b5dd9ebc55cca5e99b88fc0bdd4` |
|  `2.10` `2.10.2` `latest` `2`                 | May 23rd     | `sha256:fe8055df3918bb7d174365cda7fc679ca68dbc4a25a86079aceef3a19a92fbc1` |
|  `2.9` `2.9.4`                                | May 23rd     | `sha256:295f4cf25e0a6c7faebeac36e6409080297dca36a77ab6d9506ad595926c7970` |
|  `2.8` `2.8.6`                                | May 23rd     | `sha256:5a2fbdae0a023803593147f1820078e8f37aad469ebebc00f30f57e81a7536e8` |

