---
title: "node Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-22 00:47:17
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
|  `latest-dev` `next-dev` | May 21st     | `sha256:bfb3d7d5bf3c6cba13c957ed31fa57669fe6d4e20104ac1bdf40e6ca335cb858` |
|  `next`                  | May 21st     | `sha256:911313940c00bf663640312a621ba51f680bccc989cae8dd7026934733762248` |
|  `latest`                | May 21st     | `sha256:65217f5e41f2113b45dc2b12b917b71bffd4f6bde001b1bb0f433782a0063d73` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                   | Last Changed | Digest                                                                    |
|-----------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `20-dev` `20.13-dev` `20.13.1-dev`                       | May 21st     | `sha256:dcb2efc17cb1017daefddd6400ac33939283fb606d32cbe20bd8b9b59a969b0d` |
|  `22.2` `latest` `22.2.0` `22`                            | May 21st     | `sha256:fa6641cd98385d3480287603d597174126bf39434c00a4f052ffb4da00771469` |
|  `21-dev` `21.7.3-dev` `21.7-dev`                         | May 21st     | `sha256:8ae9dac656f12023aa8a57858b3e3363e10bbfaecb5b3e2152fb76c1c7bee77b` |
|  `20.13.1` `20.13` `20`                                   | May 21st     | `sha256:ca9461bd676f90047bb97bf69ea17523ae60b5575faa964ded0fbe96241e0c99` |
|  `18-dev` `18.20-dev` `18.20.3-dev`                       | May 21st     | `sha256:a2af3024d464e592d6895dcda1203c3329211553609ba46f45d5ac0f513bec48` |
|  `22.2-dev` `latest-dev` `22.2.0-dev` `next-dev` `22-dev` | May 21st     | `sha256:16036ffdd7c87e5e44f97926442fe4265232a107cc86d5fc56d70ed0b5017a9c` |
|  `21` `21.7` `21.7.3`                                     | May 21st     | `sha256:d2934ff192022b5b1e45d441dd8d63b3b6471785564abaa8628f98692f2201df` |
|  `18.20.3` `18` `18.20`                                   | May 21st     | `sha256:4b94683dc965e76ce2afe1bc16c946d05c95403aa632f79d976644ae1db54684` |
|  `next`                                                   | May 21st     | `sha256:8602b5df058dd6dc4775741d29e0de4e767d6312ba40fe2f458599397a6a873b` |
|  `18.20.2`                                                | May 19th     | `sha256:40733764fe090c9bcd1e943818bdd975d5ee17e7a4d579f320c7a363ae8f6f74` |
|  `18.20.2-dev`                                            | May 19th     | `sha256:da6f70486bb6dbca23f0e3a322dfd052e57c8a8ecf44e6778b13029f3eaa7066` |
|  `22.1-dev` `22.1.0-dev`                                  | May 15th     | `sha256:7f1549a91f56d8d8d27b871f7ae5f693157ac7be75bfd941d1dff48f84104600` |
|  `22.1.0` `22.1`                                          | May 15th     | `sha256:3587f6a3b187af7a03c09c41bd21a7f7fc75c5f07108299d3aec281c6ffbae76` |
|  `20.13.0-dev`                                            | May 8th      | `sha256:62ca60aa7ac471aa4aea21a8ebc3a9a69f652fbc5ab1f22dfe423fb4c4e53e9a` |
|  `20.13.0`                                                | May 7th      | `sha256:81c7c3639a70971a7866537d53deebf94b3eedd1e927034493d47c229ebe9656` |
|  `20.12.2` `20.12`                                        | May 2nd      | `sha256:922c19c9c578f2a193e00c11b27dc22c7354e486017dea73b3fb7fa6a31cc5c0` |
|  `20.12-dev` `20.12.2-dev`                                | May 2nd      | `sha256:6162388c347358eded9ecc93682e7b715b39f63f30fc8394488e9eeabc1e0fd9` |
|  `22.0-dev` `22.0.0-dev`                                  | May 2nd      | `sha256:322be128bd5a103e80b3302e41a037001d7d5b550683153db9bd7ffeb18f84fd` |
|  `22.0` `22.0.0`                                          | May 2nd      | `sha256:2212e761e601d4e4aa976527b9e610c3ac3ba6984987451128da61ddc12df585` |
|  `20.1.0-dev` `20.1-dev`                                  | May 18th     | `sha256:35a03fe6c2858aca34b0eb1c870f587ddaf949a8d3ae137f2731f56f6d7fde21` |
|  `20.1.0` `20.1`                                          | May 18th     | `sha256:81895e4eb72fd7a23c3702a943c3375002ca7d91d09c20d3d3c5a6bb9f6973b3` |
|  `20.0.0-dev` `20.0-dev`                                  | May 3rd      | `sha256:bf17a2b888d06441189fa2ae2e7cfec52a040222a15c4ec8f3bcf390e802b460` |
|  `20.0.0` `20.0`                                          | May 3rd      | `sha256:0b36acd8be48f10ad5f7e954c194cf62be13ae4eb5d6f7a998beac7d5938cbe0` |

