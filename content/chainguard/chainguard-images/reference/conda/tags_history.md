---
title: "conda Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the conda Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-23 00:43:06
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/conda/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/conda/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/conda/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/conda/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | June 22nd    | `sha256:24a7513dfcc79bfe060d7be60cd6ae100c1c98c2c2e29c73f4f34540f84f1c7b` |
|  `latest-dev` | June 22nd    | `sha256:8dbdeadbed251739be24d23eb5ad50f0f7dfcd7453aff1fbb5fc3946c45a1ccf` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `24.5-dev` `24.5.0-dev`                       | June 21st    | `sha256:a92ccd96cc67f8c48eb0e6cb5908ff15b68af838118b70f26f39bf5dd5e2ba3a` |
|  `24.5.0` `24.5`                               | June 21st    | `sha256:f0fa4cb1056af4d5a837b35ebe4b12e3bb9a88c2d89284484cfaedca2ba950fb` |
|  `24.1.1`                                      | June 21st    | `sha256:7cb1e5644527fb7ddea98fbe10f8b657fd58edba4db00d34fb7c6b62d6f8ee89` |
|  `latest` `24.1.2` `24` `24.1`                 | June 21st    | `sha256:8c68c3af1806da11902cf2a7d9155c757362ad879db3d22b63b27a0f1ab4fc18` |
|  `24.1-dev` `latest-dev` `24.1.2-dev` `24-dev` | June 21st    | `sha256:0836091bd389f7614ebe3c96926ceda652ebbf79a9de5bb749c4d0f5039ba4b1` |
|  `24.1.1-dev`                                  | June 21st    | `sha256:ce4391544066ff1532fcc57cd727acca738eba48f9e9092e46016b4a70cde0ff` |

