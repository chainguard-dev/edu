---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-23 00:43:06
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jre/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jre/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jre/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jre/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 22nd    | `sha256:5ca24d52e91e554dc58f26d8ebb67a9d69903f0d7387ca3cebd42a6faf10a356` |
|  `latest`     | June 22nd    | `sha256:7080fe8053b866845687f0b85652be6a4563d9bad26dcf0e479d7a4e5ce0dd03` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-22` `openjdk-22.0.1` `latest` `openjdk-22.0`                             | June 21st    | `sha256:3339714e3d466d1723df86401f4247558094abe85381c779f1d63c4e25b74ef9` |
|  `openjdk-14.0` `openjdk-14.0.2.12` `openjdk-14` `openjdk-14.0.2`                  | June 21st    | `sha256:82b80dcfc13d06d1993e65b5a70607a36cba6a89c81b72125527e75ed2908ba2` |
|  `openjdk-17.0.11-dev` `openjdk-17.0-dev` `openjdk-17-dev`                         | June 21st    | `sha256:3f0e948804b1419389dcd36cb9e401fa222360999a402686a036c824a17f2906` |
|  `openjdk-21-dev` `openjdk-21.0-dev` `openjdk-21.0.3-dev`                          | June 21st    | `sha256:5f8c1b8e2b91c7d45cb159c73c3c44fa38edd4288e9acde905d4bbd1829fd077` |
|  `openjdk-15.0.10.5` `openjdk-15.0` `openjdk-15` `openjdk-15.0.10`                 | June 21st    | `sha256:42c8eb7e2af013209a60a7790a9f0172ac9b5c840eebfc43f7dcadda6efa9f53` |
|  `openjdk-14.0.2-dev` `openjdk-14.0-dev` `openjdk-14-dev` `openjdk-14.0.2.12-dev`  | June 21st    | `sha256:fb401105bb371a5e67c4fe870d581a91fc1fbb776b3a42d8e39408e6b3c1e57b` |
|  `openjdk-8-dev` `openjdk-8.412.08-dev` `openjdk-8.412-dev`                        | June 21st    | `sha256:67665a750a7d9a79514b15cd233801e5512bad5f7f2d643fb75eb75e719cb4d0` |
|  `openjdk-8.412` `openjdk-8.412.08` `openjdk-8`                                    | June 21st    | `sha256:9ac48baad0cb2215f482893b49e4ad2aae6e24d1fe6e8f1b6cd934bef11b8bb5` |
|  `openjdk-22.0-dev` `openjdk-22-dev` `openjdk-22.0.1-dev` `latest-dev`             | June 21st    | `sha256:ca010a8359165c1a59c3a3681db67f83586d5db44dc588745cb8620cdb762efd` |
|  `openjdk-11.0.23-dev` `openjdk-11-dev` `openjdk-11.0-dev`                         | June 21st    | `sha256:e9189fd9677160e851145a6c545cea26fc6115a52ac49563f67bbb5a0db61f33` |
|  `openjdk-16.0.2.7-dev` `openjdk-16-dev` `openjdk-16.0.2-dev` `openjdk-16.0-dev`   | June 21st    | `sha256:b27ce9c9eefedb23cf28d59c905844d4921586f46daa21a7cdff8a60fe9ec2fa` |
|  `openjdk-17.0.11` `openjdk-17` `openjdk-17.0`                                     | June 21st    | `sha256:7512f448eeac1db9b60bafa33b34723ba2f0dfc2057fd884a1de238f43147875` |
|  `openjdk-21.0.3` `openjdk-21.0` `openjdk-21`                                      | June 21st    | `sha256:d91cf0700834c64b258f6b4f38cd806b77b5e2c4aa9bea0092a8c604f22194e8` |
|  `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16` `openjdk-16.0`                   | June 21st    | `sha256:ce37fa61a748b8e3eabf9573c5f4fffd18d0e9eb42a215be896aa0d516eb2c3c` |
|  `openjdk-11` `openjdk-11.0` `openjdk-11.0.23`                                     | June 21st    | `sha256:15cc64da72bd170da9338e3c33d16f40d1e7e4be6cc9149222afd4e672e1cadb` |
|  `openjdk-15-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0-dev` `openjdk-15.0.10-dev` | June 21st    | `sha256:8f24f50ed556d72eb93bca3180b07cd05256524d75c0e32fd6434d9ac2482577` |

