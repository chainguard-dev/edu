---
title: "aws-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the aws-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-16 00:33:13
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/aws-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/aws-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/aws-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/aws-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | March 15th   | `sha256:e4752d5370770bcd056c05bb3b6afa5c71a2143e5bc656d753f1f281847e1883` |
|  `latest-dev` | March 15th   | `sha256:1e09db0828d155800fd9a020d9d73296a386499d7f3ce8f62fd64ac99a4d397a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed  | Digest                                                                    |
|------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` `1-dev` `1.32-dev` `1.32.64-dev` | March 15th    | `sha256:27c94bbd815fa42a3d0656990e4f5b53d20b93e5fb1d449713a8e78933786601` |
|  `1.32` `1` `1.32.64` `latest`                 | March 15th    | `sha256:fba3f1e6ffe0b56e07bb145817f8044a4c532d4b2e0555a5281aacf996609921` |
|  `1.32.63-dev`                                 | March 15th    | `sha256:4428dfffea198ec40f6227d49b9c41b6a3ee2f6809e755ede645b87cad273fd5` |
|  `1.32.63`                                     | March 15th    | `sha256:d3d3542cb8336de8f4eb139d8395e03ccc6529cec7ce149df9e50179ebad7252` |
|  `1.32.62`                                     | March 14th    | `sha256:efee88d75e0fea6d5cf19cd369f215ae0eea76716f6c695d79a9935fbe8f8f3b` |
|  `1.32.62-dev`                                 | March 14th    | `sha256:9228be421a1c8fef34fc6c261e278ba79a6ef8d924c8d4d7fb2ee388c7e16b6d` |
|  `1.32.61-dev`                                 | March 13th    | `sha256:772375d497654616010899d050a17a2b3fc3547cca357e960872d8d361c6972b` |
|  `1.32.61`                                     | March 13th    | `sha256:a922016d50c828c36d02ab463514aa58a7021bf7a1e3063e0edafccbf0be2bb3` |
|  `1.32.60`                                     | March 12th    | `sha256:5e72bcb1bb5095d4834ff886f56ded9e2122a2ebc52b1e3c5b84fdc9c47510ac` |
|  `1.32.60-dev`                                 | March 12th    | `sha256:0b0a785ccb4e685c8eb26699ae0f88b6994c1b218946abd3af174081b091cd86` |
|  `1.32.59-dev`                                 | March 10th    | `sha256:142ba6072ef527e534d4e818c1f60c3265f8bf6d075b62996838cce434ad467d` |
|  `1.32.59`                                     | March 9th     | `sha256:0bedc05f05e18d3ed50486b7b7f7b9bb707f11f05280f56c8e61db50c29b3603` |
|  `1.32.58-dev`                                 | March 8th     | `sha256:03fee32e55c7d7983ff2162781180450518d792f27c5de57f868390bd597712c` |
|  `1.32.58`                                     | March 8th     | `sha256:2c747c77f9cb07c1307c70d53cf631a92edb33a8cda57739d01d0648a9a297e5` |
|  `1.32.57-dev`                                 | March 8th     | `sha256:0b5f6b0069349aa01a61ef4a72ad9446d94d9a9aae48635875035f6de0003f8b` |
|  `1.32.57`                                     | March 8th     | `sha256:a7db3d221f503cc5bb19af439586a014b726d89248d6224d0746b1f005227857` |
|  `1.32.56`                                     | March 6th     | `sha256:547889458b6af4f388f1e3eabc0d89d0ea2797af738572aefa1bd9c2c00b91bb` |
|  `1.32.56-dev`                                 | March 6th     | `sha256:0e28e5201fed77dc2ea9beea10797b9ca3a00a42f1c070108a7a75989c9d9169` |
|  `1.32.55-dev`                                 | March 5th     | `sha256:03ffca3144cb6ca3d03a14b36e8c47a553a358e327c0006a2531028eab915b5c` |
|  `1.32.55`                                     | March 5th     | `sha256:481d87a9ced69664264d72ae7dd151336be373d4c41f3469d1d27d890a905b5b` |
|  `1.32.54-dev`                                 | March 2nd     | `sha256:d0d002e1ca22bfd657ebf3c7490b49b956fe394fc362ae057749e06344ee3bc7` |
|  `1.32.54`                                     | March 2nd     | `sha256:9ef125a6250ea13ae9eca8febd673512ed07b2351fd9bd060ac21cd890e39918` |
|  `1.32.53-dev`                                 | March 1st     | `sha256:69f5002eb6afea48cf97fd7d789a8042b1d292f720493c38428927ec9d440142` |
|  `1.32.53`                                     | March 1st     | `sha256:63db4429fd51bbeb80f3fc59aea07b9b339324353aa4b4e6b7606a7f74ebe4f3` |
|  `1.32.52-dev`                                 | February 29th | `sha256:c00008eab2c0ef06ae26196be0026ce1b21ae7a941204c05e9407de25405ba3d` |
|  `1.32.52`                                     | February 29th | `sha256:319fdb6fab6d660fc7987f2c9f9c8c51bd39674d21d2ad6cf999d05b50bb6216` |
|  `1.32.51`                                     | February 28th | `sha256:099afe2d62af159ee9d0913d60ec46187419b08c48fe88fc484242b24e57c722` |
|  `1.32.51-dev`                                 | February 28th | `sha256:cd6e620cdde8c0157bd048b9822fbdd07067e7c56be1ab21b45fa7cf1149a83e` |
|  `1.32.50-dev`                                 | February 26th | `sha256:7136abcd2d8f3547dcefd753a72e10d5905a00a4bf151e9fc35dd676f1fa070c` |
|  `1.32.50`                                     | February 26th | `sha256:13c2035501101263c17b5803554029a63286b1cf32e5874f2753daa52ff221af` |
|  `1.32.49-dev`                                 | February 24th | `sha256:dd2009a9a0e97278d98da6b42efb635d830e6317baba9c7c9152ff839019e30d` |
|  `1.32.49`                                     | February 24th | `sha256:190dc2d618fee7175f442952147957d14d79def193cbfae2fedc9f74bbe42d1c` |
|  `1.32.48-dev`                                 | February 23rd | `sha256:0c866d009f08852baea892203369facac228fc7c019e42dd43fbcfbeb3887280` |
|  `1.32.48`                                     | February 23rd | `sha256:2b59fdfdb94d95d21a36866ec97a3b53228a207f6f97c7c2a3fb231b9785a276` |
|  `1.32.47-dev`                                 | February 22nd | `sha256:30b0da723de0ab016239f3fef636266b92d470e30b4d3f1b5dab6f378fd429ab` |
|  `1.32.47`                                     | February 22nd | `sha256:e947e41500674fed67d88a1977eb1ab2f4255f68748d075cc6cbdcccfe8c6221` |
|  `1.32.46`                                     | February 20th | `sha256:92eb738df8bb4a4b939e9376c9c1fa6a3e26a948d0aed06924610fc37bbac71f` |
|  `1.32.46-dev`                                 | February 20th | `sha256:f93f2104695379c1d2beaa13b96a493634b51af07025ef95d700c4935cfc5172` |
|  `1.32.45-dev`                                 | February 20th | `sha256:2ba0cde01ae73d13ebe38438df37d1a265adb60ef8306ce12c9e30a2fb74ddea` |
|  `1.32.45`                                     | February 20th | `sha256:f1fafb75b67edc1b27382304d866656a005ad020d56e9e33b57b8ae73eb9000a` |
|  `1.32.44-dev`                                 | February 19th | `sha256:f85e2914913e1c36d54355f62b78facd0b866da46f85c619ae3b55ff0b61ac19` |
|  `1.32.44`                                     | February 19th | `sha256:7cbd87ada56f412b341ad688a93529d26c9a322d4ab2fde3c983b8e3ab0550ff` |
|  `1.32.43`                                     | February 16th | `sha256:3fa4c2c80b5249ad2677d901280cfef2259042d5a11d2a925e80416dccb3ab27` |
|  `1.32.43-dev`                                 | February 16th | `sha256:12f326b78f9c63d637bb001b13bc077d2bded67b2d356c8919e9b0bf6a7b6fa1` |

