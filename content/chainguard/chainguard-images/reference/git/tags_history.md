---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-22 00:47:17
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
|  `latest-glibc-root`     | May 21st     | `sha256:a576d5d9ef448a96b198f6e2f73ba0fefd04fffac5f3bc9b0b6bebd685cb5cfc` |
|  `latest-glibc-dev`      | May 21st     | `sha256:51dd5f679f4681c2156daec17fd64dd703db07a2be607c82a17a46d640c02383` |
|  `latest-glibc`          | May 21st     | `sha256:c1fd90fb33706ee80546efe4e28f54c515a4046fbfd73dacda9119d1f3fec20d` |
|  `latest-glibc-root-dev` | May 21st     | `sha256:f3ff42b2f0a130c4401e3ceefea9746c7a01d52dfb8ef68000169a49d40f6030` |
|  `latest-root`           | May 21st     | `sha256:e9beef92934de5a5d29ff76284b7088556e11f0f1f5e464473c1ad654e4659a8` |
|  `latest-dev`            | May 21st     | `sha256:cc0ab39002193fb1319a7e3dbb2915edafd91dd1e4b6fea6325420d307046475` |
|  `latest`                | May 21st     | `sha256:159ec36df44225607cb09a4087554182eead5505723661f1ef9cad48c8d453b5` |
|  `latest-root-dev`       | May 21st     | `sha256:eb51117ee7e6e9a964a9414694e380cbdd9d6e4fbfd1b0cdbb855e4c507402ef` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                                                                                    | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `glibc-root-2-dev` `latest-root-dev` `glibc-root-2.45-dev` `root-2.45-dev` `glibc-root-2.45.1-dev` `root-2-dev` `latest-glibc-root-dev` `root-2.45.1-dev` | May 21st     | `sha256:d65e683ee599074b6cdd2aec553169a3d1b0cc3b98f11e133c488327612d019f` |
|  `2.45-dev` `glibc-2.45-dev` `glibc-2-dev` `2.45.1-dev` `latest-glibc-dev` `2-dev` `latest-dev` `glibc-2.45.1-dev`                                         | May 21st     | `sha256:ef00b7d1ad34041af5fcbd9fc372a0e3c4e56f143593c3fa35fdd28f0ce7bdfa` |
|  `root-2` `glibc-root-2` `glibc-root-2.45.1` `root-2.45` `glibc-root-2.45` `latest-root` `latest-glibc-root` `root-2.45.1`                                 | May 21st     | `sha256:0f4fe55826604d2c01cbde8b59dc1c165c1c9000b37d57ccd69c55dcd196c44f` |
|  `glibc-2.45.1` `latest` `2` `2.45` `2.45.1` `glibc-2` `latest-glibc` `glibc-2.45`                                                                         | May 21st     | `sha256:28487200ee92a2993ed9175f9ecedb2a328eb7b08443909b08e412ef194a5f5b` |
|  `2.45.0-dev` `glibc-2.45.0-dev`                                                                                                                           | May 14th     | `sha256:042068e25cbad28a8e3b127e8db212d9c4fa1aa5cc84751c262b3c83006cd1b2` |
|  `glibc-root-2.45.0` `root-2.45.0`                                                                                                                         | May 14th     | `sha256:f2ff396551bfe42e62401b04a65df65bf43f04d3aff283d0c42454d97d70d7d8` |
|  `2.45.0` `glibc-2.45.0`                                                                                                                                   | May 14th     | `sha256:827fbc62d3e475394599edbf9095a353b4ec964a64797b62b143ef100a464027` |
|  `glibc-root-2.45.0-dev` `root-2.45.0-dev`                                                                                                                 | May 14th     | `sha256:48efe16835214c405ce9131641af0e51f342d50b5e98f05dff415afb65ceb469` |
|  `root-2.40.0`                                                                                                                                             | April 27th   | `sha256:9e3145982ed708b7490b05cc89a9f232412718c035f56915e7481fe508533d3e` |
|  `glibc-2.40.0-dev`                                                                                                                                        | April 27th   | `sha256:9a4062b9ad586a8aa2903442d792e334ba808cfa230acd6da1cf29fc0264e696` |
|  `glibc-root-2.40.0`                                                                                                                                       | April 27th   | `sha256:7be4de5e55c5ebe608183205cd23a9c9cc4df8df4d681971fb5a3c2de73a4f84` |
|  `glibc-2.40.0`                                                                                                                                            | April 27th   | `sha256:e1dd4ec03f692da3ae993f57126fdd6cc600daa7af01291369fd3eebc86521f7` |
|  `2.40.0`                                                                                                                                                  | April 26th   | `sha256:f5906926d6cf3ca4ed97295570341ce776674716e70b6783c87e59f278bf5cbf` |
|  `2.40.0-dev`                                                                                                                                              | April 25th   | `sha256:dff31aeb5de3d3cdb6eba4e071b68dbfb1d8616864add22b616dca7b4a4165bc` |

