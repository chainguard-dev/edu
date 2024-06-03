---
title: "node Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-03 00:46:08
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/node/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/node/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/node/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/node/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                  | Last Changed | Digest                                                                    |
|--------------------------|--------------|---------------------------------------------------------------------------|
|  `next-dev` `latest-dev` | June 1st     | `sha256:81631665ecc421181a3959e51de193030a52128ce10f904e3d70b33d7beeb0ea` |
|  `next`                  | May 30th     | `sha256:31305f7e6a2f9ee4184ba4b5f27e1535e259ee73a1cce89550afb30ef8cc57f4` |
|  `latest`                | May 30th     | `sha256:593d8e0dfcbcc3e13dd187cc5fc497e034c713a5a5a8813139409ef8c38673f4` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                   | Last Changed | Digest                                                                    |
|-----------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `22.2.0-dev` `latest-dev` `22-dev` `next-dev` `22.2-dev` | June 1st     | `sha256:7c89fe2aefec38c93b519c1355fc14329c8773abc0196342cb298ef43c6d06ef` |
|  `18.20.3-dev` `18.20-dev` `18-dev`                       | June 1st     | `sha256:45a7cbfcc4d2613db5bfb8eeae9ac0200925feb3df85e893be63b2ba60886029` |
|  `21.7.3-dev` `21-dev` `21.7-dev`                         | June 1st     | `sha256:17052070e684555cc73ef38722479c52338c64e8df308192ae7de30c54544ed5` |
|  `20-dev` `20.14.0-dev` `20.14-dev`                       | June 1st     | `sha256:5439832697ed160e0038c80e349e68abfba70e64076c50d980dd5122625b08c5` |
|  `21.7.3` `21.7` `21`                                     | May 30th     | `sha256:751c8e4ff122571cda03a93006e9068caee3b268bb868541e426fb7ca3f63154` |
|  `18.20.3` `18` `18.20`                                   | May 30th     | `sha256:bcc52e79b5799944b8808553fe0e66e3841687baa0eae30917450de2cc6a5729` |
|  `20.14.0` `20` `20.14`                                   | May 30th     | `sha256:cc9f2d2ba0ba40d81d6082b5ba7396e6ace4540152bd804dd7aef6db5618720a` |
|  `22.2.0` `22` `22.2` `latest`                            | May 30th     | `sha256:cbaa5a247fcf5f638ba084dcc7c6b892e2dbc6ea49ae7b70327d010c6034f860` |
|  `next`                                                   | May 30th     | `sha256:03060dd8db57a4b870563ccfaa26389b806a7e079fdb6b8e4155a254e6844fc2` |
|  `20.13-dev` `20.13.1-dev`                                | May 28th     | `sha256:3b06cf35766f3f767063c21a8233a69f89a7d7fa4a4053f7a1210feefcbdc639` |
|  `20.13.1` `20.13`                                        | May 24th     | `sha256:a98fbe07a27092ae33051b896756622af2c5bea88f4f45ab851613a823e2b0b1` |
|  `18.20.2`                                                | May 19th     | `sha256:40733764fe090c9bcd1e943818bdd975d5ee17e7a4d579f320c7a363ae8f6f74` |
|  `18.20.2-dev`                                            | May 19th     | `sha256:da6f70486bb6dbca23f0e3a322dfd052e57c8a8ecf44e6778b13029f3eaa7066` |
|  `22.1-dev` `22.1.0-dev`                                  | May 15th     | `sha256:7f1549a91f56d8d8d27b871f7ae5f693157ac7be75bfd941d1dff48f84104600` |
|  `22.1.0` `22.1`                                          | May 15th     | `sha256:3587f6a3b187af7a03c09c41bd21a7f7fc75c5f07108299d3aec281c6ffbae76` |
|  `20.13.0-dev`                                            | May 8th      | `sha256:62ca60aa7ac471aa4aea21a8ebc3a9a69f652fbc5ab1f22dfe423fb4c4e53e9a` |
|  `20.13.0`                                                | May 7th      | `sha256:81c7c3639a70971a7866537d53deebf94b3eedd1e927034493d47c229ebe9656` |
|  `20.1.0-dev` `20.1-dev`                                  | May 18th     | `sha256:35a03fe6c2858aca34b0eb1c870f587ddaf949a8d3ae137f2731f56f6d7fde21` |
|  `20.1.0` `20.1`                                          | May 18th     | `sha256:81895e4eb72fd7a23c3702a943c3375002ca7d91d09c20d3d3c5a6bb9f6973b3` |
|  `20.0.0-dev` `20.0-dev`                                  | May 3rd      | `sha256:bf17a2b888d06441189fa2ae2e7cfec52a040222a15c4ec8f3bcf390e802b460` |
|  `20.0.0` `20.0`                                          | May 3rd      | `sha256:0b36acd8be48f10ad5f7e954c194cf62be13ae4eb5d6f7a998beac7d5938cbe0` |

