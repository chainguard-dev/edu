---
title: "node Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-23 00:45:07
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
|  `next-dev` `latest-dev` | May 22nd     | `sha256:25b63df3235dc7f07bef5051dc666053720d8739e5346d05cf977420d0d51d2f` |
|  `next`                  | May 21st     | `sha256:911313940c00bf663640312a621ba51f680bccc989cae8dd7026934733762248` |
|  `latest`                | May 21st     | `sha256:65217f5e41f2113b45dc2b12b917b71bffd4f6bde001b1bb0f433782a0063d73` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                   | Last Changed | Digest                                                                    |
|-----------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `18-dev` `18.20.3-dev` `18.20-dev`                       | May 22nd     | `sha256:bd12678b4ec09c86f48e5705f9da949842a4067624503ddedf49baf84971a379` |
|  `20.13-dev` `20.13.1-dev` `20-dev`                       | May 22nd     | `sha256:2a95540a53743564edb38e7f839a366b6340927c87778c786f4de27063033118` |
|  `21.7-dev` `21.7.3-dev` `21-dev`                         | May 22nd     | `sha256:388229bc390d950b076a73575bde5eab734c5995e4d304ec9bc067ce2e901e43` |
|  `22.2-dev` `22.2.0-dev` `latest-dev` `22-dev` `next-dev` | May 22nd     | `sha256:13843a72fb34dabbf9cee22f3b64bcf4bec492a4e470787309aaa698456e41b3` |
|  `22.2` `latest` `22.2.0` `22`                            | May 21st     | `sha256:fa6641cd98385d3480287603d597174126bf39434c00a4f052ffb4da00771469` |
|  `20.13.1` `20.13` `20`                                   | May 21st     | `sha256:ca9461bd676f90047bb97bf69ea17523ae60b5575faa964ded0fbe96241e0c99` |
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

