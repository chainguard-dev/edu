---
title: "aws-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the aws-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-22 00:45:38
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/aws-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/aws-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/aws-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/aws-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 21st   | `sha256:ac3aba78d29487bf0f57c6c969893abaaa59896c43fecf1c7b89b37a0387b752` |
|  `latest`     | April 21st   | `sha256:17cf4f4d7c54f98fe134e07e09333b4f8c73f647d44bef22adb5d03fe7baee00` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.32.71-dev` `1-dev` `latest-dev` `1.32-dev` | April 21st   | `sha256:2ff4d43b5301307ae2db07fa9abeedb3bc9af348d0291c71bc50615f0830125f` |
|  `1.32` `latest` `1.32.71` `1`                 | April 21st   | `sha256:23827c9454cd69db31218e8192609a8ce30e256b7c19b898804a3cab29b5a97c` |
|  `1.32.70`                                     | March 25th   | `sha256:6698fbd968e5d786f787afaa5ebb34feb88efa8297ea23a81342a988884b7c0f` |
|  `1.32.70-dev`                                 | March 25th   | `sha256:3bbbba05c5f5dadf3f55bb6f67bf775dd0be110cb2d33337215e5fd3ac798bda` |
|  `1.32.69-dev`                                 | March 22nd   | `sha256:ba8adb846a4c26230a3ec0514919d3c3265f05d028101fc30c72caa3e762787b` |
|  `1.32.69`                                     | March 22nd   | `sha256:a40d44c7006fa580ecd61250a1f733f9c1f23044c91f451357181de531f5e2d1` |

