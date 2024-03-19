---
title: "vault Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vault Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-19 00:54:00
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
|  `latest`     | March 18th   | `sha256:00c09364906f8d27786e4d7c0ce98101292bc99066c7193f6404ca65143c73dd` |
|  `latest-dev` | March 18th   | `sha256:7b50c96b439df48c7bda32e4beacf906c2608a076770ba7178f952871ef60d29` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed  | Digest                                                                    |
|------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `1.13-dev` `1.13.13-dev`                      | March 18th    | `sha256:06c023d7150d005a529fc4102a015f4cb7830911689f1c7f3de18965a90409c4` |
|  `1-dev` `1.14-dev` `1.14.10-dev` `latest-dev` | March 18th    | `sha256:9424d060a9050a6e7b7910389d194821f93575d361f4216ef23a71489e0f1917` |
|  `1.13` `1.13.13`                              | March 18th    | `sha256:438be44b21d7ad237076e5f99d9937cd31e9f0170e15f436af537ea9e272c59c` |
|  `1.14.10` `1.14` `1` `latest`                 | March 18th    | `sha256:9b7932e5242bcea62c2f13edcf4617f7379d912e32def4e46e64972eac80724d` |
|  `1.14.9-dev`                                  | February 27th | `sha256:3239e153ebec18347066b76b41c79b9ecf441c0ee825f74807324da2f1b414f4` |
|  `1.14.9`                                      | February 27th | `sha256:6e04d877a280a04e39f1ea029828ae76b2a300a6324e74c6d7c0338ee26cbd45` |
|  `1.14.8`                                      | February 26th | `sha256:77481e31f8a762eb93b4a098126b222c69bea62e9db1548e66d8c88459053d30` |
|  `1.14.8-dev`                                  | February 26th | `sha256:2642f88d27bd217d235c9c8a781c8392cf94ff0e1a5d1c6c61ec6ee6ae9d9e7f` |

