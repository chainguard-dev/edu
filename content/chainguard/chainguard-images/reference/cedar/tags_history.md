---
title: "cedar Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cedar Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-16 00:33:13
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cedar/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cedar/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cedar/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cedar/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | March 15th   | `sha256:2dc39609000752c176c57367cd8e73cd0563e47608657a80597efb63ad3e1ff5` |
|  `latest-dev` | March 15th   | `sha256:f9dbfde3018c40df165355b4b7e35344be8da98d2656ff374f34862b48400dd0` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.1-dev` `3-dev` `latest-dev` `3.1.1-dev` | March 15th   | `sha256:7ade9730f3aab1343228aa19154f58cacd95b7bcc61295a90fe25260371126dd` |
|  `3` `latest` `3.1` `3.1.1`                 | March 15th   | `sha256:ddba38b4b8f7f7b623daffddbd62d1859d3485accec0cfb7b1670676311a7e4c` |
|  `3.1.0`                                    | March 14th   | `sha256:8fc3c1355bb7f4f67450e4059bd2362215c23c085a67d9064685280c4dc0e38f` |
|  `3.1.0-dev`                                | March 14th   | `sha256:f221d3cbd9ee7beb5099e58d2d48ab17da7b4855e3528673593b4e8c9dfd8ef1` |
|  `3.0-dev` `3.0.1-dev`                      | March 8th    | `sha256:c6e01f06c064c4113639003fafefddb4a4fab50f0d924aa6988be90dc5e75ae6` |
|  `3.0` `3.0.1`                              | March 8th    | `sha256:4d86d482eecc0cb5c2c2ade17e5b13db5925b60d24f59540c84f2a29c769caef` |

