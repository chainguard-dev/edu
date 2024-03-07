---
title: "aws-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the aws-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-07 00:51:54
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
|  `latest`     | March 6th    | `sha256:8084f07a7f9fcd54ca284e3c42196ac0fe05047f73ded4376175136db8cab021` |
|  `latest-dev` | March 6th    | `sha256:34718c49c582ed318daa298a0a9589e537ffd046f5ba1e4cb20b1d7cb4ba1cc3` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed  | Digest                                                                    |
|------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `1` `1.32` `1.32.57` `latest`                 | March 6th     | `sha256:9939c759c8acb70474b8355adc84d7f6334d624b5822be81b33997c2deb341b0` |
|  `1-dev` `1.32.57-dev` `latest-dev` `1.32-dev` | March 6th     | `sha256:d4c733dac435b5a9ab622e6c24b2918271d5a21b402ddfb6f5a2dda3a2314991` |
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
|  `1.32.42-dev`                                 | February 15th | `sha256:d8d0ffd82b6170afc3654b1a9719b98621a672b49b9a079313700f4cc143839d` |
|  `1.32.42`                                     | February 15th | `sha256:8551c14dedca51239eb24d698f7fe4d17c3e77fd8625dbf4e4833fc05ddc1f59` |
|  `1.32.41`                                     | February 14th | `sha256:802585e29012712eb685fdcbb522a8768b3f2770960835c604c51c7f30aedfd6` |
|  `1.32.41-dev`                                 | February 14th | `sha256:0420add666ab295f37eb2077699c105553fab6f4f9c25732b88b44c4369229dd` |
|  `1.32.40-dev`                                 | February 13th | `sha256:faac304df7344a5f09f7706886cc648e25ea18cabcefd07db58582c1eb3f3824` |
|  `1.32.40`                                     | February 13th | `sha256:e57af9428c7f1f0efbaeff337c70c2dbae7e6b7447f8243289a77684c87d55c0` |
|  `1.32.39-dev`                                 | February 12th | `sha256:b97629fff3e4303ed355db9eeaba76b43819a888b63eb4563e1656ef52119f48` |
|  `1.32.39`                                     | February 12th | `sha256:f132fe2fdf22b1b641b55bda398e4291839032760480c48d50cba12b53182a63` |
|  `1.32.38-dev`                                 | February 8th  | `sha256:eb34eccd706be2e2cac726c65c755d0bc0f1c05bc8c3729d348046ceba0260a7` |
|  `1.32.38`                                     | February 8th  | `sha256:78fac273f590f5683013dfc6844ee89f8fff004f72c5c81cbfbb1bb9d9425352` |
|  `1.32.37-dev`                                 | February 8th  | `sha256:35cb6d99ef07b4c9e7280beb6c10dabae34c4fe98ac834d7084a3517c452857b` |
|  `1.32.37`                                     | February 7th  | `sha256:9e85f16d0c3d23a667bd3cb53295cde7f95865015bcd48985d9c2e5c3e01ea6b` |
|  `1.32.36-dev`                                 | February 7th  | `sha256:58d0370eaeb8ce5f8e5e68862f2863122f1b8966fa1e04a599e4b588879d2779` |
|  `1.32.36`                                     | February 7th  | `sha256:c11fa18c740ec69b22df8315aff53ac2c2a5a75df746f5009d4d4a5f01ac54d4` |

