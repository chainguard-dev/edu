---
title: "node Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-24 00:45:45
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
|  `latest-dev` `next-dev` | May 23rd     | `sha256:7f4892eb5f5247e5eba812299f1a51ecff3249f5e2f3956adb31faa53541271f` |
|  `next`                  | May 23rd     | `sha256:b125579d866df5a640319a09aec816496597f40ef7a53c878e8e632525b63de9` |
|  `latest`                | May 23rd     | `sha256:adc99e2e89bdfae3c6fd83921dc9a3c316015c069ec6a5559e147fb25c2a1d64` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                   | Last Changed | Digest                                                                    |
|-----------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `18-dev` `18.20-dev` `18.20.3-dev`                       | May 23rd     | `sha256:dbd433267e60f559109d629208898c4871c253c4f86efff20af6df972ea34a78` |
|  `latest` `22.2.0` `22.2` `22`                            | May 23rd     | `sha256:e1661b6d5a10f2cc7647e3a76b6a5c34b4d25f2e3a472b8d044dac13523493fb` |
|  `21.7` `21.7.3` `21`                                     | May 23rd     | `sha256:1e14a834558e50f3102d8e59bed28d8380526139a9c182189045f6897074a11f` |
|  `21.7-dev` `21.7.3-dev` `21-dev`                         | May 23rd     | `sha256:14d53661a49171240d14bc03577293bb66cb8a1329fb564cf18298e094e15eae` |
|  `18.20.3` `18.20` `18`                                   | May 23rd     | `sha256:ffbd82c84ccf76963e7580c9ca0064861bcf489223c230144cc6a510c5476c13` |
|  `20.13` `20` `20.13.1`                                   | May 23rd     | `sha256:6bced5144e54646419aa4716c3ec431c7a58060937cdbd93704f053857b712a9` |
|  `22-dev` `latest-dev` `22.2.0-dev` `22.2-dev` `next-dev` | May 23rd     | `sha256:66466e34a0c1c96f902be852f19d25d76b7e785aeea1bb902a4de457fbdf442e` |
|  `20-dev` `20.13.1-dev` `20.13-dev`                       | May 23rd     | `sha256:7f84712d0115c005d2830c83e72f0761d04fc08c29e724c47065766ce1b987e3` |
|  `next`                                                   | May 23rd     | `sha256:4abf659c07d052ff060c1faca3579c25f893914232f3f9b91f29e530dba973fc` |
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

