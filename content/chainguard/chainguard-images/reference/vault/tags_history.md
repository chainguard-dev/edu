---
title: "vault Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vault Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-13 00:52:18
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
|  `latest-dev` | March 12th   | `sha256:38b89b4f7dd41f59aea788006cf93111bb4cfe615233bb7350a35b8cac1954e3` |
|  `latest`     | March 8th    | `sha256:89b3db4e93eb693dee267a7f3013c41d0223e8fd7e9802d5e7322ead773dc630` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed  | Digest                                                                    |
|------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` `1.14-dev` `1-dev` `1.14.10-dev` | March 12th    | `sha256:c5def4d843534fb853a7712f9a5e71b75204cde5445382559903b3f421e0f3d7` |
|  `1.13.13-dev` `1.13-dev`                      | March 12th    | `sha256:8fead715ae47fdc57115d991d1f615fe5876ec80cd8d2906ead13cfc2bb0fe2b` |
|  `1.13` `1.13.13`                              | March 8th     | `sha256:6ab5702ac9f5e4c3a4681bcff594577df8b5101289a6804f9a0aed1b05550d2b` |
|  `1.14` `latest` `1.14.10` `1`                 | March 8th     | `sha256:b3099cbfb2cca00266fe3285a6f583545503860c3f2b9a606a69ad15e3584196` |
|  `1.14.9-dev`                                  | February 27th | `sha256:3239e153ebec18347066b76b41c79b9ecf441c0ee825f74807324da2f1b414f4` |
|  `1.14.9`                                      | February 27th | `sha256:6e04d877a280a04e39f1ea029828ae76b2a300a6324e74c6d7c0338ee26cbd45` |
|  `1.14.8`                                      | February 26th | `sha256:77481e31f8a762eb93b4a098126b222c69bea62e9db1548e66d8c88459053d30` |
|  `1.14.8-dev`                                  | February 26th | `sha256:2642f88d27bd217d235c9c8a781c8392cf94ff0e1a5d1c6c61ec6ee6ae9d9e7f` |

