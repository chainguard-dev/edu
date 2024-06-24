---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-24 00:43:49
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
|  `latest-dev`            | June 23rd    | `sha256:846e1a4dbb50d840bf799f49688647f93028416217cebe3631572806a9c51fb2` |
|  `latest-root`           | June 23rd    | `sha256:d6631a4bfaa73f5edc536bfd7ab9e165f394a6fc1ff1e8834574f49bc0f4c2e9` |
|  `latest-root-dev`       | June 23rd    | `sha256:f9a47a22f7d4e93f5b31ce55b4ebfdf6aa8b5ac7dc85664846c474308c760bb1` |
|  `latest`                | June 23rd    | `sha256:06119871a608d163eac2daddd0745582e457a29ee8402bd351c13f294ede30e1` |
|  `latest-glibc-root-dev` | June 22nd    | `sha256:364fe5e098b2de412679ceddcdc767aeb189952977042b8b77a3f461727a5233` |
|  `latest-glibc-dev`      | June 22nd    | `sha256:fd35ff8980c0765eaea136e476140da1bcb22175edc6c2b977297d57a5fe5143` |
|  `latest-glibc`          | June 22nd    | `sha256:56d28739399b640156a4d74949aa174c2e0b287ade802e245baef17d267bd8b3` |
|  `latest-glibc-root`     | June 22nd    | `sha256:8eefe85fda9b0c6d15f9ed8bca7ef830678c86c0c9e75b6828f124703a398d3c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                                                                                    | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.45.2` `glibc-2.45.2` `latest-glibc` `glibc-2` `latest` `2.45` `2` `glibc-2.45`                                                                         | June 23rd    | `sha256:30ca67a9818e3f25dae19fe2a5c93d88394468690b13f9d7efe222891d0f4d41` |
|  `2.45-dev` `2-dev` `glibc-2.45.2-dev` `latest-glibc-dev` `glibc-2-dev` `latest-dev` `glibc-2.45-dev` `2.45.2-dev`                                         | June 23rd    | `sha256:92568f54245f1bb6188373abd9d0282cb228e2437f0f86f17d479042f2a6213d` |
|  `glibc-root-2.45` `glibc-root-2.45.2` `latest-glibc-root` `root-2.45.2` `latest-root` `root-2.45` `glibc-root-2` `root-2`                                 | June 23rd    | `sha256:5437df373bec1c2311c71b79e09f632bdfdf9aab7049a0ebbf6ca97a874d78a2` |
|  `latest-root-dev` `latest-glibc-root-dev` `root-2-dev` `glibc-root-2.45-dev` `root-2.45.2-dev` `root-2.45-dev` `glibc-root-2.45.2-dev` `glibc-root-2-dev` | June 23rd    | `sha256:0fc3fb76bf15ff3698fd913b2d10a19e2917176a9b976635d599d0297b547d7a` |

