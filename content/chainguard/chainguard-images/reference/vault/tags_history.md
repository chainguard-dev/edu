---
title: "vault Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vault Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-18 00:56:27
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
|  `latest`     | March 15th   | `sha256:daf9805028386f0fe79956e623cce7577cd148f4ee3329ce636b09f75fabec42` |
|  `latest-dev` | March 15th   | `sha256:afe64c90a35644d71f0340420d38c61eca6a8442083244ce70b08019f17e20cc` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed  | Digest                                                                    |
|------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `1.13` `1.13.13`                              | March 16th    | `sha256:69febf3f5203408c7921c6577d378cc48f31296da23de28120299c2deed35011` |
|  `1.13.13-dev` `1.13-dev`                      | March 16th    | `sha256:9d6ba457b269f18a89a4bf2e1260f13450856ff399682dd8f7f738fd12a7db52` |
|  `latest` `1` `1.14.10` `1.14`                 | March 14th    | `sha256:4f1b409b56fac063039a5c0067f709f4a2c6eece7146c77627427315b2981196` |
|  `1.14.10-dev` `1-dev` `latest-dev` `1.14-dev` | March 14th    | `sha256:9f66ddbf26261d79014ba9baae35f55046553cfd0f9574f188a434548ed45ead` |
|  `1.14.9-dev`                                  | February 27th | `sha256:3239e153ebec18347066b76b41c79b9ecf441c0ee825f74807324da2f1b414f4` |
|  `1.14.9`                                      | February 27th | `sha256:6e04d877a280a04e39f1ea029828ae76b2a300a6324e74c6d7c0338ee26cbd45` |
|  `1.14.8`                                      | February 26th | `sha256:77481e31f8a762eb93b4a098126b222c69bea62e9db1548e66d8c88459053d30` |
|  `1.14.8-dev`                                  | February 26th | `sha256:2642f88d27bd217d235c9c8a781c8392cf94ff0e1a5d1c6c61ec6ee6ae9d9e7f` |

