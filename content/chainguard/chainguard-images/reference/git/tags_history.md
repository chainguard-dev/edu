---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
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
|  `latest-glibc-dev`      | April 29th   | `sha256:08e9e8e882ccade268bb1868064b134ce8e37ac54976d2f258bb0a54f68333b2` |
|  `latest-glibc-root`     | April 29th   | `sha256:2bf1568e194fa3b2554efac0d0b13f1f88a555017dcd54748088c3f04cdde1f9` |
|  `latest-glibc`          | April 29th   | `sha256:6d0c134c303f85445ad62bd44ac08037ac0fc6008e27a82fc6d4fb66874de096` |
|  `latest-glibc-root-dev` | April 29th   | `sha256:1d353ed4c8f15cd0cf1a823f140de5449abfd4caa18523daf1a4295eb265ee61` |
|  `latest-root`           | April 26th   | `sha256:de87d065b0efb4332080a55ccf45015891fce6aa9ee6101730779850d4634a56` |
|  `latest`                | April 26th   | `sha256:161961e61ad7b216897bfdb236cce1d3129cefe6a0b362c3842d7db03c6dede7` |
|  `latest-dev`            | April 26th   | `sha256:8afe675f248d3b899750be66d3d87a4c6ddb591bcf8075d6a0323641869b7068` |
|  `latest-root-dev`       | April 26th   | `sha256:02e2db606af85e7edede303c069fabd45290c7664682fb5c7a8d4c2e8e19f157` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                   | Last Changed | Digest                                                                    |
|-------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `glibc-root-2-dev` `glibc-root-2.45-dev` `latest-glibc-root-dev` `glibc-root-2.45.0-dev` | May 1st      | `sha256:9fa7fb1aca15dd037f8b776335c3d6557e52924c666c662bf480ab4e9a0420ad` |
|  `latest-glibc-root` `glibc-root-2` `glibc-root-2.45.0` `glibc-root-2.45`                 | May 1st      | `sha256:7010247b057c2ba3e2bef3e38cca980b1d56a34524608b9d8407878fdc191e4d` |
|  `glibc-2` `latest-glibc` `glibc-2.45` `glibc-2.45.0`                                     | May 1st      | `sha256:8b4b10c5812ed89f00394c691ac89fdb38b3fceacdae31f8bc47e6d6b0dc1909` |
|  `glibc-2.45.0-dev` `latest-glibc-dev` `glibc-2-dev` `glibc-2.45-dev`                     | May 1st      | `sha256:365761ddd0246dd9ea8dff03a7803dbcee5b77c199c9edf383c937462df0a3d0` |
|  `glibc-root-2.44-dev` `glibc-root-2.44.0-dev`                                            | April 21st   | `sha256:14b2f555f9357820c258525e78c8a1043e2b3cfeb5cd65c90f5b42c10277bd7b` |
|  `glibc-root-2.44.0` `glibc-root-2.44`                                                    | April 21st   | `sha256:e7d75a590697423d72df8fefb4ce8841e7b38cc89c7804f404dae9b3b7b0b11b` |
|  `glibc-2.44` `glibc-2.44.0`                                                              | April 21st   | `sha256:f7a2aa865cc1d894d1b495aedb4a506c8c3beb6bb2aff6e674b095212b67dfd8` |
|  `glibc-2.44.0-dev` `glibc-2.44-dev`                                                      | April 21st   | `sha256:1e89e0e1d06f58d535ee408a974f11f01233d776fe743188775cd36fb2532d58` |
|  `root-2.40.0`                                                                            | April 27th   | `sha256:9e3145982ed708b7490b05cc89a9f232412718c035f56915e7481fe508533d3e` |
|  `glibc-2.40.0-dev`                                                                       | April 27th   | `sha256:9a4062b9ad586a8aa2903442d792e334ba808cfa230acd6da1cf29fc0264e696` |
|  `glibc-root-2.40.0`                                                                      | April 27th   | `sha256:7be4de5e55c5ebe608183205cd23a9c9cc4df8df4d681971fb5a3c2de73a4f84` |
|  `glibc-2.40.0`                                                                           | April 27th   | `sha256:e1dd4ec03f692da3ae993f57126fdd6cc600daa7af01291369fd3eebc86521f7` |
|  `2.40.0`                                                                                 | April 26th   | `sha256:f5906926d6cf3ca4ed97295570341ce776674716e70b6783c87e59f278bf5cbf` |
|  `2.40.0-dev`                                                                             | April 25th   | `sha256:dff31aeb5de3d3cdb6eba4e071b68dbfb1d8616864add22b616dca7b4a4165bc` |

