---
title: "vault Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vault Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-05 17:06:05
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
|  `latest-dev` | March 1st    | `sha256:0b92b3605144fd215961328ef2e67644324573b5a6ec43a0f658e3d5dd1a6bd4` |
|  `latest`     | March 1st    | `sha256:0045296651e9f918d35095b3ce3723dcfbc88a5ea6f2540cfff76021f5745689` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed  | Digest                                                                    |
|------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `1.13.13-dev` `1.13-dev`                      | March 2nd     | `sha256:06db085b31bc439aae2d333a5cbda8ef6a510583f197139fe32ca3fcee1b3dbc` |
|  `1-dev` `1.14.10-dev` `latest-dev` `1.14-dev` | March 2nd     | `sha256:67de60518503aabb7e61abc4b8ea45f9c5a59a0ce43fcaa1924df67d59b91668` |
|  `1.14.10` `1` `1.14` `latest`                 | March 1st     | `sha256:4e7fb55b48012855bb878f89a33476d228aa1ecc353f7c697045881099a59852` |
|  `1.13.13` `1.13`                              | March 1st     | `sha256:2cb162410f8b06463c52af14b3f6a8d3dd25d9f073ad55225ea25a23dfe9ddf7` |
|  `1.14.9-dev`                                  | February 27th | `sha256:3239e153ebec18347066b76b41c79b9ecf441c0ee825f74807324da2f1b414f4` |
|  `1.14.9`                                      | February 27th | `sha256:6e04d877a280a04e39f1ea029828ae76b2a300a6324e74c6d7c0338ee26cbd45` |
|  `1.14.8`                                      | February 26th | `sha256:77481e31f8a762eb93b4a098126b222c69bea62e9db1548e66d8c88459053d30` |
|  `1.14.8-dev`                                  | February 26th | `sha256:2642f88d27bd217d235c9c8a781c8392cf94ff0e1a5d1c6c61ec6ee6ae9d9e7f` |
|  `1.13.12-dev`                                 | February 6th  | `sha256:054aaab7187e088481c1f573fca6be6137f0fd162f21636da3640b95efdbe50f` |
|  `1.13.12`                                     | February 6th  | `sha256:98bfc28168717f32b6c9710b02eaf4a92b37798b54d5b98e8bfb5101d0583bb7` |

