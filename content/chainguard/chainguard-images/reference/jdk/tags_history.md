---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-24 00:45:45
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
|  `latest-dev` | May 23rd     | `sha256:03daa96a67995fff16e3a699260ed0367c7b0cfc3e62ce8ec9ae03d63a634b78` |
|  `latest`     | May 23rd     | `sha256:0d5d8245ee011b41c630181d78800f916fdc370d15469bbd337e22788f06dc39` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `openjdk-22` `openjdk-22.0.1` `openjdk-22.0`                             | May 24th     | `sha256:48346bbc03c6370442e7444653369520ab9cdbac02b593cd8e6f8573ff3f551a` |
|  `openjdk-8.392` `openjdk-8.392.08` `openjdk-8`                                    | May 24th     | `sha256:33fcedb516b58752b167edc2cd450b4245887c2515460307832e7734df703dac` |
|  `openjdk-15` `openjdk-15.0.10` `openjdk-15.0` `openjdk-15.0.10.5`                 | May 24th     | `sha256:de468fee7d4462d27e1add9531844ee2551c7e7f2d54a7bec5f671a26acfa0a6` |
|  `openjdk-8-dev` `openjdk-8.392.08-dev` `openjdk-8.392-dev`                        | May 24th     | `sha256:69eea94e21d69f6ec26ea90e6747c3e01f277a0cf94c30b8d93c4ebfb8d1f68d` |
|  `openjdk-22.0-dev` `openjdk-22-dev` `latest-dev` `openjdk-22.0.1-dev`             | May 24th     | `sha256:b066a6a0984b4cedfd5e4db2dbeec63c01e42daf24d47fed27fa8fa7e82f426d` |
|  `openjdk-16-dev` `openjdk-16.0-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0.2-dev`   | May 24th     | `sha256:acfeb35c44c2978db1ecef4cffc78cd9dd7d70a4a3250927020def4f17e80e35` |
|  `openjdk-14.0` `openjdk-14.0.2` `openjdk-14` `openjdk-14.0.2.12`                  | May 24th     | `sha256:417422d0a3524ce954a6de7f18d6e9874865447ed80acfc90941a39a3d93880e` |
|  `openjdk-17-dev` `openjdk-17.0.11-dev` `openjdk-17.0-dev`                         | May 24th     | `sha256:a031ba23ece786f9970ada89e1a2ad7a1b41b898392cd851e6adfcdcd6d5618d` |
|  `openjdk-11.0.23-dev` `openjdk-11-dev` `openjdk-11.0-dev`                         | May 24th     | `sha256:19f0ec1e466f664f915e2cb521b579efe8991a372ef2546d4bcba43e8a73b7f7` |
|  `openjdk-21-dev` `openjdk-21.0-dev` `openjdk-21.0.3-dev`                          | May 24th     | `sha256:7b5f6d44c834b2314780a5d23f3d2de8f655e7ed4b61874a561126c92d49c075` |
|  `openjdk-14-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0-dev` `openjdk-14.0.2-dev`  | May 24th     | `sha256:d78eab6382b78d4114a08229768ebffb7740b0cd6138a5283df4798ad52bf993` |
|  `openjdk-21.0.3` `openjdk-21.0` `openjdk-21`                                      | May 24th     | `sha256:333f32607d8c55ace6248d5f2f4f3cb256d6e89e631b939106885324d6639531` |
|  `openjdk-11.0` `openjdk-11` `openjdk-11.0.23`                                     | May 24th     | `sha256:7f2290f636675cd59c1843fe547200b4c60fa39126bcfa795e8eb5b6a0e5134f` |
|  `openjdk-15-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0-dev` `openjdk-15.0.10-dev` | May 24th     | `sha256:38e96b32afed85a637705a61be0405a99cc021b0662e902d3f79ba4e6a7782ea` |
|  `openjdk-16.0.2.7` `openjdk-16.0` `openjdk-16.0.2` `openjdk-16`                   | May 24th     | `sha256:4f1eec3c24c913a93e01ab32689aef62370b42098312d048f6625f5b02793099` |
|  `openjdk-17.0.11` `openjdk-17.0` `openjdk-17`                                     | May 24th     | `sha256:e11f1265ad6489bc37f5bbb90141ad98c3342d5b383f76a097466ed061a8bd69` |
|  `openjdk-11.0.19.5-dev` `openjdk-11.0.19-dev`                                     | May 16th     | `sha256:892756bac53e2b57c43cd8b92d1790d223a18535e7186167dd65b41a51bdab7d` |
|  `openjdk-11.0.19.5` `openjdk-11.0.19`                                             | May 16th     | `sha256:4f282df7a3ebd9751b2372d077f7525f93f379e037cdf3b0d9cb3eb081fde668` |

