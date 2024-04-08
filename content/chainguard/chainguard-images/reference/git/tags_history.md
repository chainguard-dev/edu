---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-08 00:38:35
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/git/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/git/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/git/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/git/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                  | Last Changed | Digest                                                                    |
|--------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-root-dev`       | April 7th    | `sha256:d27e64ee18174f6b9bc774caa007d07a864035863d03250dee957d0330da1a7e` |
|  `latest-dev`            | April 7th    | `sha256:de97721674d6b1cce2794664981204531a011c9f24af079f6b5874d1a266fc9c` |
|  `latest`                | April 7th    | `sha256:1b0095b607c13391ea987bbcdac81745a363090cb3660bf7768de4582cfe29de` |
|  `latest-root`           | April 7th    | `sha256:55187f00c320f8b9fa44dcfe51c5543844f2beee0bbd52cb5eab4fbeae847cb9` |
|  `latest-glibc-root-dev` | April 5th    | `sha256:7a55122277ac7e08e5e33005c8d9eddcb86015b64a088321480ed78c8b7b57dc` |
|  `latest-glibc-root`     | April 5th    | `sha256:58ebf82c6fc6d5a7772615733674eb6266ad1d8dc53083ad5e89656e70e970ad` |
|  `latest-glibc`          | April 5th    | `sha256:a6c0c9d3c9a21fb123288fcf3ab90aef51404a06a7e1b0d39e5b00e669f8ccee` |
|  `latest-glibc-dev`      | April 5th    | `sha256:876ad774d2735cf8469c0074d94925b2a2841c96ff12c835f0663488c54a7533` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                   | Last Changed | Digest                                                                    |
|-------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `glibc-root-2` `glibc-root-2.44` `glibc-root-2.44.0` `latest-glibc-root`                 | April 5th    | `sha256:c31b4bb7d0f1704722e5ac71a5ae729340834643d0786d4eacdf4625a379dc3e` |
|  `glibc-2.44-dev` `latest-glibc-dev` `glibc-2-dev` `glibc-2.44.0-dev`                     | April 5th    | `sha256:59d9f89ef0b01bf8a9ebeed5e99039233979713b22f9ee354742380401c39c6e` |
|  `glibc-2.44` `glibc-2` `latest-glibc` `glibc-2.44.0`                                     | April 5th    | `sha256:464e464f3fe972a7c413745890124b5a6d89328f29015b46b631d930b8e864a2` |
|  `glibc-root-2.44-dev` `glibc-root-2-dev` `glibc-root-2.44.0-dev` `latest-glibc-root-dev` | April 5th    | `sha256:32bb2c8f93d53c6c77e120ab7b444310308e71a0ef951478f8ab8f3dce952d37` |

