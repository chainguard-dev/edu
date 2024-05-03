---
title: "loki Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the loki Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/loki/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/loki/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/loki/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/loki/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 2nd      | `sha256:d8241edc4bc8b2e3089b5dd15eeba88b128b2847081a8d04091abdaad0e0d792` |
|  `latest`     | May 2nd      | `sha256:fa933c4654448d26358703731281fca394f93638c0504f095e8d78ab1845f6b0` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3` `latest` `3.0` `3.0.0`                 | May 2nd      | `sha256:8f4cfad760246975be1fd037619699c4d3622b4fac9f5aefb1adaeb4f430d406` |
|  `latest-dev` `3.0-dev` `3-dev` `3.0.0-dev` | May 2nd      | `sha256:ed8ded42cf8f847471f2178cb3c351f53915793087a51ec6e6241485d1c8bde5` |
|  `2-dev` `2.9.6-dev` `2.9-dev`              | April 5th    | `sha256:01c011a9aa43a67ac97befaa515f896a34d8a718ca1a141a3fe9ae8b740d1283` |
|  `2.9.6` `2.9` `2`                          | April 3rd    | `sha256:4863ce4e3e24b48368ab8fca9e10fa86a859813b612096668cd1fcd3e50cd963` |

