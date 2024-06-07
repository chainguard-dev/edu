---
title: "argocd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the argocd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-07 00:46:50
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/argocd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/argocd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/argocd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/argocd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | June 6th     | `sha256:ace727d7c1e7384a9493fc5b272072071dabd5e2e563d8e4d55eb5cdfeab7bba` |
|  `latest-dev` | June 6th     | `sha256:ce88e8ed8f246852a02c02ccd0658098cc25def2fd16a5cd298ed3e9cf1e9f1a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `2-dev` `2.10-dev` `2.10.12-dev` | June 6th     | `sha256:d0a770bca603d45549398b1afb36757e9ab17dea6475a908740cffb5f938a4c4` |
|  `2.10` `2.10.12` `latest` `2`                 | June 6th     | `sha256:e155299e69f17f780e71e7537a8f3967b1b19157e99289e111c626205ceb3a28` |
|  `2.10.11-dev`                                 | June 5th     | `sha256:eae1882515a316bcef90ca232774d0b5fa22282eb0950ccc51e4891dd4241e73` |
|  `2.9` `2.9.16`                                | June 5th     | `sha256:20dbc4ea1126beb0fca556e05b2757c43d0d14f44adb73df16fb648523e8ce1c` |
|  `2.10.11`                                     | June 5th     | `sha256:6bfd91603300505669dcd0a39485e8e86581eca207c59a31c6632b8d9c39388a` |
|  `2.9.16-dev` `2.9-dev`                        | June 5th     | `sha256:c1b4d469186b692bf19b28f4a57cb0b922cb0c7d6094e9a891a4787a70e7d247` |
|  `2.8.18-dev` `2.8-dev`                        | June 5th     | `sha256:6174f9451f0363ac258f596b96fdd927f2977bf1f611a7327542e379503c56f7` |

