---
title: "argocd-repo-server Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the argocd-repo-server Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-24 00:45:45
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/argocd-repo-server/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/argocd-repo-server/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/argocd-repo-server/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/argocd-repo-server/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 23rd     | `sha256:ea55f96fc126afdb6d6f76ec434d8c3c5ad8891f211e954cd546c587c2b28a81` |
|  `latest-dev` | May 23rd     | `sha256:6fa9044544da14ce968929a42e79272318bd4fbb3f5a21b748da544adbcf0bd2` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.8.18` `2.8`                                | May 23rd     | `sha256:d34f9a9ec06c4f091f67d3f501f81f9a159902c012030d559371356d0a141ab0` |
|  `2.10.11` `latest` `2.10` `2`                 | May 23rd     | `sha256:1e0093cc529b8552b83954c8a9d61cee465d5f486f041daaf6309e2f7b064114` |
|  `2.9-dev` `2.9.16-dev`                        | May 23rd     | `sha256:58bdf38d048b387c1c156cb23e3aa24f1be7371e22c9e73440d4a1d33bc4dc7d` |
|  `2.9` `2.9.16`                                | May 23rd     | `sha256:deabfb7b59cc2a247bc14e8255908d28948a9f8767e7bcc6b9c5fb908f547dbd` |
|  `latest-dev` `2.10-dev` `2.10.11-dev` `2-dev` | May 23rd     | `sha256:a5720ac350327d6566500c4b07ae049c661b6a1dd614fa4aefe84782ee3f98da` |
|  `2.8.18-dev` `2.8-dev`                        | May 23rd     | `sha256:bee618b3cff37916b16fad8c6deba8de2e14f1419bdce7f970206d2aee5b7572` |
|  `2.9.15`                                      | May 23rd     | `sha256:7d2100c1b55a7c8f385d7af2e5b834fe8cdbad6dc46b70d330f09702633f5f14` |
|  `2.10.10`                                     | May 23rd     | `sha256:3bf7b70d3a56194c635f3bd04b320be88185ce791c6cc62479d073f911a31b32` |
|  `2.10.10-dev`                                 | May 23rd     | `sha256:f585bd4870956c2cf0b2ecdbcc896e2f8dc004d09a07c827663e6a0816607934` |
|  `2.9.15-dev`                                  | May 23rd     | `sha256:7a7b597cba4545b52a2cac5bcba4602270b3cd3517a46f3d15e32cdf4f265ccc` |
|  `2.10.9-dev`                                  | May 19th     | `sha256:c6f025f525c8bbfd682fa4b4d63ed5decca88e84ccad3a27e1f89d30d31a1883` |
|  `2.9.14-dev`                                  | May 19th     | `sha256:cc38ad8f93838200a259ef01d7bc8b780f7d0eae0f13ce3abc755234c10af23e` |
|  `2.9.14`                                      | May 19th     | `sha256:0d15ec5c95602db0f3afcc2852221368e63a7dfc47f7ae80377045a1479450cb` |
|  `2.10.9`                                      | May 19th     | `sha256:4b8181dbbb35e9469f3c3d0d88489d8dc8dcab531d0b33798a955c04fa2875df` |
|  `2.9.13`                                      | April 30th   | `sha256:34cce72c03dcbaa4a6ec7c3b3f05c3e457e002f3f367cbe9227a7bbae1b530c7` |
|  `2.8.17`                                      | April 30th   | `sha256:de6e82fbcfc6343b9f243fc310ac719336868a51b9cd9b5e6c3f573e9c499f37` |
|  `2.8.17-dev`                                  | April 30th   | `sha256:cb99e1dd885f9ae1325f0dd32bec668468d15a89084b65b4c20393d7c9c357fd` |
|  `2.10.8-dev`                                  | April 30th   | `sha256:9ce6cf1c400bdf47e11055c50a5d57dd5fb46d459f8b974e78a375b149a9466e` |
|  `2.10.8`                                      | April 30th   | `sha256:0d8611cf4161b0e8b85f12f8012758dc064d81b69b97b6cdb738d0ca6f3f5c27` |
|  `2.9.13-dev`                                  | April 30th   | `sha256:88c652251ad2e89ce72d69b66e5b186330d118ab154cbf929b80d062ffa97eb1` |
|  `2.10.7-dev`                                  | April 25th   | `sha256:f0cc0958e7eaa27c2822f29c4058a592a9a61a4699d4ae323a0003e04b90b144` |
|  `2.8.16-dev`                                  | April 25th   | `sha256:94a34185a2948a1508cfa5183c013f96b3045ebecd5b86d0d1c8deef5180b84e` |
|  `2.10.7`                                      | April 25th   | `sha256:862afa2035c638695f7e9300f162cb4901a5d4e6cd5ae8103b06c04b967de11d` |
|  `2.9.12-dev`                                  | April 25th   | `sha256:517829d535cd6241f9699523d226baad72face683083114534d655ab0eda7ea6` |
|  `2.9.12`                                      | April 25th   | `sha256:e834ed898014955f36625ba44e3e31d3e019597cf753ab700d145f46fb993fa6` |
|  `2.8.16`                                      | April 25th   | `sha256:96005211201a4b4c2ff192bfb3e8c5c9573e2383a1f3fb1d9074e0d052ce6faf` |

