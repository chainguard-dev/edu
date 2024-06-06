---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-06 00:48:16
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
|  `latest-glibc-root`     | June 5th     | `sha256:76602dcf3b1ccd18b84daa7de94cfb78225d3a731f7fa21df314ab06770fc62a` |
|  `latest-glibc-root-dev` | June 5th     | `sha256:c2512b90d829c9902f1d9a0bbcd8d08b7857d13ffcf04e1852579dc6c83afcdb` |
|  `latest-glibc-dev`      | June 5th     | `sha256:e3ffb8ddfa4c0e77084502839d8effd3a8945717e570777ee2b2edf6ed16788d` |
|  `latest-glibc`          | June 5th     | `sha256:f47585c02270b5c600d6b7a8696818ccaad0eb0135ac558c2e5b39353b66b7e9` |
|  `latest`                | June 2nd     | `sha256:ec71921b0356838c6a720d1cc15472e160a6fa7e3cf1ef776154e70892c2b090` |
|  `latest-root-dev`       | June 2nd     | `sha256:28feaef348531865019ff676e4ea38d8491d1336b552f2bd48225ff5059be233` |
|  `latest-dev`            | June 2nd     | `sha256:eac2eb6821780fc2139ecc747424bc14f9301b1d37ca86f9bc70603de8cfbf4d` |
|  `latest-root`           | June 2nd     | `sha256:41d3f1d4b0662b147ec6b956aa4678b9a0af91e2b7768c23ae7c1ce2f5afb772` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                                                                                    | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2` `glibc-2.45` `latest` `latest-glibc` `2.45.2` `2.45` `glibc-2.45.2` `glibc-2`                                                                         | June 5th     | `sha256:5a5c10f7896d6f228698bf007faceec1cc2e1a3a9a07413318d5b5443db68735` |
|  `latest-glibc-dev` `glibc-2.45-dev` `2.45.2-dev` `2-dev` `2.45-dev` `glibc-2.45.2-dev` `latest-dev` `glibc-2-dev`                                         | June 5th     | `sha256:cf80e339edbbf2988a06090e5ebd35e949f4101db526749e5c1a491acf732b13` |
|  `latest-glibc-root` `glibc-root-2` `latest-root` `root-2.45` `root-2.45.2` `glibc-root-2.45` `root-2` `glibc-root-2.45.2`                                 | June 5th     | `sha256:6e20f69b45128e6cd61129d3641a2631c85046297b5a6606391dd782d5d267a8` |
|  `glibc-root-2.45.2-dev` `latest-root-dev` `glibc-root-2-dev` `root-2.45-dev` `root-2-dev` `latest-glibc-root-dev` `glibc-root-2.45-dev` `root-2.45.2-dev` | June 5th     | `sha256:1f59b6afe2d9804260f09992fa3273b26f5e5006abfb64e2202eb7511f7441a3` |
|  `root-2.45.1` `glibc-root-2.45.1`                                                                                                                         | May 30th     | `sha256:61d8b2544f0ed4b455debf2300c7a20257a5eee1fdcd621208665b4f870a292f` |
|  `root-2.45.1-dev` `glibc-root-2.45.1-dev`                                                                                                                 | May 30th     | `sha256:b6ae07c98340f572688b8678fc81318c8a1475cdc8aec66e5914dc586f839d63` |
|  `2.45.1` `glibc-2.45.1`                                                                                                                                   | May 30th     | `sha256:7a36e339581ac80e18551d55c884ad7843bbad822f50f27cf68b8e3c2e32bcfc` |
|  `glibc-2.45.1-dev` `2.45.1-dev`                                                                                                                           | May 30th     | `sha256:f8c6b4210586298cff7c8b93360dd6738d1d8e1a7defeeaed58a8ab92d8bd557` |

