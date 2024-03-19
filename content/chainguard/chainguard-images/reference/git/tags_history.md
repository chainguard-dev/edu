---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-19 00:54:00
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
|  `latest-root`           | March 18th   | `sha256:9fe5c7c29b361fb51c387100cd9adce9e55b911b57651e83e799606f7816ac67` |
|  `latest-root-dev`       | March 18th   | `sha256:597c51d3494959984b6e34104300d258fa10833d6e5126a4cc5ce133d6e8e69c` |
|  `latest-dev`            | March 18th   | `sha256:cffd5df7ff5203c845b64f80ae75c1fde318fd6520bd89cfafe7383ec6ff3ef2` |
|  `latest`                | March 18th   | `sha256:06ae501228872f9dbc1bf30d6083f36ee7480d7a2d9b19edaad4405aba9f3e89` |
|  `latest-glibc-root`     | March 18th   | `sha256:ab594bb96fbed2266298bc9ee28dfadb2272f776de316f8f48cd3501e570dadb` |
|  `latest-glibc`          | March 18th   | `sha256:e3adff494b3210e1725aa6c06a00e69f46927313bfd7b3f1b21566ba299503f9` |
|  `latest-glibc-root-dev` | March 18th   | `sha256:82ff9a966a536b9a662e22b0cb142e790d7e728880d1ca18ac61033d1c533b2c` |
|  `latest-glibc-dev`      | March 18th   | `sha256:22f095b43bcefe2b90ac440350f4d6119dc99b4218ed2cd8331a0405449917dd` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                   | Last Changed  | Digest                                                                    |
|-------------------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `glibc-2.44.0-dev` `glibc-2-dev` `latest-glibc-dev` `glibc-2.44-dev`                     | March 18th    | `sha256:44ea776d228167ab20ef0a889f66c8f568eccddd7e5d04979740a2f99cb2f597` |
|  `glibc-2.44.0` `glibc-2` `glibc-2.44` `latest-glibc`                                     | March 18th    | `sha256:d0f2d117ba83a581e6c653f6aa1252f1bd670a14ba714cf3894d70d9489cdd52` |
|  `glibc-root-2-dev` `glibc-root-2.44.0-dev` `latest-glibc-root-dev` `glibc-root-2.44-dev` | March 18th    | `sha256:ce8b3aa79042243857d8a01f6db8a911f74eec7df2b63fc2f0f5c7b479706f50` |
|  `glibc-root-2` `glibc-root-2.44` `latest-glibc-root` `glibc-root-2.44.0`                 | March 18th    | `sha256:d6484971df054b75fb4efcb718b70ca1d7479de2bcf1bb8749766deaa6001df4` |
|  `glibc-2.43` `glibc-2.43.2`                                                              | February 22nd | `sha256:d3faa9aada431456a32f757b528c236b155777ff345ce01d15d5f0c424cf43bc` |
|  `glibc-2.43.2-dev` `glibc-2.43-dev`                                                      | February 22nd | `sha256:83620a49e96e024aa0f58042a5cee8bfba67d41c91d73b61c17ae2c0f6ec8392` |
|  `glibc-root-2.43.2` `glibc-root-2.43`                                                    | February 22nd | `sha256:1cf940d7ecc5ec0ac4bf8d000aefc4be4244f0ec8f68a11acab20fe0f5c0c5d7` |
|  `glibc-root-2.43.2-dev` `glibc-root-2.43-dev`                                            | February 22nd | `sha256:14e46233504bdb7d69370eace59e67db5da0bc05e7db079c7f96fbae1c7ec99a` |

