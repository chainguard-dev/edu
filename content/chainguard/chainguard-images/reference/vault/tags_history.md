---
title: "vault Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vault Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-08 00:34:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/vault/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/vault/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/vault/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/vault/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | July 3rd     | `sha256:890366f5c7fd6a1482873ba65d6dc2d0eff52201b78b78a917fd847ef55ac5f2` |
|  `latest-dev` | July 3rd     | `sha256:031759c9eba0bdec8eb3eff73493a3cb309d92b7b97e3071b6c7686c2b735b3e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16.3-dev` `1.16-dev`                      | July 6th     | `sha256:68a1fd99d884af9b6ed1dd6fb2996b0c3e755dea5f1789719523aa4fb560a980` |
|  `1.17.1` `1` `1.17` `latest`                 | July 6th     | `sha256:be6b6aee6eae20c020e919749b8055827e89307dbe616e683ebc116ab65a53b4` |
|  `latest-dev` `1.17.1-dev` `1.17-dev` `1-dev` | July 6th     | `sha256:b530e70763b8d92e7f932213b5f0eaecf75a8e370ecbaf8c432864f264074a4f` |
|  `1.16.3` `1.16`                              | July 6th     | `sha256:b132f19aa5bd89cdd6c16d724af487536a5805a5820acff1ce14e59c48de4ef2` |
|  `1.15` `1.15.9`                              | July 6th     | `sha256:e3a417d91b20af0995b57a9baab2e0f655d6decc83cc28511802c4839916299f` |
|  `1.15.9-dev` `1.15-dev`                      | July 6th     | `sha256:5a30e83441eb63044a78fa7df6ffe3c16ce29dacfedaa5b3f805897d0d0a4dd5` |

