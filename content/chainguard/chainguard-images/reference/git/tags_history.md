---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-25 00:42:19
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
|  `latest-glibc-dev`      | June 24th    | `sha256:367c36e0ec44ec2a6ec9d1153c0ce17f8b3794d0271320ced62812393c60c98f` |
|  `latest-glibc-root-dev` | June 24th    | `sha256:2b64a5e7921603f1dc0aed0689951a5cd89b8635727325f11e3543e56c296c81` |
|  `latest-glibc-root`     | June 24th    | `sha256:4e5ee5286a27e2091140d6141bf69f089857523ece58b951944bafa573a2304f` |
|  `latest-glibc`          | June 24th    | `sha256:4beb1cdaacefaee680734fc564c91498687b858e2834e799044ac7369211e896` |
|  `latest-dev`            | June 23rd    | `sha256:846e1a4dbb50d840bf799f49688647f93028416217cebe3631572806a9c51fb2` |
|  `latest-root`           | June 23rd    | `sha256:d6631a4bfaa73f5edc536bfd7ab9e165f394a6fc1ff1e8834574f49bc0f4c2e9` |
|  `latest-root-dev`       | June 23rd    | `sha256:f9a47a22f7d4e93f5b31ce55b4ebfdf6aa8b5ac7dc85664846c474308c760bb1` |
|  `latest`                | June 23rd    | `sha256:06119871a608d163eac2daddd0745582e457a29ee8402bd351c13f294ede30e1` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                                                                                    | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.45.2` `glibc-2.45.2` `latest-glibc` `glibc-2` `latest` `2.45` `2` `glibc-2.45`                                                                         | June 23rd    | `sha256:30ca67a9818e3f25dae19fe2a5c93d88394468690b13f9d7efe222891d0f4d41` |
|  `2.45-dev` `2-dev` `glibc-2.45.2-dev` `latest-glibc-dev` `glibc-2-dev` `latest-dev` `glibc-2.45-dev` `2.45.2-dev`                                         | June 23rd    | `sha256:92568f54245f1bb6188373abd9d0282cb228e2437f0f86f17d479042f2a6213d` |
|  `glibc-root-2.45` `glibc-root-2.45.2` `latest-glibc-root` `root-2.45.2` `latest-root` `root-2.45` `glibc-root-2` `root-2`                                 | June 23rd    | `sha256:5437df373bec1c2311c71b79e09f632bdfdf9aab7049a0ebbf6ca97a874d78a2` |
|  `latest-root-dev` `latest-glibc-root-dev` `root-2-dev` `glibc-root-2.45-dev` `root-2.45.2-dev` `root-2.45-dev` `glibc-root-2.45.2-dev` `glibc-root-2-dev` | June 23rd    | `sha256:0fc3fb76bf15ff3698fd913b2d10a19e2917176a9b976635d599d0297b547d7a` |

