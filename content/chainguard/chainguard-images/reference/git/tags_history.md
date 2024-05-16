---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/git/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/git/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/git/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/git/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                  | Last Changed | Digest                                                                    |
|--------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev`            | May 15th     | `sha256:d0679f95556e3d192661681cfb4ca258051dc6294fb493ed98f975dd50b3eeac` |
|  `latest-root-dev`       | May 15th     | `sha256:5e30d33bfd8723f208f83dc81c8f91deb7a0867b1f8774bfd66e5accc285d090` |
|  `latest-root`           | May 15th     | `sha256:1fb61a8f19d2b898f1f67d2ae2dffd4070c2f2c9bca65e6192e56b324824736d` |
|  `latest`                | May 15th     | `sha256:c4ca049994b70fe13a1370638aa7aa26004d62b866f9c1b7d84df2c6e27ba54b` |
|  `latest-glibc-root-dev` | May 15th     | `sha256:04a89d06f9293aac2c0506378336bcb67efb1b5f89a9f3691e75a5b5d03cb51e` |
|  `latest-glibc-root`     | May 15th     | `sha256:ca835d79a08bdda42811666f2ee2b193149cdfb33a95d9b9d0c7f84caeeb2b6b` |
|  `latest-glibc`          | May 15th     | `sha256:2d1b347160287b790cef906b2872bf521ceb66602c88c17df734f212a6fd7421` |
|  `latest-glibc-dev`      | May 15th     | `sha256:4b6782aaea79bd137876eec2ac2dd54632310ba32e6cb48fda8b3a12d23b6238` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                                                                                    | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.45-dev` `2-dev` `2.45.1-dev` `latest-dev` `glibc-2.45-dev` `latest-glibc-dev` `glibc-2.45.1-dev` `glibc-2-dev`                                         | May 15th     | `sha256:43a90d70e14529c1216e86d44ea89a2da000ef1ef53fc6ab9b13d1d4885b6dca` |
|  `root-2.45.1` `glibc-root-2.45.1` `glibc-root-2.45` `root-2` `root-2.45` `latest-root` `glibc-root-2` `latest-glibc-root`                                 | May 15th     | `sha256:96190f35175521d6363fcfef0af1aa5093a7ecbccea0be9a8b52a8d9debf8a4a` |
|  `glibc-root-2.45-dev` `root-2-dev` `glibc-root-2.45.1-dev` `latest-glibc-root-dev` `latest-root-dev` `root-2.45-dev` `root-2.45.1-dev` `glibc-root-2-dev` | May 15th     | `sha256:7b6a052860dc605fc4a9490747813b0c19cf1faf518552faf4284cac83f05577` |
|  `latest-glibc` `glibc-2.45` `2.45` `glibc-2` `latest` `2` `glibc-2.45.1` `2.45.1`                                                                         | May 15th     | `sha256:17551ee71b406dd8322b489c40c9cdbd9fb4f3adec6d5967e81ea880e64eb46b` |
|  `2.45.0-dev` `glibc-2.45.0-dev`                                                                                                                           | May 14th     | `sha256:042068e25cbad28a8e3b127e8db212d9c4fa1aa5cc84751c262b3c83006cd1b2` |
|  `glibc-root-2.45.0` `root-2.45.0`                                                                                                                         | May 14th     | `sha256:f2ff396551bfe42e62401b04a65df65bf43f04d3aff283d0c42454d97d70d7d8` |
|  `2.45.0` `glibc-2.45.0`                                                                                                                                   | May 14th     | `sha256:827fbc62d3e475394599edbf9095a353b4ec964a64797b62b143ef100a464027` |
|  `glibc-root-2.45.0-dev` `root-2.45.0-dev`                                                                                                                 | May 14th     | `sha256:48efe16835214c405ce9131641af0e51f342d50b5e98f05dff415afb65ceb469` |
|  `glibc-root-2.44-dev` `glibc-root-2.44.0-dev`                                                                                                             | April 21st   | `sha256:14b2f555f9357820c258525e78c8a1043e2b3cfeb5cd65c90f5b42c10277bd7b` |
|  `glibc-root-2.44.0` `glibc-root-2.44`                                                                                                                     | April 21st   | `sha256:e7d75a590697423d72df8fefb4ce8841e7b38cc89c7804f404dae9b3b7b0b11b` |
|  `glibc-2.44` `glibc-2.44.0`                                                                                                                               | April 21st   | `sha256:f7a2aa865cc1d894d1b495aedb4a506c8c3beb6bb2aff6e674b095212b67dfd8` |
|  `glibc-2.44.0-dev` `glibc-2.44-dev`                                                                                                                       | April 21st   | `sha256:1e89e0e1d06f58d535ee408a974f11f01233d776fe743188775cd36fb2532d58` |
|  `root-2.40.0`                                                                                                                                             | April 27th   | `sha256:9e3145982ed708b7490b05cc89a9f232412718c035f56915e7481fe508533d3e` |
|  `glibc-2.40.0-dev`                                                                                                                                        | April 27th   | `sha256:9a4062b9ad586a8aa2903442d792e334ba808cfa230acd6da1cf29fc0264e696` |
|  `glibc-root-2.40.0`                                                                                                                                       | April 27th   | `sha256:7be4de5e55c5ebe608183205cd23a9c9cc4df8df4d681971fb5a3c2de73a4f84` |
|  `glibc-2.40.0`                                                                                                                                            | April 27th   | `sha256:e1dd4ec03f692da3ae993f57126fdd6cc600daa7af01291369fd3eebc86521f7` |
|  `2.40.0`                                                                                                                                                  | April 26th   | `sha256:f5906926d6cf3ca4ed97295570341ce776674716e70b6783c87e59f278bf5cbf` |
|  `2.40.0-dev`                                                                                                                                              | April 25th   | `sha256:dff31aeb5de3d3cdb6eba4e071b68dbfb1d8616864add22b616dca7b4a4165bc` |

