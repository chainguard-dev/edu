---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-11 00:42:18
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
|  `latest-root-dev`       | June 10th    | `sha256:9840516c98e12853309954a134d651f364437fc0aa61647e5b78555a8c600881` |
|  `latest`                | June 10th    | `sha256:6ecdfaf18b4fc0d6141e4551d5254d13cc249b5a6c6d08a9106e0b6e3a9dbab3` |
|  `latest-root`           | June 10th    | `sha256:8b9f9e868eb4e264d1b52c55ab980fb93509d01c33ea5e00d3fe8a325863a789` |
|  `latest-dev`            | June 10th    | `sha256:b9123ff9885f02fc39e75d1e5e6aaa0395ec9a8f6ba168bdc20178d916d9ee1d` |
|  `latest-glibc-root`     | June 9th     | `sha256:cfaf622086948ddc6d13f1bce8a0b685f0e8352bccaa8b23458c53d1647c3ba7` |
|  `latest-glibc`          | June 9th     | `sha256:f605d550a85bec71c6ba4ffe16da471cc26e0a5e854015da0de056b6f012d392` |
|  `latest-glibc-dev`      | June 9th     | `sha256:f357777c5e85b40d29c3f2af84f41e555b9cc4226e679bc6a045666949469135` |
|  `latest-glibc-root-dev` | June 9th     | `sha256:b9f7732a270369feeea1a401e077b6b7bb199030e7b483d3bbaa32cceca7171e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                                                                                    | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `glibc-root-2.45` `glibc-root-2` `root-2.45` `root-2` `latest-root` `root-2.45.2` `latest-glibc-root` `glibc-root-2.45.2`                                 | June 8th     | `sha256:e988f7dfdc204ed995c4f2755a961ced290c9c8486e160a92d5158f6c67ed314` |
|  `latest-root-dev` `root-2.45.2-dev` `root-2.45-dev` `root-2-dev` `glibc-root-2-dev` `latest-glibc-root-dev` `glibc-root-2.45.2-dev` `glibc-root-2.45-dev` | June 8th     | `sha256:aa41e16c56ea9a1b747fac93df73ad9ffcbcb977ebf08b144c1fb0c31223a725` |
|  `glibc-2.45.2-dev` `glibc-2.45-dev` `2.45-dev` `latest-dev` `2-dev` `latest-glibc-dev` `2.45.2-dev` `glibc-2-dev`                                         | June 8th     | `sha256:f7ce6af969019428fa5c3a8b7f000e9046850b1fc8f30c6e3c2003660bbd4f8f` |
|  `glibc-2.45.2` `latest` `glibc-2.45` `2.45` `2.45.2` `glibc-2` `latest-glibc` `2`                                                                         | June 8th     | `sha256:db3f6d68083d75451084d6aa1e83705c9fbbf006eec9d6e4a05e004f7d03a25c` |

