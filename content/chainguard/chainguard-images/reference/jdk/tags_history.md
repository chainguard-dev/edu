---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-27 00:41:27
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jdk/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jdk/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jdk/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jdk/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 26th    | `sha256:652ef2179f972ff67f6684e5fcc818dfc9b19b3c6e7f2fa15ec22069c79da519` |
|  `latest`     | June 26th    | `sha256:caa10461ebd27fdbdcd3ec71e926fe57fa10c76237b17afb6933a7f2a3f7522c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-15.0.10` `openjdk-15` `openjdk-15.0` `openjdk-15.0.10.5`                 | June 26th    | `sha256:433dc6264de0fd48bc73a0d93d98bfa2370ee59465deb5261c300de47b026ec3` |
|  `openjdk-8-dev` `openjdk-8.412-dev` `openjdk-8.412.08-dev`                        | June 26th    | `sha256:121671d8bd053f1a3210912102ecbc4a642b0583eeda3d0b610f3ed94201751f` |
|  `openjdk-22-dev` `openjdk-22.0.1-dev` `latest-dev` `openjdk-22.0-dev`             | June 26th    | `sha256:2e23794daadf58458797a5a895e9e9e0e5c6f909d9b9f61c881b223f035cdfd0` |
|  `openjdk-17.0.11-dev` `openjdk-17.0-dev` `openjdk-17-dev`                         | June 26th    | `sha256:7a76f20f0bd9cf8b0163dbfbad612ab056cebaaf24f81fd9a87f959c0ecbcf46` |
|  `openjdk-16-dev` `openjdk-16.0.2-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0-dev`   | June 26th    | `sha256:9aaa4cb4323e33e5e26a145ed86883091fbd98452a052ce9de979b8a772f06f2` |
|  `openjdk-16.0.2` `openjdk-16` `openjdk-16.0` `openjdk-16.0.2.7`                   | June 26th    | `sha256:0e14934ceddfb32d01e5aa2c31f28f5a238d53b69287edd2656aa8b40940766b` |
|  `openjdk-17.0.11` `openjdk-17.0` `openjdk-17`                                     | June 26th    | `sha256:e693a19831c47ffb6f898ba3d266462eb8bc0d5179efb11d7d52bb41f5bf0413` |
|  `openjdk-11-dev` `openjdk-11.0.23-dev` `openjdk-11.0-dev`                         | June 26th    | `sha256:47f2241cfb5b1cf00eb0d6da2107668a83872f74a481e8efe6658966dde7740b` |
|  `openjdk-21` `openjdk-21.0` `openjdk-21.0.3`                                      | June 26th    | `sha256:d5b2772cd143886f735ef53217a455222c5d80764c784a735255990e179150cf` |
|  `openjdk-15.0.10-dev` `openjdk-15.0-dev` `openjdk-15-dev` `openjdk-15.0.10.5-dev` | June 26th    | `sha256:76b9ffc4228da6410ddc263c5bf3127fbb4232ac30229a5183d192281ddd0a30` |
|  `openjdk-11.0.23` `openjdk-11.0` `openjdk-11`                                     | June 26th    | `sha256:44ee58ea754c0f3d21e93a91e0e0ed7d08f29d47fc43f71770df5be3fff53e8f` |
|  `openjdk-22` `latest` `openjdk-22.0` `openjdk-22.0.1`                             | June 26th    | `sha256:0ff8d946ce1f4b64afa7eb0e3fd02304e4b030fbcce7135d16e09e2941388c32` |
|  `openjdk-14.0.2` `openjdk-14.0` `openjdk-14` `openjdk-14.0.2.12`                  | June 26th    | `sha256:4fe22afb9c376126fdf5c897049656728d785d906c815192ba2abb3f3b158cb3` |
|  `openjdk-8` `openjdk-8.412.08` `openjdk-8.412`                                    | June 26th    | `sha256:093d83a278d4ad3a7833ba6eb20e16fb9fd0e8fd614ab001bfae559db3f0354c` |
|  `openjdk-21-dev` `openjdk-21.0-dev` `openjdk-21.0.3-dev`                          | June 26th    | `sha256:491bab13c62abe5d49e48ddc09f98b88fe4d1ad9951573c04b1035344ff375f3` |
|  `openjdk-14-dev` `openjdk-14.0-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0.2-dev`  | June 26th    | `sha256:61c5b008b9450fd9894b3474cc92cae77d81b29c3573d0adb77c66f17d4c87d0` |

