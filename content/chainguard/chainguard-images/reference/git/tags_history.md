---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-23 00:43:06
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
|  `latest-glibc-root-dev` | June 22nd    | `sha256:364fe5e098b2de412679ceddcdc767aeb189952977042b8b77a3f461727a5233` |
|  `latest-glibc-dev`      | June 22nd    | `sha256:fd35ff8980c0765eaea136e476140da1bcb22175edc6c2b977297d57a5fe5143` |
|  `latest-glibc`          | June 22nd    | `sha256:56d28739399b640156a4d74949aa174c2e0b287ade802e245baef17d267bd8b3` |
|  `latest-glibc-root`     | June 22nd    | `sha256:8eefe85fda9b0c6d15f9ed8bca7ef830678c86c0c9e75b6828f124703a398d3c` |
|  `latest-dev`            | June 20th    | `sha256:d6b758ccc816bb1d4a497a07673dfb7aadc58f6527ef20deb61ce47df7f765f6` |
|  `latest-root-dev`       | June 20th    | `sha256:84adff7a4230c46bd633781cc05b92f744c937c6bc7ef7907625ff91cbc931e1` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                                                                                    | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `glibc-root-2.45-dev` `latest-root-dev` `root-2.45.2-dev` `glibc-root-2.45.2-dev` `glibc-root-2-dev` `latest-glibc-root-dev` `root-2.45-dev` `root-2-dev` | June 21st    | `sha256:55edfad800dc180155cc0ecd51cca4bbeaabab7f1a1f12e967ea0e077dd759a0` |
|  `glibc-2-dev` `2-dev` `glibc-2.45.2-dev` `2.45-dev` `2.45.2-dev` `glibc-2.45-dev` `latest-dev` `latest-glibc-dev`                                         | June 21st    | `sha256:16e8deb778de083e7e7dbdad0442bea1734f00e32bfc9e94c9b7ebfff57a96bd` |
|  `glibc-root-2.45.2` `glibc-root-2.45` `root-2.45.2` `root-2.45` `root-2` `latest-root` `glibc-root-2` `latest-glibc-root`                                 | June 21st    | `sha256:981c0ce53a14ad2b3037fb6f5bf33c7167d51896d1bac0173151570ad220fcf5` |
|  `latest-glibc` `glibc-2` `glibc-2.45.2` `latest` `2` `glibc-2.45` `2.45` `2.45.2`                                                                         | June 21st    | `sha256:a9694638f0b5a7b96beb63ad0ee10e4824e83c942fafa82221261cf75b74e85f` |

