---
title: "php Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the php Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/php/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/php/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/php/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/php/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                                | Last Changed | Digest                                                                    |
|----------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev-fpm` `latest-fpm`         | July 3rd     | `sha256:3f820918e5f60b8e584f7fe6483d8421913a23ff4e209a9ab9938283e82c7f60` |
|  `latest-fpm-dev` `latest-dev-fpm-dev` | July 3rd     | `sha256:055c707220ab250ad2c8c53900d3753070bb986590a047eebb315d39983895ec` |
|  `latest-dev`                          | July 3rd     | `sha256:4cb4e32fb3f6fbae908b9e974ff57fedee424d34f5d3a03bea14367ab4a10e57` |
|  `latest`                              | July 3rd     | `sha256:8fe24d88dc73aeb0c0d32712d37c9834d4158eb5594ca8c2481cec440cafa073` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                        | Last Changed | Digest                                                                    |
|--------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `8.3.9-r0-fpm` `8.3-fpm` `8-fpm` `latest-fpm` `8.3.9-fpm`                     | July 3rd     | `sha256:1e74ac79447d8c3282c601fa1580c3e2bc0be44c2cebd15eb56be3bde4770cf2` |
|  `8.2.21-r0-fpm-dev` `8.2.21-fpm-dev` `8.2-fpm-dev`                            | July 3rd     | `sha256:52d1b372cfefde88dc3855e996ff84b373e34e8fa90f2aeb4a0ba9ff9e011bc6` |
|  `8.2-fpm` `8.2.21-fpm` `8.2.21-r0-fpm`                                        | July 3rd     | `sha256:ba7c2387563b095feb80375044ce98d8e377df7861e73f67274805ec88680af1` |
|  `8` `latest` `8.3.9` `8.3`                                                    | July 3rd     | `sha256:01b4d8c9d9f7b43d917684902159dca403a38080f2a171f28c15eea0c30eddd2` |
|  `8-fpm-dev` `8.3-fpm-dev` `latest-fpm-dev` `8.3.9-r0-fpm-dev` `8.3.9-fpm-dev` | July 3rd     | `sha256:6baf49086a8f11de87a8901071da432e9a960fb0290528092c4512969bbe3983` |
|  `8.2.21-dev` `8.2-dev`                                                        | July 3rd     | `sha256:8712e4b95816512db904d2ea5bdb1c3fa5d06b64bbfe4682c501d731f387b71b` |
|  `8-dev` `8.3.9-dev` `latest-dev` `8.3-dev`                                    | July 3rd     | `sha256:f0d87c43bedfd1563c77a7e6ff7c553aa4fc97dcccca218ea673c79437bfdf03` |
|  `8.2.21` `8.2`                                                                | July 3rd     | `sha256:edf30cb39fc643d5566a8d688a731bca33d746fece1bf6856266503e84127f15` |
|  `8.3.8-r4-fpm` `8.3.8-fpm`                                                    | June 28th    | `sha256:249b462f275684051f7bab1462ddfe492108b5d8632384ff00cac91472d19222` |
|  `8.2.20`                                                                      | June 28th    | `sha256:278b56701381cc44247ad96ccc63c1ce00b428df12e3e31248e0929e7ab9dc5c` |
|  `8.2.20-dev`                                                                  | June 28th    | `sha256:300136c2fb18fc2e6310a31020d4dfbf4e3cbed22ad65f57aa583fbdb8c0fca0` |
|  `8.3.8-r4-fpm-dev` `8.3.8-fpm-dev`                                            | June 28th    | `sha256:dba8716b2d9403ec611f98b9673e64771a48fbc0a0fe45205c2dcc54b7a579b6` |
|  `8.2.20-r4-fpm-dev` `8.2.20-fpm-dev`                                          | June 28th    | `sha256:3759834054efdfa516d6242ef24bc88eaccd9adc1f03a6e08397b3399eb21633` |
|  `8.3.8-dev`                                                                   | June 28th    | `sha256:3f43d4be994c677840606013323e5cb8f889840e5123eeb69f58b93ee9ea4051` |
|  `8.2.20-fpm` `8.2.20-r4-fpm`                                                  | June 28th    | `sha256:e47d683f944620bbc167fd7ff77f104f5f7347f07eb2f5492ab34541f34003a7` |
|  `8.3.8`                                                                       | June 28th    | `sha256:1bc05bb186265b0a10d9a8fd0463ba6e4ec355440cc2c79b94ab4009c7e25cd7` |

