---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-25 00:49:44
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
|  `latest-root`           | March 24th   | `sha256:a1c7436ea2c10a19c392a13244b9e078c56505484c302507fd05e33f7431b8a6` |
|  `latest-dev`            | March 24th   | `sha256:886780fd02d07011b84606c1f86aef89a40a53bd12b297a37be2defec68eb8e0` |
|  `latest`                | March 24th   | `sha256:a16d82caaf47a26e27251ab4296f9e076557e7730494947adac4544217000b45` |
|  `latest-root-dev`       | March 24th   | `sha256:1ecc196a79733524762c8e89fa6242354e94b8b33711b84eef96266df1d02c75` |
|  `latest-glibc-root`     | March 18th   | `sha256:ab594bb96fbed2266298bc9ee28dfadb2272f776de316f8f48cd3501e570dadb` |
|  `latest-glibc`          | March 18th   | `sha256:e3adff494b3210e1725aa6c06a00e69f46927313bfd7b3f1b21566ba299503f9` |
|  `latest-glibc-root-dev` | March 18th   | `sha256:82ff9a966a536b9a662e22b0cb142e790d7e728880d1ca18ac61033d1c533b2c` |
|  `latest-glibc-dev`      | March 18th   | `sha256:22f095b43bcefe2b90ac440350f4d6119dc99b4218ed2cd8331a0405449917dd` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                   | Last Changed | Digest                                                                    |
|-------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `glibc-2.44.0-dev` `glibc-2-dev` `latest-glibc-dev` `glibc-2.44-dev`                     | March 18th   | `sha256:44ea776d228167ab20ef0a889f66c8f568eccddd7e5d04979740a2f99cb2f597` |
|  `glibc-2.44.0` `glibc-2` `glibc-2.44` `latest-glibc`                                     | March 18th   | `sha256:d0f2d117ba83a581e6c653f6aa1252f1bd670a14ba714cf3894d70d9489cdd52` |
|  `glibc-root-2-dev` `glibc-root-2.44.0-dev` `latest-glibc-root-dev` `glibc-root-2.44-dev` | March 18th   | `sha256:ce8b3aa79042243857d8a01f6db8a911f74eec7df2b63fc2f0f5c7b479706f50` |
|  `glibc-root-2` `glibc-root-2.44` `latest-glibc-root` `glibc-root-2.44.0`                 | March 18th   | `sha256:d6484971df054b75fb4efcb718b70ca1d7479de2bcf1bb8749766deaa6001df4` |

