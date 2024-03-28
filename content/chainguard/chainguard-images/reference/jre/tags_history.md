---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-28 00:50:32
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
|  `latest-dev` | March 21st   | `sha256:c6473e75a93568737ff2dc33aeb7b08ef81062ca5c53c233304c7f52e050f0e5` |
|  `latest`     | March 21st   | `sha256:f1173962af753018ad8679c9610462a3914143c7c2589411bc2f1309e29c35df` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-15.0.10` `openjdk-15.0` `openjdk-15` `openjdk-15.0.10.5`                 | March 27th   | `sha256:634169021d52e2f75facf2b9f7979ae75735a5f2497463137a14d2b3713e61ed` |
|  `openjdk-17` `openjdk-17.0.10` `openjdk-17.0`                                     | March 27th   | `sha256:06585c883bd9755353fe80f54bc3fa57190f19775e6d0beb089350cee1fa40d7` |
|  `openjdk-16.0.2` `openjdk-16.0.2.7` `openjdk-16` `openjdk-16.0`                   | March 27th   | `sha256:8e42b3224cd0dba6e908e7107d401dfb6ff6d8dff492f293f8d6ab8fe82f2a7c` |
|  `openjdk-14.0.2` `openjdk-14` `openjdk-14.0` `openjdk-14.0.2.12`                  | March 27th   | `sha256:43d3bc2f54f6ba8069bb0e91f7b01c1fd822848555e39f40b9b6d35ec9d5bca6` |
|  `openjdk-21.0.2-dev` `openjdk-21.0-dev` `openjdk-21-dev`                          | March 27th   | `sha256:fb7ab3f3c84185aebc3c37f2e23dd922e3463abf6e8370c19973646d820a6504` |
|  `openjdk-16.0-dev` `openjdk-16-dev` `openjdk-16.0.2-dev` `openjdk-16.0.2.7-dev`   | March 27th   | `sha256:289b234a9f58f4e12f07afe182fcfa3aa61397c4b77b02524ea2c704921376ab` |
|  `openjdk-8.392` `openjdk-8.392.08` `openjdk-8`                                    | March 27th   | `sha256:c1c9c830b54b812d06977d6a8a46df68af52d5b4f084cff68bd08272622da20a` |
|  `openjdk-17.0-dev` `openjdk-17-dev` `openjdk-17.0.10-dev`                         | March 27th   | `sha256:00a6df5e11187e3e63f11e1a0e03e48e64a1780e6f74ae27a79177b3ab2cabe9` |
|  `openjdk-22.0` `latest` `openjdk-22.0.0` `openjdk-22`                             | March 27th   | `sha256:ae897688e648a9a024fa80c0805d4d3a77ddfe001db5f8a0e004830b117752a7` |
|  `openjdk-21` `openjdk-21.0` `openjdk-21.0.2`                                      | March 27th   | `sha256:8fadaeb31baf9e7fb921f4c1915199338d119e1c6b266d758c784fe843b8f983` |
|  `openjdk-15.0-dev` `openjdk-15-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0.10-dev` | March 27th   | `sha256:426c3a00b913e7747cc23910aa4835b9d5994d1b082f27681e66bee2f06d3e9a` |
|  `openjdk-11.0` `openjdk-11` `openjdk-11.0.22`                                     | March 27th   | `sha256:8d21b6439ca1c09212e4e0a196208175e1db73b7f376ab1654269749320ea388` |
|  `openjdk-8-dev` `openjdk-8.392-dev` `openjdk-8.392.08-dev`                        | March 27th   | `sha256:0cff9521d5ae5775393539a2c893db93cde64438152e6f1114710c4d485c6f8b` |
|  `openjdk-14-dev` `openjdk-14.0.2-dev` `openjdk-14.0-dev` `openjdk-14.0.2.12-dev`  | March 27th   | `sha256:f822fc42c735a505013d6660305da20630c191ad9378f47b1792b8c3592add6d` |
|  `openjdk-22-dev` `openjdk-22.0-dev` `latest-dev` `openjdk-22.0.0-dev`             | March 27th   | `sha256:98b931fe271cc8501a42952b7db5ba1c64b7c459af239b621052863b21c6222d` |
|  `openjdk-11.0-dev` `openjdk-11-dev` `openjdk-11.0.22-dev`                         | March 27th   | `sha256:444124544f9be4647094f930a8941f26a2c4d83cc688fb3346258e22ce1277ee` |

